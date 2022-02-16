from django.urls import path,include
from . import views


app_name = 'api'
urlpatterns = [
    path('addproduct/', views.AddProduct.as_view(), name= 'add_product'),
    path('allproducts/', views.AllProduct.as_view(), name= 'product_list'),
    path('product/<int:pk>/', views.ProductDetails.as_view(), name= 'product_details'),

    path('api-auth', include('rest_framework.urls')),
]