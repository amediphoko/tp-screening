from edc_constants.constants import (YES, NO)

class LiteracyEvaluator:
    '''eligible evlautes to True if the subject is literate or has
    a literate witness available'''

    def __init__(self, literacy=None, has_witness=None):
        self.eligible = False
        self.reasons_ineligible = None
        if literacy == YES:
            self.eligible = True
        elif literacy == NO and has_witness:
            self.eligible = True
        if not self.eligible:
            self.reasons_ineligible = []
            if not has_witness:
                self.reasons_ineligible = 'no witness available'
