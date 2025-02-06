from django.urls import path
from apps.main_app.views import Index

urlpatterns = [
    path("", Index.as_view(), name='index'),
]