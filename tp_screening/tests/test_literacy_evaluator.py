from django.test import TestCase
from ..literacy_evaluator import LiteracyEvaluator
from edc_constants.constants import YES, NO

class TestLiteracyEvaluator(TestCase):
    
    def test_eligibility_on_literacy(self):
        literacy_eval = LiteracyEvaluator()
        self.assertFalse(literacy_eval.eligible)
        literacy_eval = LiteracyEvaluator(literacy=YES)
        self.assertTrue(literacy_eval.eligible)
        literacy_eval = LiteracyEvaluator(literacy=NO, has_witness=True)
        self.assertTrue(literacy_eval.eligible)
        literacy_eval = LiteracyEvaluator(literacy=NO)
        self.assertFalse(literacy_eval.eligible)
    
    def test_eligibility_invalid_reasons(self):
        literacy_eval = LiteracyEvaluator(literacy=YES)
        self.assertIsNone(literacy_eval.reasons_ineligible)
        literacy_eval = LiteracyEvaluator(literacy=NO, has_witness=False)
        self.assertIn('no witness available', literacy_eval.reasons_ineligible)