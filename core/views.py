from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Country, Brand, Car, Comment
from core.serializers import CountrySerializer, BrandSerializer, CarSerializer, CommentSerializer


def index(request):
    return render(request, 'core/index.html')


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class CommentQuestPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == "POST" or request.method in permissions.SAFE_METHODS


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('id')
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('id')
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('id')
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('id')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated|CommentQuestPermissions]
