from edc_constants.constants import FEMALE, YES, NO
from faker import Faker
from model_mommy.recipe import Recipe

from .models import ParticipantScreening

fake = Faker()

participantscreening = Recipe(
    ParticipantScreening,
    age_in_years=20,
    gender=FEMALE,
    citizenship=NO,
    married_to_citizen=YES,
    marriage_proof=YES,
    literacy=YES,)
