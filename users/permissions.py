from rest_framework import permissions


class PremiumPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_premium:
            return True
