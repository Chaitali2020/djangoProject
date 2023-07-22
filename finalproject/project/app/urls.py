from django.urls import path
from . import views

urlpatterns = [
   path('food',views.foodform),
   path('create_food',views.create_food),
   path('get_food',views.get_food),
   path('',views.index),
   path('edit/<rid>',views.edit),
   path('delete/<rid>',views.delete)
]
