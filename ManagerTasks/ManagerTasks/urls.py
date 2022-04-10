"""ManagerTasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path, include 

# JWT
from users.token import MyTokenObtainPairView, MyTokenRefreshView


urlpatterns = [
 ################################################# ADMIN #################################################
    path('admin/', admin.site.urls),
    
    ################################################# API #################################################
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/users/', include(('users.urls', 'users'), namespace='users')),
    path('api/v1/tasks/', include(('tasks.urls', 'tasks'), namespace='tasks')),

]
if not settings.MEDIA:
    urlpatterns += static(
        settings.STATIC_URL, 
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )

