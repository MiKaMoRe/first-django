from django.utils.translation import get_language
from news.models import *
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory

Faker._DEFAULT_LOCALE = get_language()


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    title = Faker("sentence", nb_words=3)


class NewsFactory(DjangoModelFactory):
    class Meta:
        model = News

    title = Faker("sentence", nb_words=5)
    content = Faker("text", max_nb_chars=200)
    category = SubFactory(CategoryFactory)
