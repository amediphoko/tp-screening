from django.db import models
from ..choices import (LIVING_ARRANGEMENTS, MARITAL_STATUS_CHOICES,
                       WORK_TYPE_CHOICES, INCOME_SCALE, ACTIVITY_LEVEL)
from uuid import uuid4
from ..identifiers import ScreeningIdentifier
from ..tp_screening_eligibility import TpScreeningEligibility
from edc_constants.choices import (GENDER, YES_NO, YES_NO_NA_DWTA)


class ParticipantScreening(models.Model):

    eligibility_cls = TpScreeningEligibility

    screening_identifier_cls = ScreeningIdentifier

    '''temp subjectIdentifier'''
    reference = models.UUIDField(
        verbose_name = 'Reference',
        unique = True,
        default= uuid4,
        editable = False)

    '''screening identifier is assigned to the screening_identifier_cls instance
        when saving the model data to the database'''
    screening_identifier = models.CharField(
        verbose_name = 'Screening Identifier',
        max_length = 50,
        unique = True,
        blank = True,
        editable = False)

    '''Subject Eligibility Questionnaire'''
    age_in_years = models.IntegerField(
        verbose_name="Age in years.")
    
    gender = models.CharField(
        max_length=1,
        choices=GENDER)
    
    citizenship = models.CharField(
        verbose_name = "Is subject a citizen of botswana?",
        max_length=3,
        choices=YES_NO)
    
    married_to_citizen = models.CharField(
        verbose_name = "If not citizen, are they legally"
                        " married to a motswana?",
        max_length=3,
        choices=YES_NO)
    
    marriage_proof = models.CharField(
        verbose_name = "has subject provided proof of marriage?"
                        " Marriage certificate.",
        max_length=3,
        choices=YES_NO)
    
    literacy = models.CharField(
        verbose_name = "Is subject literate?",
        max_length=3,
        choices=YES_NO)
    
    has_witness_available = models.CharField(
        verbose_name = "Does the subject have a literate witness"
                        " available with them ?",
        max_length = 3,
        choices = YES_NO)
    
    eligible = models.BooleanField(
        default=False,
        editable=False)
    
    reasons_ineligible = models.TextField(
        verbose_name='Reason not eligible',
        max_length=150,
        null=True,
        editable=False)
    
    #Demographics Questionnaire
    
    marital_status = models.CharField(
        verbose_name = "What is the subject's marital"
                        " status?",
        max_length=8,
        choices=MARITAL_STATUS_CHOICES)
    
    living_arr = models.CharField(
        verbose_name = "Who does the subject currently live with?",
        max_length=30,
        choices=LIVING_ARRANGEMENTS)
    
    number_of_spouses_f = models.IntegerField(
        verbose_name="How many wives does the subject's husband have"
                        " (including traditional marriage), including the subject?",
        )
    
    number_of_spouses_m = models.IntegerField(
        verbose_name="How many wives does the subject have, including traditional"
                    " marriage?",) 
    
    #Education Questionnaire
    
    employment_status = models.CharField(
        verbose_name = "Is the subject currently employed?",
        max_length=3,
        choices=YES_NO)
    
    work_type = models.CharField(
        verbose_name = "What type of work does the subject do?",
        max_length=30,
        choices=WORK_TYPE_CHOICES)
    
    income_earnings = models.CharField(
        verbose_name = "In the past month, how much money did the subject"
                        " earn from the work they did or received in payment?",
        max_length=10,
        choices=INCOME_SCALE,
        )
    
    #Community Engagement Questionnaire
    
    community_activity = models.CharField(
        verbose_name = "How active is the subject in community activities"
                        " such as Motshelo, Syndicate, PTA, VDC, Mophato and"
                        " development of the community that surrounds the subject?",
        max_length=20,
        choices=ACTIVITY_LEVEL)
    
    voted = models.CharField(
        verbose_name = "Did the subject vote during the last local government election?",
        max_length=15,
        choices=YES_NO_NA_DWTA)
    
    def __str__(self):
        return f'{self.screening_identifier} {self.gender} {self.age_in_years}'
    
    def save(self, *args, **kwargs):
        eligibility_obj = self.eligibility_cls(model_obj=self)
        self.eligible = eligibility_obj.eligible
        if not self.eligible:
            reasons_ineligible = [
                v for v in eligibility_obj.reasons_ineligible.values() if v]
            reasons_ineligible.sort()
            self.reasons_ineligible = ','.join(reasons_ineligible)
        else:
            self.reasons_ineligible = None
        if not self.id:
            self.screening_identifier = self.screening_identifier_cls().identifier
        super().save(*args, **kwargs)
    
    