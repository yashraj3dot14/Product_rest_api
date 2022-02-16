from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


# Create your views here.
class AddProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [IsAuthenticated]

class AllProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [IsAuthenticated]