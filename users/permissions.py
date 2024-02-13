from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerProfileOrReadOnly(BasePermission):  # Если запрос изменяет объект (например, POST, PUT, DELETE),
    # то проверяется, является ли пользователь владельцем этого объекта
    # (в данном случае, профиля пользователя)
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user
