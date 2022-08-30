from django.urls import path, include
from .views import home, mainmenu, show

urlpatterns = [
    path('', home, name='home'),
    path('menu/',mainmenu, name='mainmenu'),
    path('menu/<pk>', show, name='show'),
    path('tinymce/', include('tinymce.urls'))
]
