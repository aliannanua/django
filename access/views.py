from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from access.models import Permission
class PermissionListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'admin':
            return Response({"detail": "Forbidden"}, status=403)

        permissions = Permission.objects.all()

        data = []
        for p in permissions:
            data.append({
                "role": p.role.name,
                "resource": p.resource.name,
                "action": p.action.name
            })

        return Response(data)
