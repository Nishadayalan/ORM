
from django.db import models
from django.contrib import admin
class footballplayer(models.Model):
    name=models.CharField(max_length=10)
    team=models.CharField(max_length=15)
    goals=models.IntegerField()
    jerseyno=models.IntegerField()
    age=models.IntegerField()
    redcards=models.IntegerField()
    numberofmatches=models.IntegerField()
class footballplayerAdmin(admin.ModelAdmin):
    list_display=["name","team","goals","jerseyno","age","redcards","numberofmatches"]

    