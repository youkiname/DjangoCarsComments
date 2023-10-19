from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views
from core import views

router = DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'cars', views.CarViewSet)
router.register(r'comments', views.CommentViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api/token-auth/', auth_views.obtain_auth_token),
    path('admin/', admin.site.urls),
]

