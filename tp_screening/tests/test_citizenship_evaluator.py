from django.test import TestCase
from edc_constants.constants import YES, NO
from ..citizenship_evaluator import CitizenshipEvaluator


class TestCitizenshipEvaluator(TestCase):

    def test_eligibility_citizenship(self):
        citizenship_eval = CitizenshipEvaluator()
        self.assertFalse(citizenship_eval.eligible)
        citizenship_eval = CitizenshipEvaluator(citizenship=YES)
        self.assertTrue(citizenship_eval.eligible)
        citizenship_eval = CitizenshipEvaluator(
            citizenship=NO, legally_married=False,)
        self.assertFalse(citizenship_eval.eligible)
        citizenship_eval = CitizenshipEvaluator(
            citizenship=NO, legally_married=True, has_proof=True)
        self.assertTrue(citizenship_eval.eligible)

    def test_eligibility_invalid_citizenship_reasons(self):
        citizenship_eval = CitizenshipEvaluator(citizenship=YES)
        self.assertIsNone(citizenship_eval.reasons_ineligible)
        citizenship_eval = CitizenshipEvaluator(
            citizenship=NO, legally_married=True, has_proof=False)
        self.assertIn('Proof of marriage not provided',
                      citizenship_eval.reasons_ineligible)
        citizenship_eval = CitizenshipEvaluator(
            citizenship=NO, legally_married=False)
        self.assertIn('Not a citizen of Botswana',
                      citizenship_eval.reasons_ineligible)
