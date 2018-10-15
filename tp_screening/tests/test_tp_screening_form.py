from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import (NO, YES)
from ..form_validators import TpScreeningFormValidator


class TestTpScreeningForm(TestCase):

    def test_botswana_citizen_no_married_required(self):
        cleaned_data = {
            'age_in_years': 18,
            'citizenship': NO,
            'married_to_citizen': None}
        form_validator = TpScreeningFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('married_to_citizen', form_validator._errors)

    def test_botswana_citizen_no_married_provided(self):
        cleaned_data = {
            'age_in_years': 18,
            'citizenship': NO,
            'married_to_citizen': YES,
            'marriage_proof': YES}
        form_validator = TpScreeningFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_married_to_citizen_yes_proof_required(self):
        cleaned_data = {
            'age_in_years': 18,
            'citizenship': NO,
            'married_to_citizen': YES,
            'marriage_proof': None}
        form_validator = TpScreeningFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('marriage_proof', form_validator._errors)

    def test_married_to_citizen_yes_proof_provided(self):
        cleaned_data = {
            'age_in_years': 18,
            'citizenship': NO,
            'married_to_citizen': YES,
            'marriage_proof': YES}
        form_validator = TpScreeningFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_botswana_citizen_yes_married_invalid(self):
        cleaned_data = {
            'age_in_years': 18,
            'citizenship': YES,
            'married_to_citizen': YES}
        form_validator = TpScreeningFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('married_to_citizen', form_validator._errors)

    def test_botswana_citizen_yes_married_valid(self):
        cleaned_data = {
            'age_in_years': 18,
            'citizenship': YES,
            'married_to_citizen': None}
        form_validator = TpScreeningFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_literacy_no_witness_required(self):
        cleaned_data = {
            'age_in_years': 18,
            'literacy': NO,
            'has_witness_available': None}
        form_validator = TpScreeningFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('has_witness_available', form_validator._errors)

    def test_literacy_no_witness_provided(self):
        cleaned_data = {
            'age_in_years': 18,
            'literacy': NO,
            'has_witness_available': YES}
        form_validator = TpScreeningFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_literacy_yes_witness_invalid(self):
        cleaned_data = {
            'age_in_years': 18,
            'literacy': YES,
            'has_witness_available': YES}
        form_validator = TpScreeningFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('has_witness_available', form_validator._errors)

    def test_literacy_yes_witness_valid(self):
        cleaned_data = {
            'age_in_years': 18,
            'literacy': YES,
            'has_witness_available': None}
        form_validator = TpScreeningFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_age_minor_guardian_required(self):
        cleaned_data = {
            'age_in_years': 15,
            'guardian': None}
        form_validator = TpScreeningFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('guardian', form_validator._errors)

    def test_age_minor_guardian_provided(self):
        cleaned_data = {
            'age_in_years': 15,
            'guardian': YES}
        form_validator = TpScreeningFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
