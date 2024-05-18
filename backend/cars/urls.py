from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/appusers/', views.AppUserList.as_view()),
    path('api/v1/appusers/<int:pk>/', views.AppUserDetail.as_view()),
    path('api/v1/userprofiles/', views.UserProfileList.as_view()),
    path('api/v1/userprofiles/<int:pk>/', views.UserProfileDetail.as_view()),
    path('api/v1/carmodels/', views.CarModelList.as_view()),
    path('api/v1/carmodels/<int:pk>/', views.CarModelDetail.as_view()),
    path('api/v1/cars/', views.CarListView.as_view()), 
    path('api/v1/cars/<int:pk>/', views.CarDetailView.as_view()),
    path('api/v1/advertisements/', views.AdvertisementList.as_view()),
    path('api/v1/advertisements/<int:pk>/', views.AdvertisementDetail.as_view()),
]
