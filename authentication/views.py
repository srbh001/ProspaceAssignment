from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response


from authentication.models import CustomUser, Student, Teacher
from authentication.serializers import (
    StudentSerializer,
    TeacherSerializer,
    StudentRegisterSerializer,
    TeacherRegisterSerializer,
)


@api_view(["POST"])
@permission_classes([AllowAny])
def student_register(request):
    serializer = StudentRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def teacher_register(request):
    serializer = TeacherRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def login_get_token(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if email is None or password is None:
        return Response(
            {"error": "Please provide both email and password"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return Response(
            {"error": "Invalid email or password"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if not user.check_password(password):
        return Response(
            {"error": "Invalid email or password"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    token = user.auth_token.key
    return Response({"token": token}, status=status.HTTP_200_OK)
