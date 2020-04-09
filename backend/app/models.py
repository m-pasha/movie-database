from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    user = models.ForeignKey(User, related_name="user_movie", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=20, blank=True)
    actors = models.CharField(max_length=255, blank=True)
    awards = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    dvd = models.CharField(max_length=20, blank=True)
    director = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    plot = models.CharField(max_length=500, blank=True)
    released = models.CharField(max_length=20, blank=True)
    runtime = models.CharField(max_length=20, blank=True)
    poster = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title
