from django.db import models

class Users(models.Model):
  name = models.CharField(db_index=True, max_length=255, unique=True)