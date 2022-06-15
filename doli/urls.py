from django.contrib import admin
from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from doli_app import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('post', views.PostViewSet, basename='post')
router.register('comment', views.CommentViewSet, basename='comment')
router.register('profile', views.UserView, basename='profile')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('create-admin/', views.AdminUserView.as_view()),
    path('create/', views.UserCreateView.as_view()),
    path('', include(router.urls)),
    path('drf-login/', include('rest_framework.urls'))
]
