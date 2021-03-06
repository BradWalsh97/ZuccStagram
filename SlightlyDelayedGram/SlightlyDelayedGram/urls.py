"""SlightlyDelayedGram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from users.views import PictureListView


urlpatterns = [
    path('', user_views.home, name='users-home'),
    path('Picture/<int:pk>/', user_views.picture_detail, name='picture_detail'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/upload', user_views.upload_picture, name='upload'),
    path('profile/<int:pk>/', user_views.delete_picture, name='delete'),
    path('trending/', user_views.trending, name='trending'),
    path('search/', user_views.search, name='search'),
    path('peer_profile/<int:pk>/', user_views.peer_profile, name='peer_profile'),
    path('follow/', user_views.follow_user, name='follow_user'),
    path('like/', user_views.like_picture, name='like_picture')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)