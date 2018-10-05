from ..eligibility import Eligibility
from edc_constants.constants import (YES, NO)

class TestEligibilty:
    
    def setUp(self):   
        self.eligibility_criteria = {
            'age' : 30,
            'citizenship' : NO,
            'legally_married' : True,
            'has_proof' : True,
            'literacy' : YES,
            'has_witness' : False,}
    
    def test_participant_age_minor(self):
        criteria = self.eligibility_criteria.copy()
        criteria.update({'age' : 15})
        eligibility_obj = Eligibility(**criteria)
        self.assertFalse(eligibility_obj.eligible)
    
    def test_participant_age_valid(self):
        criteria = self.eligibility_criteria.copy()
        criteria.update({'age' : 18})
        eligibility_obj = Eligibility(**criteria)
        self.assertTrue(eligibility_obj.eligible)
        self.assertIsNone(eligibility_obj.reasons_ineligible)
    
    def test_participant_below_age_reason(self):
        criteria = self.eligibility_criteria.copy()
        criteria.update({'age' : 15})
        eligibility_obj = Eligibility(**criteria)
        self.assertIn('under 18 years old',
                      eligibility_obj.reasons_ineligible)
    
    def test_participant_eligible_if_citizen(self):
        criteria = self.eligibility_criteria.copy()
        criteria.update({'citizenship': YES})
        eligibility_obj = Eligibility(**criteria)
        self.assertTrue(eligibility_obj.eligible)
        self.assertIsNone(eligibility_obj.reasons_ineligible)
    
    def test_not_eligible_if_not_citizen(self):
        criteria = self.eligibility_criteria.copy()
        criteria.update({'citizenship': NO, 'legally_married': False,
                         'has_proof': False})
        eligibility_obj = Eligibility(**criteria)
        self.assertFalse(eligibility_obj.eligible)
    
    def test_eligible_if_citizen_by_marriage(self):
        criteria = self.eligibility_criteria.copy()
        criteria.update({'citizenship': NO, 'legally_married': True,
                         'has_proof': True})
        eligibility_obj = Eligibility(**criteria)
        self.assertTrue(eligibility_obj.eligible)

    def test_not_citizen_reason(self):
        criteria = self.eligibility_criteria.copy()
        criteria.update({'citizenship': NO, 'legally_married': False,
                         'has_proof': False})
        eligibility_obj = Eligibility(**criteria)
        self.assertIn('Not a citizen of Botswana',
                      eligibility_obj.reasons_ineligible)

    def test_citizen_by_marriage_not_proof_reason(self):
        criteria = self.eligibility_criteria.copy()
        criteria.update({'citizenship': NO, 'legally_married': True,
                         'has_proof': False})
        eligibility_obj = Eligibility(**criteria)
        self.assertFalse(eligibility_obj.eligible)
        self.assertIn('Proof of marriage not provided',
                      eligibility_obj.reasons_ineligible)
        
    def test_participant_literacy(self):
        criteria = self.eligibility_criteria.copy()
        eligibility_obj = Eligibility(**criteria)
        self.assertTrue(eligibility_obj.eligible)
    
    def test_not_eligible_if_illiterate(self):
        criteria = self.eligibility_criteria.copy()
        criteria.update({'literacy': NO})
        eligibility_obj = Eligibility(**criteria)
        self.assertFalse(eligibility_obj.eligible)
        self.assertIn(
            'no witness available',
            eligibility_obj.reasons_ineligible.get('literacy'))
    
    def test_eligibile_illiterate_with_witness(self):
        criteria = self.eligibility_criteria.copy()
        criteria.update({'literacy' : NO, 'has_witness' : True})
        eligibility_obj = Eligibility(**criteria)
        self.assertTrue(eligibility_obj.eligible)
