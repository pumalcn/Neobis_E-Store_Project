from django.contrib.auth.models import User

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerProfileOrReadOnly
from product.models import UserInfo
from users.serializers import UserInfoSerializer, UserSerializer


class UserInfoListCreateView(ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):  # Подвязывает текущего авторизованного пользователя,
        # который создает объект UserInfo
        user = self.request.user
        serializer.save(user=user)


class UserInfoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerProfileOrReadOnly, ]