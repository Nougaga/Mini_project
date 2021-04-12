from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=255)
    user_pw = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_dog = models.CharField(max_length=255)

