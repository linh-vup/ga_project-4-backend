from .common import FoodSerializer
from colors.serializers.common import ColorSerializer

class PopulatedFoodSerializer(FoodSerializer):
  color = ColorSerializer()