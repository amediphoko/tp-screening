from django import forms
from edc_form_validators import FormValidatorMixin
from ..models import ParticipantScreening
from ..form_validators import TpScreeningFormValidator


class TpScreeningForm(FormValidatorMixin, forms.ModelForm):
    
    form_validator_cls = TpScreeningFormValidator
    
    class Meta:
        model = ParticipantScreening
        fields = '__all__'