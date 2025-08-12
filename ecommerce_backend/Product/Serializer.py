from Serializer import ModelSerializer
from .models import Products

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        read_only_fields = ('id',)  # Assuming 'id' is an auto-generated field