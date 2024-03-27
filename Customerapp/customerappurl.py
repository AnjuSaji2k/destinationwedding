from django.urls import path
from .import views
urlpatterns = [
    path('customerhome/',views.customerhome,name='customerhome'),
    path('categoryview/',views.categoryview,name='categoryview'),
    path('subcategoryview/<id>',views.subcatview,name='subcatview'),
    path('servicesview/<id>',views.servicesview,name='servicesview'),
    path('servicesviewmore/<id>',views.servicesviewmore,name='servicesviewmore'),
    path('booking/<id>',views.booking,name='booking'),
    path('logout',views.logout,name='logout')






]