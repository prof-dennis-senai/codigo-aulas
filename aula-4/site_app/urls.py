from django.urls import path
from .views import home, produtos, precos

urlpatterns = [
    path('', home),
    path('produtos/', produtos),
    path('precos/', precos),
    path('precos/<int:id>', precos),
]
