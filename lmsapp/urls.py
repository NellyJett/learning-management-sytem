from django.urls import path
from lmsapp.views import home
from lmsapp.views import register

urlpatterns = [
    path('home/', home, name='home'),

    path('register/', register.as_view(), name='register')
]