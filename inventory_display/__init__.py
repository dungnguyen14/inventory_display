from otree.api import *
import random
import pandas as pd
#from sklearn.utils import shuffle

doc = """
Your app description
"""

#data_pretest = pd.read_csv(r"C:\Users\PhanThuyDung.Nguyen\Documents\KEDGE\Research\paper 2\Experiment\Pretest3.csv",
#                           encoding="ISO-8859-1", low_memory=False)
data_pretest = pd.read_csv("_static/Pretest4.csv",encoding="ISO-8859-1", low_memory=False)
#data_pretest=shuffle(data_pretest)
data_pretest=data_pretest.reset_index(drop=True)


class C(BaseConstants):
    NAME_IN_URL = 'inventory_display'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 27
    payment_per_correct_answer = 1
    penalty_per_wrong_answer = -2
    max_num_failed_attention_check = 4

    fixed_payoff = 5
    fixed_participation = 1.5 #usd
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(label="Will you go to the store?",
                                  choices=["Go", "Not go"],
                                  widget=widgets.RadioSelectHorizontal)  # data type of the answer
    sum_payoff = models.IntegerField()
    display_inventory = models.IntegerField()
    demand = models.IntegerField()
    actual_inventory = models.IntegerField()
    penalty_per_wrong_answer = models.IntegerField()
    error = models.IntegerField()
    round = models.IntegerField()
    attention_check = models.BooleanField()
    result_round = models.BooleanField()
#    final_payoff = models.FloatField()
#    bonus = models.FloatField()
### New variables
    failed_attention = models.BooleanField(initial=False)
    num_failed_attention = models.IntegerField(initial=0)
#(blank=True)

# PAGES
class Experiment(Page):
    form_model = "player"
    form_fields = ["decision"]  # player enter this

    def vars_for_template(self):
        self.penalty_per_wrong_answer = C.penalty_per_wrong_answer
        #        if self.round_number <= 6:
        #            self.penalty_per_wrong_answer =  C.penalty_per_wrong_answer

        #        else:
        #            self.penalty_per_wrong_answer =  C.penalty_per_wrong_answer - 4

        # self.penalty_per_wrong_answer=self.in_previous_rounds()[0].penalty_per_wrong_answer

        #        self.display_inventory = random.randint(1, 10)
        #        self.demand = random.randint(1, self.display_inventory+ random.randint(1, 2))
        #        error=random.randint(0, 4)
        #        self.actual_inventory = max(0, self.display_inventory - error)

        self.display_inventory = data_pretest['Shown_inventory'][self.round_number - 1].item()
        self.demand = data_pretest['Demand'][self.round_number - 1].item()
        self.error = data_pretest['Inventory_inaccuracy'][self.round_number - 1].item()
        self.actual_inventory = data_pretest['Actual_inventory'][self.round_number - 1].item()
        self.round = data_pretest['Round'][self.round_number - 1].item()
        self.attention_check = data_pretest['Attention_check'][self.round_number - 1].item()

        return {
            "display_inventory": self.display_inventory,
            "demand": self.demand,
            "actual_inventory": self.actual_inventory,
            "penalty_per_wrong_answer": self.penalty_per_wrong_answer

        }

    def before_next_page(self, timeout_happened):
#        if self.round_number != 7 and self.round_number != 14 and self.round_number != 21:

        if self.attention_check == False:
            if self.actual_inventory >= self.demand:
                if self.decision == "Go":
                    self.payoff = C.payment_per_correct_answer
                    self.result_round = True
                else:
                    self.payoff = 0

            else:
                if self.decision == "Go":
                    self.payoff = self.penalty_per_wrong_answer
                    self.result_round = False

                else:
                    self.payoff = 0
                    self.result_round = True

        else:
            self.payoff = 0
            if self.decision == "Go":
                self.failed_attention = True

            #    self.participant.vars["failed_attention_check"] = False  # participant not player i.e. 10 rounds -> 10 players but only 1 participant
            else:
            #    self.participant.vars["failed_attention_check"] = True
                self.failed_attention = False

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    def display_decision(self, timeout_happened):
        return self.decision

    def vars_for_template(self):
        all_players = self.in_all_rounds()
        combined_payoff = 0

        for each_player in all_players:
            combined_payoff += each_player.payoff

            if each_player.failed_attention:
                self.num_failed_attention += 1

        return {
            "combined_payoff": combined_payoff + C.fixed_payoff

        }

    def display_failed_attention_check(self):
        return {
            "failed_attention": self.failed_attention
        }

class CombinedResults(Page):
    def is_displayed(self):
        return self.round_number == C.NUM_ROUNDS  # return true if correct

    def vars_for_template(player: Player):
        all_players = player.in_all_rounds()
        sum_payoff = 0
        for each_player in all_players:
            sum_payoff += each_player.payoff

#        if sum_payoff + 5 >= 0:
#            player.bonus = (float(sum_payoff) + 5) * 0.25
#        else:
#            player.bonus = 0

#        player.final_payoff = C.fixed_participation + player.bonus
        if sum_payoff + 5 >= 0:
            bonus = (float(sum_payoff) + 5) * 0.25
        else:
            bonus = 0
        player.payoff = C.fixed_participation + bonus

        return {
#            "final_payoff": player.final_payoff,
            "final_payoff": player.payoff,
            "sum_payoff": sum_payoff + 5,
            "bonus": bonus

#            "sum_payoff": final_payoff
#            "bonus": player.bonus
        }


class FailAttentionCheck(Page):
    def is_displayed(self):
        return self.num_failed_attention == C.max_num_failed_attention_check
        #return self.participant.vars["failed_attention_check"]  # only show if fail attention check


class Introductions(Page):
    def is_displayed(self):
        return self.participant.vars["failed_attention_check"]  # only show if fail attention check


page_sequence = [Experiment, Results, FailAttentionCheck, CombinedResults]
