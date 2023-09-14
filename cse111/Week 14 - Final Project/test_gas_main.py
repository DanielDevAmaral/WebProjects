from pytest import approx
import pytest
from Gas_main import calculation as calc

#The only testeble fuction in my code.
def test_calculation():
    corola_cal = calc("Corola/2023", 100)
    assert corola_cal == approx(31.84,0.001)

    hyundai_cal = calc("HR10/2023", 100)
    assert hyundai_cal == approx(71.67,0.001)

    iveco_cal = calc("Iveco/2023", 100)
    assert iveco_cal == approx(81.65,0.001)

    jeep_cal = calc("Compass/2023", 100)
    assert jeep_cal == approx(62.62,0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
if __name__ == '__main__':
    pytest.main(["-v", "--tb=line", "-rN", __file__])
