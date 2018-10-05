from .citizenship_evaluator import CitizenshipEvaluator
from .tp_age_evaluator import age_evaluator
from .literacy_evaluator import LiteracyEvaluator

class EligibilityError(Exception):
    pass

class Eligibility:
    '''Eligible if all criteria evaluate to True'''

    age_evaluator = age_evaluator
    citizenship_evaluator_cls = CitizenshipEvaluator
    literacy_evaluator_cls = LiteracyEvaluator

    def __init__(self, age=None, citizenship=None, legally_married=None,
                 has_proof=None, literacy=None, has_witness=None):

        self.criteria = {}

        self.citizenship_evaluator = self.citizenship_evaluator_cls(
            citizenship=citizenship, legally_married=legally_married,
            has_proof=has_proof)

        self.literacy_evaluator = self.literacy_evaluator_cls(
            literacy=literacy, has_witness=has_witness)

        self.criteria.update(age=self.age_evaluator.eligible(age))
        self.criteria.update(citizenship=self.citizenship_evaluator.eligible)
        self.criteria.update(literacy=self.literacy_evaluator.eligible)

        self.eligible = all([v for v in self.criteria.values()])

        if self.eligible:
            self.reasons_ineligible = None
        else:
            self.reasons_ineligible = {
                k: v for k, v in self.criteria.items() if not v}

            if not self.age_evaluator.eligible(age):
                self.reasons_ineligible.update(age=self.age_evaluator.reasons_ineligible)

            if not self.citizenship_evaluator.eligible:
                self.reasons_ineligible.update(
                    citizenship=self.citizenship_evaluator.reasons_ineligible)

            if not self.literacy_evaluator.eligible:
                self.reasons_ineligible.update(literacy=self.literacy_evaluator.reasons_ineligible)

    def __str__(self):
        return self.eligible
