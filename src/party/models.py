#encoding:utf-8

from django.db import models
from django.contrib.auth.models import User

class Party(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    master = models.ForeignKey(User)
    status = models.CharField(max_length=10)
    players = models.ManyToManyField(User, through='Character', related_name='characters')

class Scene(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    party = models.ForeignKey(Party)

class Narration(models.Model):
    text = models.TextField()
    scene = models.ForeignKey(Scene)
    player = models.ForeignKey(User)

class Character(models.Model):
    name = models.CharField(max_length=100)
    history = models.TextField()
    player = models.ForeignKey(User)
    party = models.ForeignKey(Party)