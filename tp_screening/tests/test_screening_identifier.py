from django.test import TestCase
from ..identifiers import ScreeningIdentifier
from model_mommy import mommy


class TestScreeningIdentifier(TestCase):
    def test_indentifier(self):
        identifier = ScreeningIdentifier()
        self.assertTrue(identifier.identifier)
        self.assertTrue(identifier.identifier.startswith('S'))

    def test_model_generates_identifier(self):
        model_obj = mommy.make_recipe('tp_screening.participantscreening')
        self.assertIsNotNone(model_obj.screening_identifier)
        self.assertTrue(model_obj.screening_identifier.startswith('S'))
