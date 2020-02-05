
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
	form_model = 'player'
class Bekreftet_forstaaelse(Page):
	form_model = 'player'
	form_fields = ['s1', 's2', 's3', 's4']
	def app_after_this_page(self, upcoming_apps):
		if self.player.s1 == "40" and  self.player.s2 == "svar2" and self.player.s3 == "s3svar1" and self.player.s4 == "ja":
		    return upcoming_apps[0]
		
class MyWaitPage(WaitPage):
	def is_displayed(self):
		return True
page_sequence = [Intro, Bekreftet_forstaaelse, MyWaitPage]
