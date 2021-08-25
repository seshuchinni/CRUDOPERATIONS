from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import * 
from .models import *
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin


class BooksListGeneric(GenericAPIView,ListModelMixin):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer
    def get(self,request):
        return self.list(request)
    
class BooksListCreate(GenericAPIView,CreateModelMixin):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer
    def post(self,request):
        return self.create(request)

class BooksListRetrive(GenericAPIView,RetrieveModelMixin,):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    
class BooksListUpdate(GenericAPIView,UpdateModelMixin,):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    
class BooksListDel(GenericAPIView,DestroyModelMixin,):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)


#Read
@api_view(['GET'])
def Booklist(request):
    booksobj = BooksModel.objects.all()
    serializer = BookSerializer(booksobj,many = True)
    return Response(serializer.data)

#create
@api_view(['POST'])
def post_Book(request):
    booksobj = BooksModel.objects.all()
    serializer = BookSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update
@api_view(['POST'])
def update_Book(request,id):
    booksobj = BooksModel.objects.get(id=id)
    serializer = BookSerializer(instance = booksobj,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
#Delete
@api_view(['DELETE'])
def delete_Book(request,id):
    booksobj = BooksModel.objects.get(id=id)
    booksobj.delete()
    return Response("Book is deleted...")


