from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    user = models.ForeignKey(User, related_name="user_movie", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=20, blank=True, null=True)
    actors = models.CharField(max_length=255, blank=True, null=True)
    awards = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    dvd = models.CharField(max_length=20, blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    plot = models.CharField(max_length=500, blank=True, null=True)
    released = models.CharField(max_length=20, blank=True, null=True)
    runtime = models.CharField(max_length=20, blank=True, null=True)
    poster = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title
