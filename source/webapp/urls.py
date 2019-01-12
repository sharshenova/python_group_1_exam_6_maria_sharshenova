from django.urls import path
from webapp.views import welcome_view, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

from django.conf.urls.static import static
from django.conf import settings


app_name = 'webapp'

urlpatterns = [
    path('', welcome_view, name='welcome'),
    path('posts', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('posts/create', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
