from django.db import models

class UserDay(models.Model):
    user = models.CharField(max_length=50)
    day_logged = models.DateField(blank=True)
    foods_consumed = models.ManyToManyField('foods.Food', related_name='user_days')
    
    def __str__(self):
        return f"{self.user}"