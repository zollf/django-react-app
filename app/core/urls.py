from django.contrib import admin
from django.conf.urls import include, re_path
from django.urls import path 
from app.test_app.views import HomeView, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', HomeView, name='home'),
  re_path('^', include(router.urls)),
]
