from .view import ScarfView

from muffler.models import Article


class ArticleView(ScarfView):
    def begin(self, request):
        modarticle = Article.objects.all()
        articles = [
            (
                a.title,
                a.synopsis,
                a.author,
                a.created,
            )
            for a in modarticle
        ]
        self.context["articles"] = reversed(articles)
        return super().begin(request)
