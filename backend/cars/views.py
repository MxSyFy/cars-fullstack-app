from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import (AppUserSerializer, UserProfileSerializer, CarModelSerializer, CarSerializer, AdvertisementSerializer)
from .models import AppUser, UserProfile, CarModel, Car, Advertisement


# Create your views here.
###############################################################################
class AppUserList(APIView):
    def get(self, request):
        appusers = AppUser.objects.all()
        serializer = AppUserSerializer(appusers, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data})
        return Response({"error": serializer.errors})

class AppUserDetail(APIView):
    def get(self, request, pk):
        appuser = get_object_or_404(AppUser.objects.all(), pk=pk)
        serializer = AppUserSerializer(appuser)
        return Response({"result": serializer.data})

    def put(self, request, pk):
        appuser = get_object_or_404(AppUser.objects.all(), pk=pk)
        serializer = AppUserSerializer(appuser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data})
        return Response({"error": serializer.errors})

    def delete(self, request, pk):
        appuser = get_object_or_404(AppUser.objects.all(), pk=pk)
        appuser.delete()
        return Response({"result": "AppUser deleted"})


###############################################################################
class UserProfileList(APIView):
    def get(self, request):
        userprofiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(userprofiles, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data})
        return Response({"error": serializer.errors})

class UserProfileDetail(APIView):
    def get(self, request, pk):
        userprofile = get_object_or_404(UserProfile.objects.all(), pk=pk)
        serializer = UserProfileSerializer(userprofile)
        return Response({"result": serializer.data})

    def put(self, request, pk):
        userprofile = get_object_or_404(UserProfile.objects.all(), pk=pk)
        serializer = UserProfileSerializer(userprofile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data})
        return Response({"error": serializer.errors})

    def delete(self, request, pk):
        userprofile = get_object_or_404(UserProfile.objects.all(), pk=pk)
        userprofile.delete()
        return Response({"result": "UserProfile deleted"})


###############################################################################
class CarModelList(APIView):
    def get(self, request):
        carmodels = CarModel.objects.all()
        serializer = CarModelSerializer(carmodels, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        serializer = CarModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data})
        return Response({"error": serializer.errors})

class CarModelDetail(APIView):
    def get(self, request, pk):
        carmodel = get_object_or_404(CarModel.objects.all(), pk=pk)
        serializer = CarModelSerializer(carmodel)
        return Response({"result": serializer.data})

    def put(self, request, pk):
        carmodel = get_object_or_404(CarModel.objects.all(), pk=pk)
        serializer = CarModelSerializer(carmodel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data})
        return Response({"error": serializer.errors})

    def delete(self, request, pk):
        carmodel = get_object_or_404(CarModel.objects.all(), pk=pk)
        carmodel.delete()
        return Response({"result": "CarModel deleted"})


###############################################################################
class CarListView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data})
        return Response({"error": serializer.errors})

class CarDetailView(APIView):
    def get(self, request, pk):
        car = get_object_or_404(Car.objects.all(), pk=pk)
        serializer = CarSerializer(car)
        return Response({"result": serializer.data})

    def put(self, request, pk):
        car = get_object_or_404(Car.objects.all(), pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data})
        return Response({"error": serializer.errors})

    def delete(self, request, pk):
        car = get_object_or_404(Car.objects.all(), pk=pk)
        car.delete()
        return Response({"result": "Car deleted"})


###############################################################################
class AdvertisementList(APIView):
    def get(self, request):
        advertisements = Advertisement.objects.all()
        serializer = AdvertisementSerializer(advertisements, many=True)
        return Response({"result": serializer.data})

    def post(self, request):
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data})
        return Response({"error": serializer.errors})

class AdvertisementDetail(APIView):
    def get(self, request, pk):
        advertisement = get_object_or_404(Advertisement.objects.all(), pk=pk)
        serializer = AdvertisementSerializer(advertisement)
        return Response({"result": serializer.data})

    def put(self, request, pk):
        advertisement = get_object_or_404(Advertisement.objects.all(), pk=pk)
        serializer = AdvertisementSerializer(advertisement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data})
        return Response({"error": serializer.errors})

    def delete(self, request, pk):
        advertisement = get_object_or_404(Advertisement.objects.all(), pk=pk)
        advertisement.delete()
        return Response({"result": "Advertisement deleted"})