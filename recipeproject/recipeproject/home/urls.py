from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

    path('create/',views.create_recipe, name='create_recipe'),
    path('recipes/', views.recipe_list, name='recipe_list'),

]