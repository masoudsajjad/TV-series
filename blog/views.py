from django.shortcuts import render
from django.views.generic import TemplateView
from.models import *


class IndexPage(TemplateView):

    def get(self, request, **kwargs):
        article_data = []
        all_articles = Article.objects.all().order_by('-created_at')[:9]

        for article in all_articles:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category.title,
                'created_at': article.created_at.date(),
            })

        promote_article_data= []
        all_promote_article=Article.objects.filter(promote=True)
        for promote_article in all_promote_article:
            promote_article_data.append({
                'title': promote_article.title,
                'cover': promote_article.cover.url,
                'category': promote_article.category.title,
                'author': promote_article.author.user.first_name,
                'author_cover': promote_article.author.avatar.url,
                'created_at': promote_article.created_at.date()
            })

        context = {
            'article_data': article_data,
            'promote_article_data': promote_article_data,
        }

        return render(request,'index.html', context)


class ContactPage(TemplateView):
    template_name = "page-contact.html"