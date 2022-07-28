from django.urls import path
from .views import home, mainmenu

urlpatterns = [
    path('', home, name='home'),
    path('menu/',mainmenu, name='mainmenu')
]
