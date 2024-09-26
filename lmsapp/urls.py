from django.urls import path
from lmsapp.views import register

urlpatterns = [

    path('register/', register, name='register')
]