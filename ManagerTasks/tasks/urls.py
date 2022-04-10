# Django
from django.urls import path

from tasks import views

urlpatterns = [
    
    path('', views.ListCreateTasksAPIView.as_view(), name='get_post_task'),
    path('<int:pk>', views.RetrieveUpdateDestroyTasksAPIView.as_view(), name='get_delete_update_task'),

]
