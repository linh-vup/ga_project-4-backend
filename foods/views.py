from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.exceptions import NotFound
from django.db import IntegrityError
from django.db.models import Q 

from .serializers.common import FoodSerializer
from .serializers.populated import PopulatedFoodSerializer
from .models import Food

class FoodListView(APIView):
    def get(self, _request):
        foods = Food.objects.all()
        serialized_foods = PopulatedFoodSerializer(foods, many=True)
        return Response(serialized_foods.data, status=status.HTTP_200_OK)

    def post(self, request):
        food_to_add = FoodSerializer(data=request.data)
        try:
            food_to_add.is_valid()
            food_to_add.save()
            return Response(food_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class FoodDetailView(APIView):
    def get_food(self, pk):
        try:
            return Food.objects.get(pk=pk)
        except Food.DoesNotExist:
            raise NotFound(detail='Cannot find food')
    
    
    def get(self, _request, pk):
        try:
            food = self.get_food(pk=pk)
            serialized_food = PopulatedFoodSerializer(food)
            return Response(serialized_food.data, status=status.HTTP_200_OK)
        except Food.DoesNotExist:
            raise NotFound(detail="Can't find food!")

    def put(self, request, pk):
        food_to_edit = self.get_food(pk=pk)
        updated_food = FoodSerializer(food_to_edit, data=request.data)
        try:
            updated_food.is_valid()
            updated_food.save()
            return Response(updated_food.data, status=status.HTTP_202_ACCEPTED)
        
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            res = {
                "detail": "Unprocessable Entity"
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        food_to_delete = Food.objects.get(pk=pk)
        print("food TO DELETE", food_to_delete)
        food_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FoodSearchView(APIView):
    def get(self, request):      
        query = request.GET.get('search')
        print("THIS QUERY", query)                
        results = Food.objects.filter(Q(name__icontains=query))
        serialied_results = PopulatedFoodSerializer(results, many=True)
        return Response(serialied_results.data)