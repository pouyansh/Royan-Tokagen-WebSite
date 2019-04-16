from django.db import models


class ResearchArea(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
