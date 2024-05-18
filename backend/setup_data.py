from datetime import datetime
from cars.models import AppUser, UserProfile, CarModel, Car, Advertisement

# Create sample users
user1 = AppUser.objects.create(
    first_name="John", last_name="Doe", email="john@example.com", password="password"
)
user2 = AppUser.objects.create(
    first_name="Alice",
    last_name="Smith",
    email="alice@example.com",
    password="password",
)
user3 = AppUser.objects.create(
    first_name="Bob", last_name="Johnson", email="bob@example.com", password="password"
)

# Create sample user profiles
profile1 = UserProfile.objects.create(
    account_id=user1,
    street_name="Main Street",
    street_number="123",
    zip_code="12345",
    city="City",
)
profile2 = UserProfile.objects.create(
    account_id=user2,
    street_name="Oak Avenue",
    street_number="456",
    zip_code="54321",
    city="Town",
)
profile3 = UserProfile.objects.create(
    account_id=user3,
    street_name="Elm Street",
    street_number="789",
    zip_code="67890",
    city="Village",
)

# Create sample car models
car_model1 = CarModel.objects.create(make="Toyota", model="Corolla")
car_model2 = CarModel.objects.create(make="Honda", model="Civic")
car_model3 = CarModel.objects.create(make="Ford", model="Mustang")

# Create sample cars
car1 = Car.objects.create(
    number_of_owners=1,
    registration_number="ABC123",
    manufacture_year=2018,
    car_model_id=car_model1,
    mileage=50000,
)
car2 = Car.objects.create(
    number_of_owners=2,
    registration_number="XYZ789",
    manufacture_year=2020,
    car_model_id=car_model2,
    mileage=30000,
)
car3 = Car.objects.create(
    number_of_owners=1,
    registration_number="DEF456",
    manufacture_year=2016,
    car_model_id=car_model3,
    mileage=70000,
)

# Create sample advertisements
advertisement1 = Advertisement.objects.create(
    advertisement_date=datetime.now(), car_id=car1, seller_account_id=user1
)
advertisement2 = Advertisement.objects.create(
    advertisement_date=datetime.now(), car_id=car2, seller_account_id=user2
)
advertisement3 = Advertisement.objects.create(
    advertisement_date=datetime.now(), car_id=car3, seller_account_id=user3
)

print("Sample data populated successfully!")
