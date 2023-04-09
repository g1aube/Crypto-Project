from django.urls import path
from backend import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', views.CustomUserList.as_view()),
    path('api/users/<int:pk>', views.CustomUserDetail.as_view()),
    path('api/post/', views.PostModel.as_view()),
    path('api/post/<int:id>', views.PostModel.as_view()),
    path('api/posts/', views.GetPostsModel.as_view())
]

# ivan 1234
