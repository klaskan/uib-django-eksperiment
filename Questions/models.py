
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = 'Gir informasjon og spør etter telefonnummer.'
class Constants(BaseConstants):
    name_in_url = 'Questions'
    players_per_group = None
    num_rounds = 10
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    phone_number = models.IntegerField()
    s1 = models.StringField(choices=[['20', '20%'], ['30', '30%'], ['40', '40%'], ['50', '50%']], label='Hvor mange prosent blir tatt av det du oppgir?', widget=widgets.RadioSelect)
    s2 = models.StringField(choices=[['svar1', '{1kr, 2kr, 3kr, 4kr, 5kr, 6kr, 7kr , 8kr}'], ['svar2', '{1kr, 3kr, 4kr, 5kr, 6kr, 7kr, 8kr}']], label='Dersom du får utbetalingen 2kr, hvilke andre utbetalinger kan de andre deltagerne få? ', widget=widgets.RadioSelect)
    s3 = models.StringField(choices=[['s3svar1', '15 * (ikke oppgitt utbetaling)'], ['s3svar2', '10 * (ikke oppgitt utbetaling)'], ['s3svar3', '2 * (ikke oppgitt utbetaling)']], label='Hvor stor er boten dersom man ikke deklarerer hele inntekten?', widget=widgets.RadioSelect)
    s4 = models.StringField(choices=[['ja', 'Ja'], ['nei', 'Nei']], label='Dersom man ikke oppgir noe. Vil man fortsatt få noe dersom noen av de andre oppga noe?', widget=widgets.RadioSelect)