from rest_framework.decorators import api_view, permission_classes
from rest_framework.schemas.coreapi import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from lms.models import Class, Assignment, Question
from lms.serializers import ClassSerializer, AssignmentSerializer, QuestionSerializer
from authentication.models import Teacher

# Create your views here.


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def classes_view(request):

    if request.method == "GET":
        classes = Class.objects.all()
        serialized_data = ClassSerializer(classes, many=True)
        return Response(data=serialized_data, status=status.HTTP_200_OK)

    if request.method == "POST":
        try:
            user = request.user
            teacher = Teacher.objects.get(user_model=user)
        except Teacher.DoesNotExist or ValueError:
            return Response(
                data={"message": "You are not authorized to add class"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serialized_data = ClassSerializer(request.data)
        if serialized_data.is_valid:
            serialized_data.save()
            return Response(data=serialized_data, status=status.HTTP_201_CREATED)

        return Response(
            data=serialized_data.errrors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([AllowAny])
def class_view(request, class_id):
    try:
        class_ = Class.objects.get(id=class_id)
    except Class.DoesNotExist:
        return Response(
            data={"message": "Class does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serialized_data = ClassSerializer(class_)
        return Response(data=serialized_data, status=status.HTTP_200_OK)
    else:
        try:
            user = request.user
            teacher = Teacher.objects.get(user_model=user)
        except Teacher.DoesNotExist or ValueError:
            return Response(
                data={"message": "You are not authorized to add class"},
                status=status.HTTP_404_NOT_FOUND,
            )
        if request.method == "PUT":
            serialized_data = ClassSerializer(instance=class_, data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(data=serialized_data, status=status.HTTP_200_OK)
            return Response(
                data=serialized_data.errors, status=status.HTTP_400_BAD_REQUEST
            )

        if request.method == "DELETE":
            class_.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def assignments_view(request):

    if request.method == "GET":
        assignments = Assignment.objects.all()
        serialized_data = AssignmentSerializer(assignments, many=True)
        return Response(data=serialized_data, status=status.HTTP_200_OK)
    if request.method == "POST":
        try:
            user = request.user
            teacher = Teacher.objects.get(user_model=user)
            request.data["teacher"] = teacher
        except Teacher.DoesNotExist or ValueError:
            return Response(
                data={"message": "You are not authorized to add class"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer_data = AssignmentSerializer(request.data)
        if serializer_data.is_valid:
            serializer_data.save()
            return Response(data=serializer_data, status=status.HTTP_201_CREATED)
        return Response(
            data=serializer_data.errrors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([AllowAny])
def assignment_view(request, pk):
    try:
        assignment = Assignment.objects.get(id=pk)
    except Assignment.DoesNotExist:
        return Response(
            data={"message": "Assignment does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        serialized_data = AssignmentSerializer(assignment)
        return Response(data=serialized_data, status=status.HTTP_200_OK)
    else:
        try:
            user = request.user
            teacher = Teacher.objects.get(user_model=user)
        except Teacher.DoesNotExist or ValueError:
            return Response(
                data={"message": "You are not authorized to add class"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if request.method == "PUT":
            serialized_data = AssignmentSerializer(
                instance=assignment, data=request.data
            )
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(data=serialized_data, status=status.HTTP_200_OK)
            return Response(
                data=serialized_data.errors, status=status.HTTP_400_BAD_REQUEST
            )
        if request.method == "DELETE":
            assignment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def question_view(request):
    if request.method == "GET":
        questions = Question.objects.all()
        serialized_data = QuestionSerializer(questions, many=True)
        return Response(data=serialized_data, status=status.HTTP_200_OK)
    if request.method == "POST":

        try:
            user = request.user
            teacher = Teacher.objects.get(user_model=user)
        except Teacher.DoesNotExist or ValueError:
            return Response(
                data={"message": "You are not authorized to add class"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serialized_data = QuestionSerializer(request.data)
        if serialized_data.is_valid:
            serialized_data.save()
            return Response(data=serialized_data, status=status.HTTP_201_CREATED)
        return Response(
            data=serialized_data.errrors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([AllowAny])
def question_view(request, pk):
    try:
        question = Question.objects.get(id=pk)
    except Question.DoesNotExist:
        return Response(
            data={"message": "Question does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        serialized_data = QuestionSerializer(question)
        return Response(data=serialized_data, status=status.HTTP_200_OK)

    else:
        try:
            user = request.user
            teacher = Teacher.objects.get(user_model=user)
        except Teacher.DoesNotExist or ValueError:
            return Response(
                data={"message": "You are not authorized to add class"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if request.method == "PUT":
            serialized_data = QuestionSerializer(instance=question, data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(data=serialized_data, status=status.HTTP_200_OK)
            return Response(
                data=serialized_data.errors, status=status.HTTP_400_BAD_REQUEST
            )
        if request.method == "DELETE":
            question.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
