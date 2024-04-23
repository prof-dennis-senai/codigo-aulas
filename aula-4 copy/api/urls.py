from django.urls import path, include
from rest_framework import routers
from api.api.viewsets import PessoaViewSet

route = routers.DefaultRouter()

route.register('pessoa',PessoaViewSet, basename='pessoa_api')

urlpatterns = [
    path('',include(route.urls)),
]
