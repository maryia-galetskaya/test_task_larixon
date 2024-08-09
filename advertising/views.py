from rest_framework import generics
from .models import Advert
from .serializers import AdvertSerializer, AdvertCreateUpdateSerializer
from django.shortcuts import get_object_or_404

class AdvertListView(generics.ListAPIView):
    queryset = Advert.objects.select_related('city', 'category').all()
    serializer_class = AdvertSerializer

class AdvertDetailView(generics.RetrieveAPIView):
    queryset = Advert.objects.select_related('city', 'category').all()
    serializer_class = AdvertSerializer

    def get_object(self):
        obj = get_object_or_404(Advert, pk=self.kwargs["pk"])
        obj.views += 1
        obj.save()
        return obj