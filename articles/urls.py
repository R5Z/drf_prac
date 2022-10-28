from django.urls import path, include
from articles.views import ArticleView


urlpatterns = [ 
    path('', ArticleView.as_view(), name='article_view'),
]

