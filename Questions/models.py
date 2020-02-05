
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
	s1 = models.StringField(choices=[['20', '20%'], ['30', '30%'], ['40', '40%'], ['50', '50%']], label='Hvor mange prosent av den deklarerte inntekten tar auksjonarius?', widget=widgets.RadioSelect)
	s2 = models.StringField(choices=[['svar1', '[$0.25, $0.5, $0.75, $1, $1.25, $1.5, $1.75, $2]'], ['svar2', '[$0.25, $0.75, $1, $1.25, $1.5, $1.75, $2]']], label='Dersom du får utbetalingen $0.5, hvilke andre utbetalinger kan de andre deltagerne få? ', widget=widgets.RadioSelect)
	s3 = models.StringField(choices=[['s3svar1', '15 * udeklarert inntekt'], ['s3svar2', '10 * udeklarert inntekt'], ['s3svar3', '2 * udeklarert inntekt']], label='Hvor stor er boten dersom man ikke deklarerer hele inntekten?', widget=widgets.RadioSelect)
	s4 = models.StringField(choices=[['ja', 'Ja'], ['nei', 'Nei']], label='Dersom man ikke deklarerer noe. Vil man fortsatt motta noe fra auksjonarius dersom noen av de andre deltakerne deklarerte noe?', widget=widgets.RadioSelect)
