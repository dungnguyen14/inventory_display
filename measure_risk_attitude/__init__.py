from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'measure_risk_attitude'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ques_1 = models.StringField(label = "Please indicate your preference between each of the pairs of gambles",
                                choices=["10% chance of $100, 90% chance of $80", "10% chance of $190, 90% chance of $5"],
                                  widget=widgets.RadioSelectHorizontal)
    ques_2 = models.StringField(label = "Please indicate your preference between each of the pairs of gambles",
                                choices=["20% chance of $100, 80% chance of $80", "20% chance of $190, 80% chance of $5"],
                                  widget=widgets.RadioSelectHorizontal)
    ques_3 = models.StringField(label = "Please indicate your preference between each of the pairs of gambles",
                                choices=["30% chance of $100, 70% chance of $80", "30% chance of $190, 70% chance of $5"],
                                  widget=widgets.RadioSelectHorizontal)
    ques_4 = models.StringField(label = "Please indicate your preference between each of the pairs of gambles",
                                choices=["40% chance of $100, 60% chance of $80", "40% chance of $190, 60% chance of $5"],
                                  widget=widgets.RadioSelectHorizontal)
    ques_5 = models.StringField(label = "Please indicate your preference between each of the pairs of gambles",
                                choices=["50% chance of $100, 50% chance of $80", "50% chance of $190, 50% chance of $5"],
                                  widget=widgets.RadioSelectHorizontal)
    ques_6 = models.StringField(label = "Please indicate your preference between each of the pairs of gambles",
                                choices=["60% chance of $100, 40% chance of $80", "60% chance of $190, 40% chance of $5"],
                                  widget=widgets.RadioSelectHorizontal)
    ques_7 = models.StringField(label = "Please indicate your preference between each of the pairs of gambles",
                                choices=["70% chance of $100, 30% chance of $80", "70% chance of $190, 30% chance of $5"],
                                  widget=widgets.RadioSelectHorizontal)
    ques_8 = models.StringField(label = "Please indicate your preference between each of the pairs of gambles",
                                choices=["80% chance of $100, 20% chance of $80", "80% chance of $190, 20% chance of $5"],
                                  widget=widgets.RadioSelectHorizontal)
    ques_9 = models.StringField(label = "Please indicate your preference between each of the pairs of gambles",
                                choices=["90% chance of $100, 10% chance of $80", "90% chance of $190, 10% chance of $5"],
                                  widget=widgets.RadioSelectHorizontal)
    ques_10 = models.StringField(label = "Please indicate your preference between each of the pairs of gambles",
                                choices=["100% chance of $100, 0% chance of $80", "100% chance of $190, 0% chance of $5"],
                                  widget=widgets.RadioSelectHorizontal)

    ques_check_inv = models.StringField(label = "Do you find checking online the inventory level at stores useful? ",
                                choices=[1, 2, 3, 4, 5],
                                  widget=widgets.RadioSelectHorizontal)



# PAGES
class RiskAttitude(Page):
    form_model = "player"
    form_fields = ["ques_1","ques_2","ques_3","ques_4","ques_5","ques_6","ques_7","ques_8","ques_9","ques_10"]

class AdditionalQues(Page):
    form_model = "player"
    form_fields = ["ques_check_inv"]

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [RiskAttitude]
