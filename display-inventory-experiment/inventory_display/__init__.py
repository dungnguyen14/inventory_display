from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'inventory_display'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 9
    payment_per_correct_answer = 1
    penalty_per_wrong_answer = -2

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(#label="Will you go to the store?",
                                          choices=["Go","Not go"],
                                          widget=widgets.RadioSelectHorizontal)  # data type of the answer
    sum_payoff = models.IntegerField()

    display_inventory = models.IntegerField()
    demand = models.IntegerField()
    actual_inventory =models.IntegerField()
    penalty_per_wrong_answer = models.IntegerField()
# PAGES
class Round_1(Page):
    form_model = "player"
    form_fields = ["decision"]  # player enter this

    def vars_for_template(self):
        if self.round_number <= 6:
            self.penalty_per_wrong_answer =  C.penalty_per_wrong_answer

#        elif self.round_number > 3 and self.round_number <=6:
#            self.penalty_per_wrong_answer =  C.penalty_per_wrong_answer - 2

        else:
            self.penalty_per_wrong_answer =  C.penalty_per_wrong_answer - 4

            #self.penalty_per_wrong_answer=self.in_previous_rounds()[0].penalty_per_wrong_answer

        self.display_inventory = random.randint(1, 10)
        self.demand = random.randint(1, self.display_inventory+ random.randint(1, 2))
        error=random.randint(0, 4)
        self.actual_inventory = max(0, self.display_inventory - error)
        return {
            "display_inventory":  self.display_inventory,
            "demand": self.demand,
            "actual_inventory": self.actual_inventory,
            "penalty_per_wrong_answer": self.penalty_per_wrong_answer

        }

    def before_next_page(self, timeout_happened):
        if self.actual_inventory >= self.demand:
            if self.decision == "Go":
                self.payoff = C.payment_per_correct_answer
            else:
                self.payoff = 0
        else:
            if self.decision == "Go":
                self.payoff = self.penalty_per_wrong_answer
            else:
                self.payoff = 0


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    def display_decision(player: Player, timeout_happened):
        return player.decision


    def vars_for_template(player: Player):
        all_players = player.in_all_rounds()
        combined_payoff = 0
        for each_player in all_players:
            combined_payoff += each_player.payoff
        return {
            "combined_payoff":combined_payoff
        }

class CombinedResults(Page):
    def is_displayed(self):
        return self.round_number == C.NUM_ROUNDS  # return true if correct
    def vars_for_template(player: Player):
        all_players = player.in_all_rounds()
        sum_payoff = 0
        for each_player in all_players:
            sum_payoff += each_player.payoff
        return {
            "sum_payoff":sum_payoff
        }
page_sequence = [Round_1, Results,CombinedResults]
