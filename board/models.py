from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    STATUS = ((0, 'TO DO'), (1, 'In Progress'), (2, 'Done'))
    status = models.IntegerField(choices=STATUS, default=0)
