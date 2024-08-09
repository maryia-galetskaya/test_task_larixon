from rest_framework.serializers import ModelSerializer
from .models import Category, City, Advert

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ['name']

class AdvertSerializer(ModelSerializer):
    city = CitySerializer()
    category = CategorySerializer()

    class Meta:
        model = Advert
        fields = ['created', 'title', 'description', 'city', 'category', 'views']
        read_only_fields = ['views']

class AdvertCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Advert
        fields = ['title', 'description', 'city', 'category']
