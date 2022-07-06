from django.urls import path, include

from rest_framework import routers

from api.views import UserViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]