from django.urls import path
from .views import home, mainmenu

urlpatterns = [
    path('', home),
    path('menu/',mainmenu)
]
