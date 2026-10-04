import re

from django.db import migrations, models


def places_to_number(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        # "5", "2 місця", "1 місце", "до 4": беремо число, для "до 4" це максимум місць
        match = re.search(r"\d+", program.places)
        program.places_number = int(match.group()) if match else 0
        program.save(update_fields=["places_number"])


def places_to_text(apps, schema_editor):
    # Повертає лише число: початковий текст ("2 місця", "до 4") відновити неможливо.
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
        # default потрібен, щоб при відкаті SQLite зміг повернути колонку в непорожню таблицю
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
