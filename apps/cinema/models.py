from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=24, blank=True)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.age}'

class Movie(models.Model):
    title = models.CharField(max_length=32, blank=True)
    description = models.TextField()
    release = models.DateTimeField()
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f'{self.title} {self.release}'