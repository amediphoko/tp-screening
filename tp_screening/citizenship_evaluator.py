from edc_constants.constants import YES, NO


class CitizenshipEvaluator:
    '''eligible if citizen of botswana or legally married to a motswana'''

    def __init__(self, citizenship=None, legally_married=None, has_proof=None):
        self.eligible = False
        self.reasons_ineligible = None
        if citizenship == YES:
            self.eligible = True
        elif citizenship == NO and legally_married and has_proof:
            self.eligible = True
        if not self.eligible:
            self.reasons_ineligible = []
            if not legally_married:
                self.reasons_ineligible = 'Not a citizen of Botswana'
            if legally_married and not has_proof:
                self.reasons_ineligible = 'Proof of marriage not provided'
