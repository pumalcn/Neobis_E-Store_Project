from django.urls import path, include, re_path
from .views import UserInfoDetailView, UserInfoListCreateView


urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
    path(r'auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # b935a5b4b2f981c43f0ee53272647e892c7d8172
    path('info/<int:pk>/', UserInfoDetailView.as_view()),
    path('info/', UserInfoListCreateView.as_view()),
]
