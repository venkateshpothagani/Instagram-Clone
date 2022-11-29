from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from instagramcloneapi import views
from django.conf import settings
from django.conf.urls.static import static

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'posts', views.PostList, basename='Post')
# router.register('posts/<int:pk>/', views.PostDetail, basename='Post')
# router.register('register', views.APIView, basename='register')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("instagramcloneapi.urls")),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)