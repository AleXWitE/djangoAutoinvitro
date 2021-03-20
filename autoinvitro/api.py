from .models import News, Notification, Sale, SaleItem, Car, Forum, Posts, Events
from rest_framework import viewsets, permissions
from .serializers import NewsSerializer, NotificationSerializer, SaleSerializer, SaleItemSerializer, CarSerializer, ForumSerializer, PostsSerializer,EventsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NewsSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NotificationSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SaleSerializer


class SaleItemViewSet(viewsets.ModelViewSet):
    queryset = SaleItem.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SaleItemSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer


class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ForumSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostsSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EventsSerializer
