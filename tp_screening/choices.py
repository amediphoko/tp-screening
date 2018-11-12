NA = 'NOT ANSWERING'
OT = 'OTHER'


MARITAL_STATUS_CHOICES = (
    ('SINGLE', 'Single'),
    ('MARRIED', 'Married'),
    ('DIVORCED', 'Divorced'),
    ('WIDOWED', 'Widowed'),)

LIVING_ARRANGEMENTS = (
    ('ALONE', 'Alone'),
    ('PARTNER', 'Partner'),
    ('SIBLINGS', 'Siblings'),
    ('OTHER', 'Other'),
    (NA, 'Don\'t want to answer'),)

WORK_TYPE_CHOICES = (
    ('CASUAL EMPLOYMENT', 'Casual Employment'),
    ('SEASONAL EMPLOYMENT', 'Seasonal Employment'),
    ('FW FULL TIME', 'Formal Wage (Full-Time)'),
    ('FW PART TIME', 'Formal Wage (Part-Time)'),
    ('SE AGRICULTURE', 'Self Employed in Agriculture'),
    ('SE FULL TIME', 'Self Employed Full Time'),
    ('SE PART TIME', 'Self Employed Part Time'),
    (NA, 'Don\'t want to answer'),
    (OT, 'Other'),)

INCOME_SCALE = (
    ('None', 'No income'),
    ('1-199', '1-199 pula'),
    ('200-499', '200-499 pula'),
    ('500-999', '500-999 pula'),
    ('1000-4999', '1000-4999 pula'),
    ('5000-10000', '5000-10000 pula'),
    ('>10000', 'More than 10000 pula'),
    (NA, 'Don\'t want to answer'))

ACTIVITY_LEVEL = (
    ('VERY', 'Very Active'),
    ('SOMEWHAT', 'Somewhat Active'),
    ('NOT ACTIVE', 'Not active'),
    (NA, 'Don\'t want to answer'),)

PROBLEM_CHOICES = (
    ('HIV/AIDS', 'HIV and AIDS'),
    ('SCHOOLS', 'Schools'),
    ('SEWER', 'Sewer'),
    ('UNEMPLOYMENT', 'Unemployment'),
    ('ROADS', 'Roads'),
    ('WATER', 'Water'),
    (OT, 'Other'),
    ('HOUSE', 'House'),
    ('MALARIA', 'Malaria'),)
