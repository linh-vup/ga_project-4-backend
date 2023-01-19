from rest_framework import serializers
from .models import UserDay


class UserDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDay
        fields = '__all__'