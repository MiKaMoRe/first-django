from users.models import User


def seed_users():
    User.objects.create_superuser(
        username="admin", email="admin@gmail.com", password="simplepass"
    ).save()

    print('Superuser created')
