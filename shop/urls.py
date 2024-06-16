from django.urls import path

from shop import views
from shop.apps import ShopConfig

app_name = ShopConfig.name
urlpatterns = [
    path('<int:pk>/', views.product, name='product'),
    path('', views.product_list, name='product_list')
]