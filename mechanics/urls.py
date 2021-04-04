from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_mechanics, name='machanics'),
    path('<machanic_id>', views.mechanic_detail, name='machanic_detail'),
]
