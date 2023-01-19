from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=50)
    color = models.ForeignKey('colors.Color', related_name='foods', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
