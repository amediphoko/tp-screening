from django.contrib import admin
from tp_screening.models import participant_screening


@admin.register(participant_screening.ParticipantScreening)
class ParticipantScreeningAdmin(admin.ModelAdmin):

    radio_fields = {
        'gender': admin.VERTICAL,
        'guardian': admin.HORIZONTAL,
        'citizenship': admin.HORIZONTAL,
        'married_to_citizen': admin.HORIZONTAL,
        'marriage_proof': admin.HORIZONTAL,
        'literacy': admin.HORIZONTAL,
        'has_witness_available': admin.HORIZONTAL,
        'marital_status': admin.HORIZONTAL,
        'living_arr': admin.HORIZONTAL,
        'employment_status': admin.HORIZONTAL,
        'work_type': admin.HORIZONTAL,
        'income_earnings': admin.HORIZONTAL,
        'community_activity': admin.HORIZONTAL,
        'voted': admin.HORIZONTAL
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
        ('Demographics Questions', {
            'fields': ('marital_status',
                       'living_arr')
        }),
    )
