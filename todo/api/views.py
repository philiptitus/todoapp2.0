from django.shortcuts import render
from rest_framework import generics,permissions
from .serializers import TlistSerializer,TlistCompleteSerializer
from todoapp.models import Tlist
from django.utils import timezone

# Create your views here.
class TlistCreate(generics.ListCreateAPIView):
    serializer_class = TlistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        user = self.request.user
        return Tlist.objects.filter(user=user, date_completed__isnull=True)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class TlistComplete(generics.UpdateAPIView):
    serializer_class = TlistCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tlist.objects.filter(user=user)
    
    def perform_update(self, serializer):
        serializer.instance.date_completed = timezone.now()
        serializer.save()


class TlistCompletedTasks(generics.ListAPIView):
    serializer_class = TlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tlist.objects.filter(user=user, date_completed__isnull = False).order_by('-date_completed')
    

class TlistRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tlist.objects.filter(user=user)
    