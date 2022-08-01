from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'additional_question'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ques_check_inv = models.StringField(label="Do you find it useful to check the inventory level on the website before going to the store ? ",
                                        choices=[1, 2, 3, 4, 5],
                                        widget=widgets.RadioSelectHorizontal)
    ques_check_inv2 = models.StringField(label="Have you ever noticed the inventory inaccuracy in real world? ",
                                        choices=[1, 2, 3, 4, 5],
                                        widget=widgets.RadioSelectHorizontal)
    ques_check_inv3 = models.StringField(label="How often do you check the inventory level on the website before going to the store   ",
                                        choices=[1, 2, 3, 4, 5],
                                        widget=widgets.RadioSelectHorizontal)
    ques_check_inv4 = models.StringField(label="How often do you shop online?",
                                        choices=[1, 2, 3, 4, 5],
                                        widget=widgets.RadioSelectHorizontal)

    ques_check_inv5 = models.StringField(label="Do you feel disappointed if you go to a store to buy a product and find out it is out-of-stock?",
                                        choices=[1, 2, 3, 4, 5],
                                        widget=widgets.RadioSelectHorizontal)

#    ques_check_inv6 = models.StringField(label="When you look at a product on the website, you see that the store has enough of the products you want, but when you go to the store, there aren't. How disappointed are you?",
#                                        choices=[1, 2, 3, 4, 5],
#                                        widget=widgets.RadioSelectHorizontal)

#    ques_check_inv7 = models.StringField(label="The inventory level is represented by a traffic light (e.g., red - out of stock, green - available, yellow - low stock)",
#                                        choices=[1, 2, 3, 4, 5],
#                                        widget=widgets.RadioSelectHorizontal)
#    ques_check_inv8 = models.StringField(label="The inventory level is represented by exact quantity of available items (i.e., 8 items available)",
#                                        choices=[1, 2, 3, 4, 5],
#                                        widget=widgets.RadioSelectHorizontal)
#    ques_check_inv9 = models.StringField(label="The inventory level is represented by Available / Out of stock",
#                                        choices=[1, 2, 3, 4, 5],
#                                        widget=widgets.RadioSelectHorizontal)


# PAGES
class AdditionalQuestion(Page):
    form_model = "player"
    form_fields = ["ques_check_inv","ques_check_inv5"]
#    form_fields = ["ques_check_inv","ques_check_inv5"]

class AdditionalQuestion_page2(Page):
    form_model = "player"
    form_fields = ["ques_check_inv2","ques_check_inv3","ques_check_inv4"]

#class AdditionalQuestion_page3(Page):
#    form_model = "player"
#    form_fields = ["ques_check_inv7","ques_check_inv8","ques_check_inv9"]


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

page_sequence = [AdditionalQuestion,AdditionalQuestion_page2]

#page_sequence = [AdditionalQuestion, AdditionalQuestion_page2,AdditionalQuestion_page3 ]
