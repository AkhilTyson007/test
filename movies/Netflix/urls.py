from django.urls import path
from . import views

urlpatterns = [
    path('salaar/', views.salaar, name="salaar"),
    path('func/', views.func, name="func"),
    path('result/',views.result, name='result'),
    path('testing/',views.testing, name='testing'),
    path('add/',views.add, name='add'),
    path('studDetails/',views.studDetails, name='studDetails'),
    path('register/',views.register, name='register'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    
]

