from rest_framework import serializers
from articles.models import Article
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "content") # author에 대한 벨리데이션을 하지 않음

# 2
# class ArticleSerializer(serializers.ModelSerializer): # read_only로 두면 게시글 생성 시에 벨리데이션에 걸리지 않음
#    class Meta:
#        model = Article
#        fields = '__all__'
#
#        extra_kwargs = {
#            'author': {'read_only': True}
#        }
#     

# 3
# class ArticleSerializer(serializers.ModelSerializer):
#   author = serializers.SerializerMethodField()
#   def get_author(self, obj):
#       return obj.author.username
#    class Meta:
#        model = Article
#        fields = '__all__'
#
#        extra_kwargs = {
#            'author': {'read_only': True}
#        }
