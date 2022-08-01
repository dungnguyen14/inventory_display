from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'pre_experiment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    check_1 = models.StringField(label="Is there sufficient inventory at the store for you?",
                             choices=["Yes", "No"],widget=widgets.RadioSelect)  # data type of the answer
    check_2 = models.StringField(label="What will you receive?",
                             choices=["A penalty", "A bonus", "0"],widget=widgets.RadioSelect)  # data type of the answer
    check_3 = models.StringField(label="What is the inventory error in this case?",
                             choices=["0","1", "2", "3","4","5","6"])  # data type of the answer
    check_4 = models.IntegerField(label="What is your desired quantity of item?")
    check_5 = models.IntegerField(label="What is the displayed inventory of the item on the website?")
    check_6 = models.IntegerField(label="What is the actual inventory of the product at the store?")
    check_7 = models.StringField(label="What is your decision in this case?",
                             choices=["Go", "Not go"],widget=widgets.RadioSelect)  # data type of the answer

    fail_attention = models.BooleanField(initial=False)
# PAGES
class Instruction_1(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return self.in_round(1).fail_attention == True


class Instruction_2(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return self.in_round(1).fail_attention == True

class PaymentIns(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return self.in_round(1).fail_attention == True

class CheckReading(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return self.in_round(1).fail_attention == True
    form_model = "player"
    form_fields = ["check_1", "check_2","check_3","check_4","check_5","check_6","check_7"]
    def before_next_page(self, timeout_happened):
        if self.check_1 =="No" and self.check_2 =="A penalty" and self.check_3 =="5" and self.check_4==5 and self.check_5==8 and self.check_6==3 and self.check_7=="Go":
            self.fail_attention = False
        else:
            self.fail_attention = True


class FailedAttentionCheck(Page):
    def is_displayed(self):
        return self.fail_attention==True

class Structure(Page):
    pass


class Results(Page):
    pass


page_sequence = [Structure, Instruction_1, Instruction_2, PaymentIns,CheckReading,FailedAttentionCheck]