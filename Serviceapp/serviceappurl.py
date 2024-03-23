from django.urls import path
from .import views
urlpatterns = [
    path('servicehome/',views.home,name='home'),
    path('travelreg/',views.travelreg,name='travelreg'),
    path('filldistrict/',views.filldistrict,name='filldistrict'),
    path('filllocation/',views.filllocation,name='filllocation'),
    path('travelview/',views.travelview,name='travelview'),
    path('traveldelete/<id>', views.traveldelete, name='traveldelete'),
    path('cateringreg/',views.cateringreg,name='cateringreg'),
    path('traveledit/<id>', views.traveledit, name='traveledit'),
    path('cateringview/',views.cateringview,name='cateringview'),
    path('cateringdelete/<id>', views.cateringdelete, name='cateringdelete'),
    path('cateringedit/<id>', views.cateringedit, name='cateringedit'),
    path('destinationreg/',views.destinationreg,name='destinationreg'),
    path('destinationview/',views.destinationview,name='destinationview'),
    path('destinationdelete/<id>', views.destinationdelete, name='destinationdelete'),
    path('destinationedit/<id>', views.destinationedit, name='destinationedit'),
    path('fillcategory/',views.fillcategory,name='fillcategory'),
    path('serviceregistration/',views.serviceregistration,name='serviceregistration'),
    path('serviceregisterview/',views.serviceregisterview,name='serviceregisterview'),

]