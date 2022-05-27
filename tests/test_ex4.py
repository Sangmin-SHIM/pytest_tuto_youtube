import pytest
from django.contrib.auth.models import User

"""
# (1) ---------------------------------------
@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test-user1")

@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True
"""

"""
# (2) ---------------------------------------
@pytest.fixture()
def user_2(db):
    user = User.objects.create_user("test-user2")
    return user
def test_set_check_password(user_2):
    assert user_2.username == "test-user2"
"""

"""
# (3) ---------------------------------------
def test_set_check_password1(user):
    print("check-user1")
    user.set_password("new-password")
    assert user.check_password("new-password") is True

def test_set_check_password2(user):
    print("check-user2")
    user.set_password("new-password")
    assert user.check_password("new-password") is True
"""

"""
# (4) ---------------------------------------
def test_new_staff_user(new_staff_user):
    print(new_staff_user.is_staff)
    assert new_staff_user.is_staff

def test_new_user(new_user):
    print(new_user.username)
    assert new_user.username == "Test_user"
"""

"""
# (5) ---------------------------------------
def test_factory_user(user_factory):
    user = user_factory.build()
    print(user.username)
    assert True

# (6) ---------------------------------------
@pytest.mark.django_db
def test_factory_user_db(user_factory):
    user = user_factory.create()
    count = User.objects.all().count()
    print('DB connected Count : ', count)
    print('User : ', user.username)
    assert True 
"""

# (7) ---------------------------------------
def test_product(db, product_factory):
    product = product_factory.create()
    print("Description : ",product.description)
    assert True