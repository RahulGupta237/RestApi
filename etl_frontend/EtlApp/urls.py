from django.urls import path, include
from EtlApp.views import Login,uploadPdf
urlpatterns = [
    path('', Login,name="login"),
    path('upload/',uploadPdf,name="uploadPdf")
]