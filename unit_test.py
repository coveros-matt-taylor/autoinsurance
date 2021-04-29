import pytest
from process import *

cases = [
    # claims, age, premium_increase, warning_letter_enum, is_policy_canceled, is_error
    (0, 15, -1, WarningLetterEnum.NONE, False, True),
    (0, 16, 50, WarningLetterEnum.NONE, False, False),
    (0, 17, 50, WarningLetterEnum.NONE, False, False),

    (0, 25, 50, WarningLetterEnum.NONE, False, False),
    (0, 26, 25, WarningLetterEnum.NONE, False, False),
    (0, 27, 25, WarningLetterEnum.NONE, False, False),

    (0, 84, 25, WarningLetterEnum.NONE, False, False),
    (0, 85, 25, WarningLetterEnum.NONE, False, False),
    (0, 86, -1, WarningLetterEnum.NONE, False, True),

    (1, 15, -1, WarningLetterEnum.NONE, False, True),
    (1, 16, 100, WarningLetterEnum.LTR1, False, False),
    (1, 17, 100, WarningLetterEnum.LTR1, False, False),

    (1, 25, 100, WarningLetterEnum.LTR1, False, False),
    (1, 26, 50, WarningLetterEnum.NONE, False, False),
    (1, 27, 50, WarningLetterEnum.NONE, False, False),

    (1, 84, 50, WarningLetterEnum.NONE, False, False),
    (1, 85, 50, WarningLetterEnum.NONE, False, False),
    (1, 86, -1, WarningLetterEnum.NONE, False, True),

    (2, 15, -1, WarningLetterEnum.NONE, False, True),
    (2, 16, 400, WarningLetterEnum.LTR2, False, False),
    (2, 17, 400, WarningLetterEnum.LTR2, False, False),

    (2, 25, 400, WarningLetterEnum.LTR2, False, False),
    (2, 26, 200, WarningLetterEnum.LTR3, False, False),
    (2, 27, 200, WarningLetterEnum.LTR3, False, False),

    (2, 84, 200, WarningLetterEnum.LTR3, False, False),
    (2, 85, 200, WarningLetterEnum.LTR3, False, False),
    (2, 86, -1, WarningLetterEnum.NONE, False, True),

    (4, 15, -1, WarningLetterEnum.NONE, False, True),
    (4, 16, 400, WarningLetterEnum.LTR2, False, False),
    (4, 17, 400, WarningLetterEnum.LTR2, False, False),

    (4, 25, 400, WarningLetterEnum.LTR2, False, False),
    (4, 26, 200, WarningLetterEnum.LTR3, False, False),
    (4, 27, 200, WarningLetterEnum.LTR3, False, False),

    (4, 84, 200, WarningLetterEnum.LTR3, False, False),
    (4, 85, 200, WarningLetterEnum.LTR3, False, False),
    (4, 86, -1, WarningLetterEnum.NONE, False, True),

    (5, 26, 0, WarningLetterEnum.NONE, True, False),
    (6, 26, 0, WarningLetterEnum.NONE, True, False),
    (5, 80, 0, WarningLetterEnum.NONE, True, False),

    (-1, 80, -1, WarningLetterEnum.NONE, False, True),
]
@pytest.mark.parametrize("data", cases)
def test_thing(data):
    result = process(data[0], data[1])
    expected = AutoInsuranceAction(data[2], data[3], data[4], data[5])
    assert(expected.premium_increase == result.premium_increase)
    assert(expected.warning_letter_enum == result.warning_letter_enum)
    assert(expected.is_policy_canceled == result.is_policy_canceled)
    assert(expected.is_error == result.is_error)