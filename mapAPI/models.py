from django.db import models

class Curriculum(models.Model):
 name = models.CharField(max_length=255)

class Info_Delete(models.Model):
 id = models.CharField(primary_key=True,max_length=20)
 pw = models.CharField(max_length=20)
 email = models.CharField(max_length=20)


class Info_Update(models.Model):
 key = models.IntegerField(primary_key=True, default=0)
 id = models.CharField(max_length=20)
 pw = models.CharField(max_length=20)
 email = models.CharField(max_length=20)