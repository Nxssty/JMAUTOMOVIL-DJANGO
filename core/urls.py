from django.urls import path
from .views import home, descripcion, crear_auto

urlpatterns = [
    path('', home, name='home'),
    path('descripcion/<int:id>/', descripcion, name='descripcion'),
    path('crear/', crear_auto, name='crear_auto'),
]
