from django.contrib import admin
from django.contrib.auth.models import Group

from app.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "year")
    list_filter = ("user", "year",)
    ordering = ("user",)


admin.site.site_header = "Movie Database: Admin site"

# unregister the Group model from admin.
admin.site.unregister(Group)
