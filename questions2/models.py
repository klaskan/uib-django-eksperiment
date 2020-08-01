
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = 'Questions about how they felt.'
class Constants(BaseConstants):
    name_in_url = 'questions2'
    players_per_group = None
    num_rounds = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    age = models.IntegerField(label='Hva er alderen din?', max=125, min=13)
    gender = models.StringField(choices=[['Male', 'Mann'], ['Female', 'Kvinne'], ['Annet ', 'Annet ']], label='Hva er kjønnet ditt?', widget=widgets.RadioSelect)
    crt_bat = models.IntegerField(label='A bat and a ball cost 22 dollars in total The bat costs 20 dollars more than the ball How many dollars does the ball cost')
    crt_widget = models.IntegerField(label='If it takes 5 machines 5 minutes to make 5 widgets how many minutes would it take 100 machines to make 100 widgets')
    crt_lake = models.IntegerField(label='In a lake there is a patch of lily pads Every day the patch doubles in size If it takes 48 days for the patch to cover the entire lake how many days would it take for the patch to cover half of the lake')
    betale = models.StringField(label='(Dersom du betalte) Hvorfor betalte du? ')
    telefon = models.IntegerField(label='Telefonnummer')