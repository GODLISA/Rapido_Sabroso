from django.urls import path
from .views import *

urlpatterns = [
    path('', vista1, name="vista1"),
    path('menu', menu, name="menu"),
    path('logout/', logout_view, name='logout'),
    path('marca/<str:marca>/', productos_por_marca, name='marca'),
    path('categoria/<str:categoria>/', categorias, name='categoria'),
    path('producto/<int:id>/', producto, name='producto'),
    
]

