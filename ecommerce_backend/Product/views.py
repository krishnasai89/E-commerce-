from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Products
from .Serializer import ProductSerializer
# Create your views here.
class ProductListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
