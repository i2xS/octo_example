from verbose_octo_goggles.adapter.django_model import DjangoModelAdapter

from .models import Article, User, Category


class UserAdapter(DjangoModelAdapter):
    model = User


class CategoryAdapter(DjangoModelAdapter):
    model = Category


class ArticleAdapter(DjangoModelAdapter):
    model = Article
    fk_fields = {
        'creator': UserAdapter
    }
    m2m_fields = {
        'categories': CategoryAdapter
    }
