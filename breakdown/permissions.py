from rest_framework import permissions

from rest_framework.permissions import BasePermission, DjangoModelPermissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the ticket.
        return obj.create_user.username == request.user.username

 
 
# class ModelPermission(BasePermission):
#     """ Access granted for requests with API key in header,
#     or made by user with appropriate Django model permissions. """
#     def has_permission(self, request, view):
#         return DjangoModelPermissions().has_permission(request, view)