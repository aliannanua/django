from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Пользователь создан"}, status=201)

        return Response(serializer.errors, status=400)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "email": request.user.email,
            "message": "Ты авторизован"
        })


class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not has_permission(request.user, 'reports', 'read'):
            return Response({"detail": "Forbidden"}, status=403)

        return Response({"message": "Доступ разрешен"})