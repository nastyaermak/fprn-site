import re

from django.db import migrations, models


def places_to_number(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        # беру перше число з тексту, "до 4" рахую як 4
        match = re.search(r"\d+", program.places)
        program.places_number = int(match.group()) if match else 0
        program.save(update_fields=["places_number"])


def places_to_text(apps, schema_editor):
    # назад можна повернути тільки число, текст типу "2 місця" вже не відновити
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.places = str(program.places_number)
        program.save(update_fields=["places"])


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0003_split_university_and_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="exchangeprogram",
            name="places_number",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.RunPython(places_to_number, places_to_text),
        # без default відкат падав, sqlite не міг додати назад not null колонку
        migrations.AlterField(
            model_name="exchangeprogram",
            name="places",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.RemoveField(
            model_name="exchangeprogram",
            name="places",
        ),
        migrations.RenameField(
            model_name="exchangeprogram",
            old_name="places_number",
            new_name="places",
        ),
        migrations.AlterField(
            model_name="exchangeprogram",
            name="places",
            field=models.PositiveIntegerField(),
        ),
    ]
