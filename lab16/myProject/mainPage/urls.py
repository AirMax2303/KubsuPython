from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('add-shop', views.addShop, name='add-shop'),
    path('show-details/<manufacturer_id>/<model_id>/<_id>', views.showDetails),
    path('add-manufacturer', views.addManufacturer, name='add-manufacturer'),
    path('add-tech', views.addTech, name='add-tech')
]
