from . import views
from django.urls import path


urlpatterns = [
    path('/image', views.process_image, name='home'),
    path('/pdf', views.process_pdf, name='pdf'),
    path('', views.homw, name='choice'),
]
