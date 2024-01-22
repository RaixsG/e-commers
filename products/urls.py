from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search products'),
    path('', views.get_products, name='get_products'),
    path('get/<str:name>', views.get_product, name='get_product'),
    path('get/admin/<int:id>', views.get_product, name='get_product at admin'),
    path('post/', views.create_product, name='crear products'),
    path('edit/<int:pk>', views.edit_product, name='editar product'),
    path('delete/<int:pk>', views.delete_product, name='eliminar product'),
]