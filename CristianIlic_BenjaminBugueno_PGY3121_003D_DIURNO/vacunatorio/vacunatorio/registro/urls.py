from django.urls import path
from registro import views as v

urlpatterns = [
    path('', v.inicio)
]