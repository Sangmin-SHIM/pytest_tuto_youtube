import pytest

from django.contrib.auth.models import User

from pytest_factoryboy import register
from tests.factories import UserFactory, ProductFactory, CategoryFactory

######################################################################
################################# Fixture ############################
######################################################################
"""
# test_ex4.py / test_set_check_password1 , test_set_check_password2
@pytest.fixture()
def user(db):
    print("create-user")
    return User.objects.create_user("test-user1")

# test_ex4.py / test_new_user1, test_new_user2 
@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username : str,
        password : str = None,
        first_name : str = "firstname",
        last_name : str = "lastname",
        email : str = "test@test.com",
        is_staff : str = False,
        is_superuser : str = False,
        is_active : str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name = first_name,
            last_name = last_name,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = is_active,
        )

        return user
    return create_app_user 

@pytest.fixture
def new_staff_user(db, new_user_factory):
    return new_user_factory("Test_staff_user","password", is_staff="True")

@pytest.fixture
def new_user(db, new_user_factory):
    return new_user_factory("Test_user","password")    
"""
######################################################################
##############################/ Fixture ##############################
######################################################################    

######################################################################
################################# Factory ############################
######################################################################

register(UserFactory)
register(CategoryFactory)
register(ProductFactory)


######################################################################
##############################/ Factory ##############################
######################################################################    