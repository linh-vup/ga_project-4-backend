from rest_framework import serializers
from .models import UserDay
# from foods.serializers.common import FoodSerializer
from foods.serializers.populated import PopulatedFoodSerializer


class UserDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDay
        fields = '__all__'


class PopulatedUserDaySerializer(UserDaySerializer):
    # foods_consumed = FoodSerializer(many = True)
    foods_consumed = PopulatedFoodSerializer(many=True)