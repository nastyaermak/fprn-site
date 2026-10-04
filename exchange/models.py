from django.db import models


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    languages = models.CharField(max_length=200)
    places = models.PositiveIntegerField()
    deadline = models.DateField()
    description = models.TextField()

    class Meta:
        ordering = ["deadline"]

    def __str__(self):
        return self.university
