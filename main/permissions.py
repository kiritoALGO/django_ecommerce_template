from rest_framework import permissions


class IsAuthorOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow authors and admins to edit an object.
    """

    def has_object_permission(self, request, view, obj):
        """Write permissions are only allowed 
        to the author of the object or admin users."""
        return obj.user == request.user or request.user.is_staff
