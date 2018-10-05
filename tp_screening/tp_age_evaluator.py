from edc_reportable import AgeEvaluator, ValueBoundryError
from django.utils.timezone import localtime
from edc_base.utils import get_utcnow
from dateutil.relativedelta import relativedelta


class TpAgeEvaluator(AgeEvaluator):

    def __init__(self, **kwargs):
        self.reasons_ineligible = None
        super().__init__(**kwargs)

    def eligible(self, age=None):
        self.reasons_ineligible = None
        eligible = False
        if age:
            try:
                self.in_bounds_or_raise(age=age)
            except ValueBoundryError:
                self.reasons_ineligible = 'under 18 years old'
            else:
                eligible = True
        return eligible

    def in_bounds_or_raise(self, age=None):
        self.reasons_ineligible = None
        dob = localtime(get_utcnow() - relativedelta(years=age)).date()
        report_date = localtime(get_utcnow())
        age_units = 'years'
        return super().in_bounds_or_raise(
            dob=dob, report_datetime=report_date, age_units=age_units)


age_evaluator = TpAgeEvaluator(
    age_lower=18,
    age_lower_inclusive=True
    )
