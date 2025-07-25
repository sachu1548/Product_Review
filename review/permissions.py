from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsAuthenticatedAndOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
