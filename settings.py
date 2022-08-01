from os import environ


SESSION_CONFIGS = [
    dict(
        name='all_questions',
        display_name="Complete Survey",
        app_sequence=['pre_experiment','inventory_display','surveyapp','measure_risk_attitude','additional_question'],
        num_demo_participants=1,
    ),
    dict(
        name='surveyapp',
        display_name="Demographic information questions",
        app_sequence=['surveyapp', 'inventory_display', 'measure_risk_attitude'],
        num_demo_participants=1,
    )
    ,

    #    dict(
#        name='real_effort_numbers',
#        display_name="A task which adds numbers",
#        app_sequence=['real_effort_numbers'],
#        num_demo_participants=1, #should be minimum
#    ),

    dict(
        name='inventory_display',
        display_name="Experiment on the go-to-store decision ",
        app_sequence=['inventory_display'],
        num_demo_participants=1, #should be minimum
   )
    ,
    dict(
        name='measure_risk_attitude',
        display_name='Risk attitude question',
        num_demo_participants=1, #should be minimum
        app_sequence=['measure_risk_attitude'],

    ),
    dict(
        name='additional_question',
        display_name='Additional questions',
        num_demo_participants=1,  # should be minimum
        app_sequence=['additional_question'],

    ),
    dict(
        name='pre_experiment',
        display_name='Instruction and pre-experiment trials',
        num_demo_participants=1,  # should be minimum
        app_sequence=['pre_experiment'],

    )

]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=1.50, doc="",
    mturk_hit_settings=dict(
        keywords='bonus,study',
        title='Experiments on customer behavior towards the displayed inventory information',
        description='Decide whether or not you want to go to store after checking the inventory online',
        frame_height=500,
        template='global/mturk_template.html',
        minutes_alloted_per_ssignment=60,
        expiration_hours=7*24,
        grant_qualification_id='complete01',
        qualification_requirements=[
            {
                'QualificationTypeId': "00000000000000000071",
                'Comparator': "EqualTo",
                'LocaleValues': [{'Country': "US"}]
            },
            # At least 100 HITs approved
            {
                'QualificationTypeId': "00000000000000000040",
                'Comparator': "GreaterThanOrEqualTo",
                'IntegerValues': [100]
            },
            # At least 95% of HITs approved
            {
                'QualificationTypeId': "000000000000000000L0",
                'Comparator': "GreaterThanOrEqualTo",
                'IntegerValues': [95]
            },
            # to prevent retakes
            {
                'QualificationTypeId': "complete01",
                'Comparator': "DoesNotExist",
            }
        ]

    )
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY

REAL_WORLD_CURRENCY_CODE = 'USD'

USE_POINTS = True #use real world currency usd


ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '7475244659486'

INSTALLED_APPS = ['otree']

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

