from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=35)
    slug = models.CharField(max_length=35)

    def __str__(self):
        return f"{self.name}"