from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    full_name = make_full_name("Daniel", "Amaral")
    assert full_name == "Amaral; Daniel"

def test_extract_family_name():
    family_name = extract_family_name(full_name = "Amaral; Daniel")
    assert family_name == "Amaral"

def test_extract_given_name():
    first_name = extract_given_name(full_name = "Amaral; Daniel")
    assert first_name == "Daniel"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])



