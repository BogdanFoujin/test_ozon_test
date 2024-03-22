import pytest
from src.baseclasses.response import Response
from src.schemas.user import User


def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    # print(make_number)

@pytest.mark.development
@pytest.mark.production
@pytest.mark.skip("[ISSUE-23414] Issue with network connection")
def test_another():
    """
    In that test we try to check that 1 equal 2
    """
    assert 1 == 2

@pytest.mark.development
@pytest.mark.parametrize(
        "first_value, second_value, result",
        [
            (1, 2, 3),
            (-1, -2, -3),
            (-1, 2, 1),
            ('b', -2, None),
            ('b', 'b', None),
        ]
)
def test_calculation(first_value, second_value, result, calculate):
    """
    In test we are testing calcularing with different values(Valid and Invalid)
    """
    assert calculate(first_value, second_value) == result



# -k development
# -k "not development"

# a = [1, 4, 5]

# print(a.__sizeof__())
# print(sys.getsizeof(a))
    
@pytest.mark.development
@pytest.mark.production
def test_another_failing_test():
    assert 1 == 2