from django.contrib import admin
from .modeladmin_mixins import ModelAdminMixin
from ..admin_site import tp_screening_admin
from ..forms import ParticipantScreeningForm
from ..models import ParticipantScreening


@admin.register(ParticipantScreening, site=tp_screening_admin)
class ParticipantScreeningAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ParticipantScreeningForm

    radio_fields = {
        'gender': admin.VERTICAL,
        'guardian': admin.HORIZONTAL,
        'citizenship': admin.HORIZONTAL,
        'married_to_citizen': admin.HORIZONTAL,
        'marriage_proof': admin.HORIZONTAL,
        'literacy': admin.HORIZONTAL,
        'has_witness_available': admin.HORIZONTAL,
    }

    fieldsets = (
        ('Eligibility Criteria', {
            'fields': ('gender',
                       'age_in_years',
                       'guardian',
                       'citizenship',
                       'married_to_citizen',
                       'marriage_proof',
                       'literacy',
                       'has_witness_available',)
        }),
    )
