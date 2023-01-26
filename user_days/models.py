from django.db import models

class UserDay(models.Model):
    user = models.ForeignKey('jwt_auth.User', related_name='user_days', on_delete=models.CASCADE)
    day_logged = models.DateField(blank=True)
    foods_consumed = models.ManyToManyField('foods.Food', related_name='user_days', blank=True)
    
    def __str__(self):
        return f"{self.day_logged} - {self.user}"