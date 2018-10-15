from django.test import TestCase
from model_mommy import mommy
from edc_constants.constants import (FEMALE, NO, YES, )


class TestParticipantScreening(TestCase):
    '''Test eligibility for the Participant Screening criteria and
    the overall model behavior'''

    def test_with_default_mommy_recipe(self):
        participant_screening = mommy.make_recipe(
            'tp_screening.participantscreening')
        self.assertTrue(participant_screening.eligible)
        self.assertTrue(participant_screening.gender, FEMALE)
        self.assertTrue(participant_screening.citizenship, NO)
        self.assertTrue(participant_screening.married_to_citizen, YES)
        self.assertTrue(participant_screening.marriage_proof, YES)
        self.assertTrue(participant_screening.literacy, YES)

    def test_partcipant_age_minor(self):
        participant_screening = mommy.prepare(
            'tp_screening.participantscreening', age_in_years=15)
        self.assertFalse(participant_screening.eligible)

    def test_participant_minor_ineligible_reason(self):
        participant_screening = mommy.make_recipe(
            'tp_screening.participantscreening', age_in_years=15)
        self.assertFalse(participant_screening.eligible)
        self.assertIn('under 18 years old',
                      participant_screening.reasons_ineligible)

    def test_participant_age_lower_bound_inclusion(self):
        participant_screening = mommy.make_recipe(
            'tp_screening.participantscreening', age_in_years=18)
        self.assertTrue(participant_screening.eligible)
        self.assertEqual(participant_screening.reasons_ineligible, None)
