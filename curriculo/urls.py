from django.urls import path
from . import views

urlpatterns = [
    # Aspas vazias '' significa: é a página inicial do app
    path('', views.criar_curriculo, name='criar_curriculo'),
]