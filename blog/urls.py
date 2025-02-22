from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', views.post_detail, name='blog-post-detail'),
    path('author/<int:author_id>/', views.author_posts, name='blog-author-posts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
