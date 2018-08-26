"""This module does validation and formatting for UK Postcodes"""

import re

# Regex used in validation.
# This regex can be found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
REGEX_VALIDATION = re.compile('^([A-Za-z][A-Ha-hJ-Yj-y]?[0-9][A-Za-z0-9]? ?[0-9][A-Za-z]{2}|[Gg][Ii][Rr] ?0[Aa]{2})$')

OUTWARD_AREA_SINGLE_DIGIT_DISTRICT = ['BR', 'FY', 'HA', 'HD', 'HG', 'HR',
                                      'HS', 'HX', 'JE', 'LD', 'SM', 'SR',
                                      'WN', 'ZE']
OUTWARD_AREA_DOUBLE_DIGIT_DISTRICT = ['AB', 'LL', 'SO']
OUTWARD_AREA_ZERO_DIGIT_DISTRICT = ['BL', 'CM', 'CR', 'FY', 'HA', 'PR',
                                    'SL', 'SS']

OUTWARD_AREA_CENTRAL_LONDON_AREA_SINGLE = ['W1', 'E1', 'N1', 'N1', 'EC',
                                           'SW', 'WC', 'WC', 'NW', 'SE']

LETTERS_NOT_USED_AS_FIRST_POSITION = ['Q', 'V', 'X']
LETTERS_NOT_USED_AS_SECOND_POSITION = ['I', 'J', 'Z']
LETTERS_NOT_USED_AS_FINAL_POSITION = ['C', 'I', 'K', 'M', 'O', 'V']

LETTERS_TO_APPEAR_AT_THIRD_POSITION = ['A', 'C', 'E', 'F', 'G', 'H', 'J', 'K',
                                       'P', 'S', 'T', 'U', 'W']  # For A9A
LETTERS_TO_APPEAR_AT_FOURTH_POSITION = ['A', 'B', 'E', 'H', 'M', 'N', 'P',
                                        'R', 'V', 'W', 'X', 'Y']  # for AA9A


def validate(postcode):
    """Function that validates a UK Postcode
     Args:
         postcode (string): The first parameter.

     Returns:
         bool: The return value. True for success, False otherwise.
     """

    # The postcode can be or not with a space between outward and inward code.
    # So we use replace function to remove it in any case.
    postcode = postcode.replace(' ', '').upper()

    # Validate against Regex
    if not REGEX_VALIDATION.match(postcode):
        return False

    # Get Outward and Inward codes
    outward, inward = postcode[:-3], postcode[-3:]

    if outward[1].isdigit():
        # A9A, A9 and A99 formats
        area, district = outward[0], outward[1:]
    else:
        # AA9A, AA9 and AA99 formats
        area, district = outward[:2], outward[2:]

    # Areas with only single-digit districts
    if area in OUTWARD_AREA_SINGLE_DIGIT_DISTRICT and len(district) > 1:
        return False

    # Areas with only double-digit districts
    if area in OUTWARD_AREA_DOUBLE_DIGIT_DISTRICT and len(district) < 2:
        return False

    # Areas with a district '0'
    if district == '0' and area not in OUTWARD_AREA_ZERO_DIGIT_DISTRICT:
        return False

    # London single-digit districts
    if area in OUTWARD_AREA_CENTRAL_LONDON_AREA_SINGLE:
        if not district[0].isdigit() or district[1].isdigit():
            return False

    # The letters QVX are not used in the first position.
    if area[0] in LETTERS_NOT_USED_AS_FIRST_POSITION:
        return False

    # The letters IJZ are not used in the second position.
    if len(area) > 1 and area[1] in LETTERS_NOT_USED_AS_SECOND_POSITION:
        return False

    # The only letters to appear in the third position are ABCDEFGHJKPSTUW
    # when the structure starts with A9A
    if (len(area) == 1 and len(district) == 2
        and not district[-1].isdigit()
            and district[-1] not in LETTERS_TO_APPEAR_AT_THIRD_POSITION):
        return False

    # The only letters to appear in the fourth position are
    # ABEHMNPRVWXY when the structure starts with AA9A.
    if (len(area) == 2 and not district[-1].isdigit()
            and district[-1] not in LETTERS_TO_APPEAR_AT_FOURTH_POSITION):
        return False

    # The final two letters do not use the letters CIKMOV,
    if (inward[-1] in LETTERS_NOT_USED_AS_FINAL_POSITION
            or inward[-1] in LETTERS_NOT_USED_AS_FINAL_POSITION):
        return False

    return True


def format_postcode(postcode):
    """Function that formats a UK Postcode
     Args:
         postcode (string): The first parameter.

     Returns:
         string: The Postcode formatted.
     """
    # Remove any space in the string, so we can format its properly.
    postcode = postcode.replace(' ', '')
    if not validate(postcode):
        raise ValueError('You need to pass a valid postcode')
    return "{} {}".format(postcode[:-3], postcode[-3:])
