from django.urls import path
from .views import PostList, PostDetail, courses



urlpatterns = [
    path('', courses, name='home-page'),
    path('list/<int:pk>/', PostDetail.as_view()),
    path('list/', PostList.as_view())
]