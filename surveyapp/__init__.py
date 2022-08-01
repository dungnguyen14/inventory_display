from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'surveyapp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
#    age = models.IntegerField(label="Please enter your age")
#
    age = models.StringField(label="What is your age?",
                             choices=["Under 15","15-24","25-34","35-44","45-54","55-64","65 and over"])
#                             widget=widgets.RadioSelect)  # data type of the answer


    gender = models.StringField(
        label="Please choose your gender",
        choices=["Male","Female","Other"] #cannot enter

    )


    income = models.StringField(
        label="Please indicate your approximate yearly household income before taxes ?",
        choices=["Less than $25,000", "$25,000 - $49,999", "$50,000 - 99,999", "$100,000 - $149,999","$150,000 and more"] ) # cannot enter

    education = models.StringField(
    label="What is the highest degree or level of education you have completed?",
    choices=["High School", "Bachelor's Degree", "Master's Degree", "Ph.D. or higher", "Other"]
)
#    is_lefthanded = models.BooleanField(label="Are you lefthanded?",
#                                        choice=[
#                                            [True,"Yes"],
#                                            [False, "No"]
#                                        ])

# PAGES
class SurveyQuestion(Page):
    form_model = "player"
    form_fields = ["age","gender","income","education"]


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [SurveyQuestion]
