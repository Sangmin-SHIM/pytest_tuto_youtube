import pytest

from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_create1():
    User.objects.create_user('test','test@test.com','test')
    count = User.objects.all().count()
    print(count)
    assert  count == 1

@pytest.mark.django_db
def test_user_create2():
    count = User.objects.all().count()
    print(count)
    assert  count == 0