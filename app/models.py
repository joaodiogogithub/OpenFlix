from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    genre = models.CharField(max_length=100, blank=False, null=False)
    descripton = models.TextField(blank=False, null=False)
    qnt_episodes = models.IntegerField(blank=False, null=False)
    rating = models.FloatField(blank=False, null=False)
    thumb = models.CharField(max_length=1000, blank=False, null=False)