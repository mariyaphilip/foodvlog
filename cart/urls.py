from django.urls import path
from . import views

urlpatterns=[
    path('cartDetails',views.cart_Details,name='cartDetails')
]