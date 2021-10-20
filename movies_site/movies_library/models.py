from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Actor(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):
    GENERAL_AUDIENCES = 'G'
    PARENTAL_GUIDANCE_SUGGESTED = 'PG'
    PARENTS_STRONGLY_CAUTIONED = 'PG-13'
    RESTRICTED = 'R'
    NO_ONE_17_AND_UNDER_ADMITTED = 'NC-17'
    MOVIE_CERTIFICATE = [
        (GENERAL_AUDIENCES, 'General Audiences'),
        (PARENTAL_GUIDANCE_SUGGESTED, 'Parental Guidance Suggested'),
        (PARENTS_STRONGLY_CAUTIONED, 'Parents Strongly Cautioned'),
        (RESTRICTED, 'Restricted'),
        (NO_ONE_17_AND_UNDER_ADMITTED, 'No One 17 and Under Admitted')
    ]
    title = models.CharField(max_length=64)
    year = models.PositiveIntegerField(blank=False)
    actors = models.ManyToManyField(Actor)
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    certificate_rate = models.CharField(max_length=8, choices=MOVIE_CERTIFICATE, default=GENERAL_AUDIENCES)

    class Meta:
        unique_together = ('title', 'year')

    def __str__(self):
        return f'{self.title} ({self.year})'
