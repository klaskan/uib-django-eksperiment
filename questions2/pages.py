
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['telefon']
page_sequence = [CognitiveReflectionTest]