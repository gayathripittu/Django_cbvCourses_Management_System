from django.shortcuts import render
from courses_app.models import Course
from courses_app.serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class CourseList(APIView):
    def get(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Course_detail(APIView):
    def get_object(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,pk):
        Course_data=self.get_object(pk)
        serializer=CourseSerializer(Course_data)
        return Response(serializer.data)
    
    def put(self,request,pk):
        Course_data=self.get_object(pk)
        serializer=CourseSerializer(Course_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        Course_data=self.get_object(pk)
        Course_data.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)








