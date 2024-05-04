from django.db import models


class Todo(models.Model):
    name = models.TextField(max_length=50)
    desc = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=True)

