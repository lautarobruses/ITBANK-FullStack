from rest_framework import permissions
from sucursal.models import Empleado

class IsEmploye(permissions.BasePermission):
    def has_permission(self, request, view):
        
        try:
            empleado = Empleado.objects.get(user_id=request.user.id)
        except Empleado.DoesNotExist:
            return False
        
        return empleado.user == request.user