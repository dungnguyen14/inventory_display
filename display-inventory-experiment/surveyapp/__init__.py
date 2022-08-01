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
    age = models.IntegerField(label="Please enter your age")
    gender = models.StringField(
        label="Please choose your gender",
        choices=["Male","Female","Other"] #cannot enter

    )
    is_lefthanded = models.BooleanField(label="Are you lefthanded?",
                                        choice=[
                                            [True,"Yes"],
                                            [False, "No"]
                                        ])
# PAGES
class SurveyQuestion(Page):
    form_model = "player"
    form_fields = ["age","gender","is_lefthanded"]


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [SurveyQuestion]
