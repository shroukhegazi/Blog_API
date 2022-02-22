from django.db.models.query_utils import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from rest_framework.response import Response
from .models import Post
from rest_framework import generics, permissions
from .serializers import PostSerializer
from posts import serializers
from rest_framework.views import APIView


def courses(request):
    return HttpResponse("<h1>THIS IS MY HOME PAGE</h1>")

def home(request):
    post = Post.objects.aLL()
    return render(request, 'home.html',{'post': post} )

class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return
    qposts = Post.objects.all()
    serializer_class = PostSerializer



class PostDetail(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExists:
            raise Http404
    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = PostSerializer(guest)
        return Response(serializer.data)
#class PostDetail(generics.RetrieveUpdateAPIView):
    #def get_queryset(self):
        #return
    #qpost = Post.objects.all()
    #serializers_class1=  PostSerializer    