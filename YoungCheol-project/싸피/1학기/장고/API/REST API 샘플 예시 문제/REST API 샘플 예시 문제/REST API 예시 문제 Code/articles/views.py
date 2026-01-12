from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Article
from .serializers import (
    ArticleSerializer,
    ArticleListSerializer
)


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleListSerializer(article, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if serializer.is_valid(raise_excption = True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data = request.data)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        data ={ 'msg': f'{article_pk}번 파일 삭제'}
        return Response(data, status=status.HTTP_204_CONTENT)