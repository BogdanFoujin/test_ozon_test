import pytest
from src.baseclasses.response import Response
from src.schemas.user import User


def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    # print(make_number)

@pytest.mark.skip("[ISSUE-23414] Issue with network connection")
def test_another():
    assert 1 == 1


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
    assert calculate(first_value, second_value) == result


# a = [1, 4, 5]

# print(a.__sizeof__())
# print(sys.getsizeof(a))