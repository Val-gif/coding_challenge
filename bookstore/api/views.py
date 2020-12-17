from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from api.models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.response import Response

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookList(APIView):
    def get(self, request, format=None):
        try:
            author = request.query_params["author"]
            books = BookList.objects.filter(author=author)
        except:
            books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            book = self.get_object(pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, rquest, pk, format=None):
        serializer = BookSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            book = self.get_object(pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        return Response(serializer.data)