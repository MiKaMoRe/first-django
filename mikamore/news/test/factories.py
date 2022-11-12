from news.models import *
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    title = Faker("sentence", nb_words=3)


class NewsFactory(DjangoModelFactory):
    class Meta:
        model = News

    title = Faker("sentence", nb_words=5)
    content = Faker("paragraph", nb_sentences=20)
    category = SubFactory(CategoryFactory)
