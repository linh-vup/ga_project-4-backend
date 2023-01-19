from .common import ColorSerializer
from foods.serializers.common import FoodSerializer

class PopulatedColorSerializer(ColorSerializer):
    foods = FoodSerializer(many=True)