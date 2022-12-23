from django.urls import path
from seyahat_agency_app import views


urlpatterns = [
    path('', views.home_page, name="home")
]
