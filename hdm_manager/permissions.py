from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
    
    def has_permission(self, request, view):
       
        return request.user.is_authenticated and request.user.is_superuser 


class IsAdminOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            
            return request.user.is_authenticated and request.user.is_superuser
        
        
        return request.user.is_authenticated