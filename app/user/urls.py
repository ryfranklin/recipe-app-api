from django.urls import path
from django.urls.resolvers import URLPattern

from user import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]
