# permissions.py
# Custom permissions for the fundraisers app

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True # Write permissions are only allowed to the owner of the fundraiser.
        return obj.owner == request.user


# Custom permission for Pledge supporter
