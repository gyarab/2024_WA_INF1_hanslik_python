from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', views.post_detail, name='blog-post-detail'),
    path('author/<int:author_id>/', views.author_posts, name='blog-author-posts'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog-home'), name='logout'),
    path('register/', views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
