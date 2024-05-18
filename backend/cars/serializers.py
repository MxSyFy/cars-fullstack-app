from rest_framework import serializers
from .models import AppUser, UserProfile, CarModel, Car, Advertisement


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['account_id', 'first_name', 'last_name', 'email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['profile_id', 'account_id', 'street_name', 'street_number', 'zip_code', 'city'] 


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['car_model_id', 'make', 'model']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['car_id', 'number_of_owners', 'registration_number', 'manufacture_year', 'number_of_doors', 'car_model_id', 'mileage']


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['advertisement_id', 'advertisement_date', 'car_id', 'seller_account_id']
