from verbose_octo_goggles.adapter.django_model import DjangoModelAdapter

from .models import Entry, User, Category


class UserAdapter(DjangoModelAdapter):
    model = User


class CategoryAdapter(DjangoModelAdapter):
    model = Category


class EntryAdapter(DjangoModelAdapter):
    model = Entry
    fk_fields = {
        'author': UserAdapter,
        'category': CategoryAdapter
    }
