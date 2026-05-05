from django.contrib import admin
from django.urls import path
from users.views import RegisterView, ProfileView, AdminOnlyView
from rest_framework_simplejwt.views import TokenObtainPairView
from access.views import PermissionListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('admin-only/', AdminOnlyView.as_view()),
    path('permissions/', PermissionListView.as_view()),
]