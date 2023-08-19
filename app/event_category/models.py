from django.db import models

class EventCategory(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name