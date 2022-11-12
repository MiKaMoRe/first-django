from news.models import *
from news.test.factories import *
import random


def SeedNews():
    categories = CategoryFactory.create_batch(5)

    for category in categories:
        NewsFactory.create_batch(random.randint(4, 30), category=category)

    print("News seeded")
