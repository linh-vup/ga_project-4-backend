from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.exceptions import NotFound, PermissionDenied
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers.common import ColorSerializer
from .serializers.populated import PopulatedColorSerializer
from .models import Color

class ColorListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):
        colors = Color.objects.all()
        serialized_colors = ColorSerializer(colors, many=True)
        return Response(serialized_colors.data, status=status.HTTP_200_OK)

    def post(self, request):
        # if  request.data['is_staff'] != True:
        #     raise PermissionDenied()
        color_to_add = ColorSerializer(data=request.data)
        try:
            color_to_add.is_valid()
            color_to_add.save()
            return Response(color_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ColorDetailView(APIView):
    def get_color(self, pk):
        try:
            return Color.objects.get(pk=pk)
        except Color.DoesNotExist:
            raise NotFound(detail='Cannot find color')
    
    
    def get(self, _request, pk):
        try:
            color = self.get_color(pk=pk)
            serialized_food = PopulatedColorSerializer(color)
            return Response(serialized_food.data, status=status.HTTP_200_OK)
        except Color.DoesNotExist:
            raise NotFound(detail="Can't find color!")

    def put(self, request, pk):
        color_to_edit = self.get_color(pk=pk)
        updated_color = ColorSerializer(color_to_edit, data=request.data)
        try:
            updated_color.is_valid()
            updated_color.save()
            return Response(updated_color.data, status=status.HTTP_202_ACCEPTED)
        
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            res = {
                "detail": "Unprocessable Entity"
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        color_to_delete = Color.objects.get(pk=pk)
        print("color TO DELETE", color_to_delete)
        color_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
