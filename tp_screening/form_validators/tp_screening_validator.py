from edc_form_validators import FormValidator
from edc_constants.constants import NO, YES


class TpScreeningFormValidator(FormValidator):
    
    def clean(self):
        self.required_if(
            NO,
            field='citizenship',
            field_required='married_to_citizen',
            required_msg='If not a citizen of Botswana, Are they married to'
                         ' to a citizen?')
        
        self.required_if(
            YES,
            field='married_to_citizen',
            field_required='marriage_proof',
            required_msg='If participant is married to a citizen, is there'
                         ' proof of marriage?(Marriage Certificate).')
        
        self.required_if(
            NO,
            field='literacy',
            field_required='has_witness_available',
            required_msg='If participant is illiterate, do they have a'
                         ' witness available?')
        
        condition = self.cleaned_data.get('age_in_years') < 18
        self.required_if_true(
            condition=condition,
            field_required='guardian',
            required_msg='If the participant is a minor, do they have a'
                         ' guardian with them to give consent?')