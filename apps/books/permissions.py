# books/permissions.py
from rest_framework import permissions

class IsNotBlocked(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return True
        return not getattr(user, 'is_blocked', False)
