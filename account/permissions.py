from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, BasePermission


class IsAuthenticated_(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_active
        )
