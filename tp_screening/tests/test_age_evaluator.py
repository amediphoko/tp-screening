from ..tp_age_evaluator import age_evaluator
from django.test import TestCase

class TestAgeEvaluator(TestCase):
    
    def test_eligibility_of_age(self):
        self.assertFalse(age_evaluator.eligible(13))
        self.assertTrue(age_evaluator.eligible(18))
        self.assertTrue(age_evaluator.eligible(30))
    
    def test_ineligibilty_age_reasons_invalid(self):
        age_evaluator.eligible(17)
        self.assertIn(age_evaluator.reasons_ineligible, 'under 18 years old')
        age_evaluator.eligible(18)
        self.assertIsNone(age_evaluator.reasons_ineligible)