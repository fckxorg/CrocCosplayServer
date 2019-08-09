from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CosplayElement(models.Model):
    uuid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    cost = models.IntegerField()
    url = models.CharField(max_length=1000)


class Ability(models.Model):
    uuid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    damage = models.IntegerField()
    picture = models.FileField(upload_to="static/pictures/ability")


class Character(models.Model):
    uuid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    abilities = models.ManyToManyField(Ability)
    cosplay_elements = models.ManyToManyField(CosplayElement)
    picture = models.FileField(upload_to="static/pictures/character/")


class Fight(models.Model):
    uuid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    team_evil = models.ManyToManyField(User, related_name="team_evil")
    team_good = models.ManyToManyField(User, related_name="team_good")
    victor = models.CharField(max_length=200)
    date = models.DateTimeField()
    picture = models.FileField(upload_to="static/pictures/fight/")


class SubEvent(models.Model):
    uuid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    date = models.DateTimeField()


class Event(models.Model):
    uuid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField()
    picture = models.FileField(upload_to="static/pictures/event/")
    characters = models.ManyToManyField(Character)
    members = models.ManyToManyField(User)
    fights = models.ManyToManyField(Fight)
    sub_events = models.ManyToManyField(SubEvent)


class AttendedCharacter(models.Model):
    uuid = models.AutoField(primary_key=True)
    character = models.ForeignKey(Character, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)

