from rest_framework.permissions import BasePermission, SAFE_METHODS


class ISOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(obj.visitor == request.user)
