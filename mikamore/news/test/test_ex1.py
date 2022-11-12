import pytest
from factories import *
from news.models import *


@pytest.mark.django_db
def test_example():
    category = CategoryFactory()
    news = NewsFactory()
    news.category = category
    assert news.category.pk == category.pk
