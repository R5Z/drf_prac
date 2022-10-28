from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles import serializers

from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    # def post(self, request):
    # article = ArticleSerializer(data=request.data)
    # 1
    #   if not article.is_valid():
    #   return Reponse(article.errors)

    # 2
    #   article.is_valid(raise_exception=True) # 검증에 통하지 않으면 에러를 발생시키겠다는 의미
    #   article.save(author=request.user) # 게시글을 저장할 때 유저를 저장한다

    #   return Response(article.data)