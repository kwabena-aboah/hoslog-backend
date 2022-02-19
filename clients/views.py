from django.shortcuts import get_object_or_404, render
# from django.utils import timezone
# from django.core import serializers
from django.db.models import Sum, Count, Min, Max, Avg
from django.db.models.functions import TruncMonth
from rest_framework import viewsets
# from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
# from django.http import JsonResponse
from django.contrib import messages
from rest_framework import generics, status
from . serializer import ClientSerializer, ChartSerializer
from . permissions import ClientOwner
from . models import Client

def index(request):
    message = messages.add_message(request, messages.INFO, 'Welcome to HosLog.')
    return render(request, 'clients/index.html', {'messages': message})


class ClientViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, ClientOwner,)
    lookup_field = "id"
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


# @api_view(http_method_names=['GET'])
class TotalClients(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ChartSerializer
    permission_classes = (IsAuthenticated, ClientOwner,)
    lookup_field = "id"
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Client.objects.all()
        month = self.request.query_params.get('month', None)
        if month is not None:
            queryset = queryset.annotate(month=TruncMonth('date_of_arrival')).values('month').annotate(total=Count('id'))#.filter(user=self.request.user)
        # return self.queryset.filter(user=self.request.user)
        return queryset
            
    
    