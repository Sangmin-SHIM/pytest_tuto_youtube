import pytest

from django.contrib.auth.models import User
"""
@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test-user1")

@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True
"""

"""
@pytest.fixture()
def user_2(db):
    user = User.objects.create_user("test-user2")
    return user
def test_set_check_password(user_2):
    assert user_2.username == "test-user2"
"""

@pytest.fixture(scope="session")
def user(db):
    print("create-user")
    return User.objects.create_user("test-user1")

def test_set_check_password1(user):
    print("check-user1")
    user.set_password("new-password")
    assert user.check_password("new-password") is True

def test_set_check_password2(user):
    print("check-user2")
    user.set_password("new-password")
    assert user.check_password("new-password") is True
