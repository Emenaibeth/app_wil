from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='notas_index'),
    path('eliminar/<int:nota_id>/', views.eliminar_nota, name='eliminar_nota'),
]