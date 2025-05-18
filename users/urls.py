from django.urls import path  
from .views import middleware_test

urlpatterns = [  
    path('test/', middleware_test, name='test'),
]  




