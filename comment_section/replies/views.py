from django.shortcuts import render
from .models import Replies
from .serializers import ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps
from django.db.models import Q

# Create your views here.

class PostReply(APIView):
    def post(self,request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReplyList(APIView):
    def get(self, request, comment_id):
        comment_model = apps.get_model('comments.Comment')
        comment_object = comment_model.objects.get(pk=comment_id)
        replies = Replies.objects.filter(Q(comment_id=comment_id) & Q(video_id=comment_object.video_id))
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

