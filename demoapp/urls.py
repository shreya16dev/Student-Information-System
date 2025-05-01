
from django.urls import path,include
from .views import*
urlpatterns = [
    path('',home,name="home"), 
    path('stusave/',stusave,name="stusave"),
    path('deletestu/<int:id>',deletestu,name="deletestu"),
    path('editstu/<int:id>',editstu,name="editstu"),
]