from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostDelete, PostUpdate, Subscribe

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('add/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('subscribe/', Subscribe.as_view(), name='subscribe'),
]
