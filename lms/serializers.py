from rest_framework import serializers, viewsets
from lms.models import Class, Assignment, Question


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
