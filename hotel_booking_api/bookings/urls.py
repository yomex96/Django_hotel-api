from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/<int:pk>/', views.booking_detail, name='booking_detail'),

    path('reviews/', views.review_list, name='review_list'),
    path('reviews/<int:pk>/', views.review_detail, name='review_detail'),

]