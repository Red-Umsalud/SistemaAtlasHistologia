from django.urls import path, include
from .views import home, mainmenu, show, refreshContent

urlpatterns = [
    path('', home, name='home'),
    path('menu/',mainmenu, name='mainmenu'),
    path('menu/<pk>', show, name='show'),
    path('refreshContent/<pk>', refreshContent, name='refreshContent'),
    path('tinymce/', include('tinymce.urls'))
]
