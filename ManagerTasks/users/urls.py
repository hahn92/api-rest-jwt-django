# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    path('', views.ListUsersAPIView.as_view(), name='get_users'),
]

