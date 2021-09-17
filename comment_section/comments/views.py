from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.

class CommentList(APIView):
    def get(self, request, videoId):
        comments = Comment.objects.filter(video_id=videoId)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class PostCommment(APIView):
    def post(self,request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LikeComment(APIView):
    def get_id(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comments = self.get_id(pk)
        comments.like += 1
        comments.save()
        serializer = CommentSerializer(comments)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DislikeComment(APIView):
    def get_id(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comments = self.get_id(pk)
        comments.dislike += 1
        comments.save()
        serializer = CommentSerializer(comments)
        return Response(serializer.data, status=status.HTTP_200_OK)