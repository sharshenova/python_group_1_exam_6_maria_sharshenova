from django.urls import path
from webapp.views import welcome_view, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, \
    UserListView, UserDetailView




app_name = 'webapp'

urlpatterns = [
    path('', welcome_view, name='welcome'),
    path('posts', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('posts/create', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('users', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user_detail'),
]


