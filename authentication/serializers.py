from rest_framework import serializers
from rest_framework.authtoken.models import Token

from authentication.models import Student, Teacher, CustomUser


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class StudentRegisterSerializer(serializers.ModelSerializer):
    "Serializer to register a student."

    class Meta:
        model = Student
        fields = "__all__"

    def create(self, validated_data):
        name = validated_data["name"]
        email = validated_data["email"]
        password = validated_data["password"]
        try:
            user = CustomUser.objects.create_user(
                email=email, password=password, name=name
            )
        except Exception as e:
            raise serializers.ValidationError(e)

        validated_data.pop("password")
        validated_data["user_model"] = user

        student_instance = Student.objects.create(**validated_data)
        token = Token.objects.get_or_create(user=user)

        serialized_data = StudentSerializer(student_instance)
        return {"token": token.key, "student": serialized_data.data}


class TeacherRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

    def create(self, validated_data):
        name = validated_data["name"]
        email = validated_data["email"]
        password = validated_data["password"]
        try:
            user = CustomUser.objects.create_user(
                email=email, password=password, name=name
            )
        except Exception as e:
            raise serializers.ValidationError(e)
        validated_data.pop("password")
        validated_data["user_model"] = user
        teacher = Teacher.objects.create(**validated_data)
        serialized_data = TeacherSerializer(teacher)
        token = Token.objects.get_or_create(user)

        return {"token": token.key, "teacher": serialized_data}
