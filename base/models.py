from django.db import models

import uuid


class Parent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    street_address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    zip = models.CharField(max_length=256)


class Child(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    parent = models.ForeignKey(Parent, related_name='children', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
