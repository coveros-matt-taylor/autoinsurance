from enum import Enum
class WarningLetterEnum(Enum):
    NONE = 'NONE'
    LTR1 = 'LTR1'
    LTR2 = 'LTR2'
    LTR3 = 'LTR3'

class AutoInsuranceAction():
    def __init__(self, premium_increase : int, warning_letter_enum : WarningLetterEnum, is_policy_canceled : bool, is_error : bool):
        self.premium_increase = premium_increase
        self.warning_letter_enum = warning_letter_enum
        self.is_policy_canceled = is_policy_canceled
        self.is_error = is_error

def process(claims, age):
    if claims == 0 and age >= 16 and age <=25:
        return AutoInsuranceAction(50, WarningLetterEnum.NONE, False, False)

    if claims == 0 and age >=26 and age <= 85:
        return AutoInsuranceAction(25, WarningLetterEnum.NONE, False, False)
    
    if claims == 1 and age >= 16 and age <= 25:
        return AutoInsuranceAction(100, WarningLetterEnum.LTR1, False, False)

    if claims == 1 and age  >= 26 and age <= 85:
        return AutoInsuranceAction(50, WarningLetterEnum.NONE, False, False)

    if (claims >= 2 and claims <= 4 and age >= 16 and age <= 25):
        return AutoInsuranceAction(400, WarningLetterEnum.LTR2, False, False)

    if (claims >= 2 and claims <= 4 and age >= 26 and age <= 85):
        return AutoInsuranceAction(200, WarningLetterEnum.LTR3, False, False)

    if (claims >= 5):
        return AutoInsuranceAction(0, WarningLetterEnum.NONE, True, False)

    return AutoInsuranceAction(-1, WarningLetterEnum.NONE, False, True)

print(process(0, 20))