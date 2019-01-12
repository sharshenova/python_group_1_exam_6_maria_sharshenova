from django.urls import path
from webapp.views import welcome_view, post_view

from django.conf.urls.static import static
from django.conf import settings


app_name = 'webapp'

urlpatterns = [
    path('', welcome_view, name='welcome'),
    path('posts', post_view, name='post_list'),
    # path('posts', PostListView.as_view(), name='post_list'),
    # path('posts/<int:pk>', FoodDetailView.as_view(), name='post_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
