from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .models import UserDay
from .serializers import UserDaySerializer, PopulatedUserDaySerializer


class UserDayListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        is_staff = request.user.is_staff
        is_user = request.user.id
        print("REQUEST USER", request.user.id)
        if is_staff:
            user_days = UserDay.objects.all()  # get everything from the shows table in the db
        else:
            user_days = UserDay.objects.filter(user=request.user.id)
        # run everything through the serializer
        serialized_user_days = PopulatedUserDaySerializer(user_days, many=True)
        # return the response and a status
        return Response(serialized_user_days.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['user'] = request.user.id
        user_day_to_add = UserDaySerializer(data=request.data)
        try:
            user_day_to_add.is_valid()
            user_day_to_add.save()
            return Response(user_day_to_add.data, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class UserDayDetailView(APIView):
    permission_classes = (IsAuthenticated, )

    def get_user_day(self, pk):
        try:
            return UserDay.objects.get(pk=pk)
        except UserDay.DoesNotExist:
            raise NotFound(detail='Cannot find user days')

    def get(self, _request, pk):
        try:
            user_day = self.get_user_day(pk=pk)
            # user_day = UserDay.objects.get(pk=pk)
            serialized_user_day = PopulatedUserDaySerializer(user_day)
            return Response(serialized_user_day.data, status=status.HTTP_200_OK)
        except UserDay.DoesNotExist:
            raise NotFound(detail="Can't find user day!")

    def put(self, request, pk):
        user_day_to_edit = self.get_user_day(pk=pk)
        is_user = request.user.id
        if not is_user:
            raise PermissionDenied()
        updated_user_day = UserDaySerializer(
            user_day_to_edit, data=request.data)
        try:
            updated_user_day.is_valid()
            updated_user_day.save()
            user_day = self.get_user_day(pk=pk)
            serialized_user_day = PopulatedUserDaySerializer(user_day)
            return Response(serialized_user_day.data, status=status.HTTP_202_ACCEPTED)

        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            res = {
                "detail": "Unprocessable Entity"
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, pk):
        try:
            user_day_to_delete = UserDay.objects.get(pk=pk)
            if user_day_to_delete != request.user:
                raise PermissionDenied()
            user_day_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UserDay.DoesNotExist:
            raise NotFound(detail="Comment not found")
