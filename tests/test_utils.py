import pytest

from uk_postcode.utils import validate, format_postcode


@pytest.mark.parametrize('expected, postcode', [
    (True, 'EC1A 1BB'), (True, 'W1A 0AX'),
    (True, 'M1 1AE'),   (True, 'B33 8TH'),
    (True, 'CR26XH'),  (True, 'DN551PT'),
    (True, 'WC1A0AX'),  (True, 'M11AE'),
])
def test_true_for_valid_postcodes(expected, postcode):
    assert expected == validate(postcode)


@pytest.mark.parametrize('expected, postcode', [
    (False, 'AB1E'), # Invalid length
    (False, 'AB110ABB'), # Invalid length
    (False, 'AB5 1PT'), # Invalid for single digits
    (False, 'BR51 1PT'),  # Invalid for double digits
    (False, 'WC0 1PT'), # Invalid for digit zero
    (False, 'NW11 0AX'),  # Invalid for London single-digits
    (False, 'QJ1A 0AX'),  # Invalid letter for first position
    (False, 'WJ1A 0AX'),  # Invalid letter for second position
    (False, 'M1Z 0AX'),  # Invalid letter for third position
    (False, 'BA1C 0AX'),  # Invalid letter for fourth position
    (False, 'WC1A 0AC'),  # Invalid letter for fourth position
])
def test_validate_for_false_postcodes(expected, postcode):
    assert expected == validate(postcode)


def test_true_for_format_postcode():
    postcode = 'WC1A0AX'
    assert 'WC1A 0AX' == format_postcode(postcode)


def test_raise_exception_for_invalid_postcode():
    postcode = 'WC1A 0AC'
    with pytest.raises(ValueError) as e_info:
        format_postcode(postcode)
    assert 'You need to pass a valid postcode' == str(e_info.value)
