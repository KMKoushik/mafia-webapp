# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
import json




# Create your models here.
class Game(models.Model):

    name = models.CharField(max_length=100,null=False)
    player = models.IntegerField(null=False)
    roles = models.CharField(max_length=500)
    playerDetails = models.TextField()


    # this returns the name of the user when the object of user is printed
    def __str__(self):
        return self.name

    def getAsDict(self):
        userJson = {}
        userJson["name"] = self.name
        userJson["player"] = self.player
        userJson["roles"] = self.roles
        userJson["playerDetails"] = self.playerDetails
        return userJson

    def getJson(self):
        return str(self.playerDetails)
