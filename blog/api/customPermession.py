from rest_framework.permissions import BasePermission 
class IsAuthor(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the request user is the author of the post
        return obj.author == request.user