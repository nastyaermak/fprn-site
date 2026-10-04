import re

from django.db import migrations, models

# "Назва, Країна", "Назва (Країна)" або "Назва - Країна"
UNIVERSITY_PATTERN = re.compile(r"^(?P<name>.+?)\s*(?:,|\(|\s-\s)\s*(?P<country>[^()]+?)\)?\s*$")


def split_university(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        match = UNIVERSITY_PATTERN.match(program.university)
        if match:
            program.university = match.group("name")
            program.country = match.group("country")
            program.save(update_fields=["university", "country"])


def join_university(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.exclude(country=""):
        program.university = f"{program.university}, {program.country}"
        program.save(update_fields=["university"])


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0002_load_dean_office_programs"),
    ]

    operations = [
        migrations.AddField(
            model_name="exchangeprogram",
            name="country",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.RunPython(split_university, join_university),
    ]
