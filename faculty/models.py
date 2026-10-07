from django.db import models

UKRAINIAN_ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"


def ukrainian_sort_key(text):
    # sqlite сортує по кодах unicode, тому Є та І були вище за А
    return [UKRAINIAN_ALPHABET.find(char) if char in UKRAINIAN_ALPHABET else ord(char) for char in text.lower()]


class FacultyInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contacts = models.TextField()

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200)
    head = models.CharField(max_length=200)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=200)
    coordinator_contact = models.CharField(max_length=200)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="programs",
    )
    disciplines = models.TextField()

    class Meta:
        ordering = ["code", "name"]

    def __str__(self):
        return f"{self.code} {self.name}"


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    degree = models.CharField(max_length=200, blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="teachers",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
