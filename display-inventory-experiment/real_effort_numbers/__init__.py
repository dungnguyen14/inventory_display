from otree.api import *

import random
doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'real_effort_numbers'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3
    payment_per_correct_answer = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number_entered =models.IntegerField()#data type of the answer
    sum_of_number = models.IntegerField()

# PAGES
class AddNumbers(Page):
    form_model = "player"
    form_fields = ["number_entered"] #player enter this
    def vars_for_template(player: Player): #    def vars_for_template(self):
        number_1 = random.randint(1,100)
        number_2 = random.randint(1,100)
        player.sum_of_number = number_1 + number_2
        return {
            "number_1":  number_1,
            "number_2": number_2,
        }

    def before_next_page(player: Player, timeout_happened):
        if player.sum_of_number == player.number_entered:
            player.payoff = C.payment_per_correct_answer


class Results(Page):
    pass

class CombinedResults(Page):
    def is_displayed(self):
        return self.round_number == C.NUM_ROUNDS #return true if correct
#        if self.round_number == C.num_rounds:
#            return True
#        else:
#            return False


    def vars_for_template(player: Player):
        all_players = player.in_previous_rounds() #gather all players
        combined_payoff = 0
        for each_player in all_players:
            combined_payoff += each_player.payoff
        return {
            "combined_payoff":combined_payoff
        }
page_sequence = [AddNumbers, Results, CombinedResults]
