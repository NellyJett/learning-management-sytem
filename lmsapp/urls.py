from django.urls import path
from lmsapp.views import register, result

urlpatterns = [

    path('register/', register, name='register'),

]