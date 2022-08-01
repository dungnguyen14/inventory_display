from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'multiply_app'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    factor = 3

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number_entered = models.IntegerField ()



# PAGES
class MyPage(Page):
    form_model = "player" #choose form model player or group
    form_fields = ["number_entered"] #list because player might enter multiple values



class ResultsWaitPage(WaitPage):
    pass


class Results(Page):

    def vars_for_template (player: Player): #display result to subject
        result = player.number_entered * C.factor #use result that player enteres
        return {
            "result": result, #key: var assigned
        }


page_sequence = [MyPage, Results]
