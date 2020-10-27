from rest_framework import generics
from todos import models
from .serializers import ListItemSerializer

class Item(generics.ListCreateAPIView):
    queryset = models.ListItem.objects.all()
    serializer_class = ListItemSerializer

class Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ListItem.objects.all()
    serializer_class = ListItemSerializer

# Create your views here.
