from django import forms
from edc_form_validators import FormValidatorMixin
from ..models import ParticipantScreening
from ..form_validators import ParticipantScreeningFormValidator


class ParticipantScreeningForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = ParticipantScreeningFormValidator

    class Meta:
        model = ParticipantScreening
        fields = '__all__'
