from apps.article.models import Article, Category, Tag


def data():
   categories = Category.objects.all().order_by('title')
   last_articles = Article.objects.all()
   tags = Tag.objects.all().order_by('title')

   return {
      "categories": categories,
      "last_articles": last_articles.order_by('-id')[:3],
      "tags": tags,
   }
