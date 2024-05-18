from django.db import models


class AppUser(models.Model):
    account_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=100)
    street_number = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)


class CarModel(models.Model):
    car_model_id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    number_of_owners = models.IntegerField()
    registration_number = models.CharField(unique=True, max_length=100)
    manufacture_year = models.IntegerField()
    number_of_doors = models.IntegerField(default=5)
    car_model_id = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    mileage = models.IntegerField(null=True)


class Advertisement(models.Model):
    advertisement_id = models.AutoField(primary_key=True)
    advertisement_date = models.DateTimeField()
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    seller_account_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)
