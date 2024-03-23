from django.urls import path
from .import views
urlpatterns = [
    path('login/',views.login,name='Login'),
    path('',views.guesthome,name='guesthome'),
    path('servicereg/',views.servicereg,name='servicereg'),
    path('filldistrict/',views.filldistrict,name='filldistrict'),
    path('filllocation/',views.filllocation,name='filllocation'),
    path('customerreg/', views.customerreg, name='customerreg'),
]