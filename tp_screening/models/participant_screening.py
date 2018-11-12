from django.db import models
from uuid import uuid4
import re
from ..identifiers import ScreeningIdentifier
from ..tp_screening_eligibility import TpScreeningEligibility
from edc_constants.choices import GENDER, YES_NO
from edc_constants.constants import UUID_PATTERN
from edc_base.model_managers import HistoricalRecords
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.sites import CurrentSiteManager
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_search.model_mixins import SearchSlugManager, SearchSlugModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin


class SubjectScreeningManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(screening_identifier=screening_identifier)


class SubjectIdentifierModelMixin(NonUniqueSubjectIdentifierModelMixin,
                                  SearchSlugModelMixin, models.Model):

    def update_subject_identifier_on_save(self):
        """Overridden to not set the subject identifier on save.
        """
        if not self.subject_identifier:
            self.subject_identifier = self.subject_identifier_as_pk.hex
        elif re.match(UUID_PATTERN, self.subject_identifier):
            pass
        return self.subject_identifier

    def make_new_identifier(self):
        return self.subject_identifier_as_pk.hex

    class Meta:
        abstract = True


class ParticipantScreening(SiteModelMixin, BaseUuidModel):

    eligibility_cls = TpScreeningEligibility

    screening_identifier_cls = ScreeningIdentifier

    '''temp subjectIdentifier'''
    reference = models.UUIDField(
        verbose_name='Reference',
        unique=True,
        default=uuid4,
        editable=False)

    '''screening identifier is assigned to the screening_identifier_cls instance
        when saving the model data to the database'''
    screening_identifier = models.CharField(
        verbose_name='Screening Identifier',
        max_length=50,
        unique=True,
        blank=True,
        editable=False)

    '''Subject Eligibility Questionnaire'''
    age_in_years = models.IntegerField(
        verbose_name="Age in years.",
        blank=True,
        null=True)

    guardian = models.CharField(
        verbose_name='Does subject have a guardian available?, If minor',
        max_length=3,
        choices=YES_NO,
        default=False,
        blank=True,
        null=True)

    gender = models.CharField(
        max_length=1,
        choices=GENDER)

    citizenship = models.CharField(
        verbose_name="Is subject a citizen of botswana?",
        max_length=3,
        choices=YES_NO,
        blank=True,
        null=True)

    married_to_citizen = models.CharField(
        verbose_name="If not citizen, are they legally"
                     " married to a motswana?",
        max_length=3,
        choices=YES_NO,
        blank=True,
        null=True)

    marriage_proof = models.CharField(
        verbose_name="has subject provided proof of marriage?"
                     " Marriage certificate.",
        max_length=3,
        choices=YES_NO,
        blank=True,
        null=True)

    literacy = models.CharField(
        verbose_name="Is subject literate?",
        max_length=3,
        choices=YES_NO,
        blank=True,
        null=True)

    has_witness_available = models.CharField(
        verbose_name="Does the subject have a literate witness"
                     " available with them ?",
        max_length=3,
        choices=YES_NO,
        blank=True,
        null=True)

    eligible = models.BooleanField(
        default=False,
        editable=False)

    reasons_ineligible = models.TextField(
        verbose_name='Reason not eligible',
        max_length=150,
        null=True,
        editable=False)

    consented = models.BooleanField(
        default=False,
        editable=False)

    on_site = CurrentSiteManager()

    objects = SubjectScreeningManager()

    history = HistoricalRecords()

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
