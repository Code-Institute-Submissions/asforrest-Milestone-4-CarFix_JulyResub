from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_mechanics, name='mechanics'),
    path('<mechanic_id>', views.mechanic_detail, name='mechanic_detail'),
]
