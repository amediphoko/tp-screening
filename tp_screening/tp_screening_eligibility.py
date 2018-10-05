from edc_constants.constants import YES, NO
from .eligibility import Eligibility


def if_yes(value):
    return value == YES


def if_no(value):
    return value == NO


class TpScreeningEligibility:

    eligibility_cls = Eligibility

    def __init__(self, model_obj=None):

        eligibility_obj = self.eligibility_cls(
            age=model_obj.age_in_years,
            citizenship=model_obj.citizenship,
            legally_married=if_yes(model_obj.married_to_citizen),
            has_proof=if_yes(model_obj.marriage_proof),
            literacy=model_obj.literacy,
            has_witness=if_yes(model_obj.has_witness_available),)

        self.eligible = eligibility_obj.eligible
        self.reasons_ineligible = eligibility_obj.reasons_ineligible
