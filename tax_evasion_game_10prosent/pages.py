
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Initial_setup_distribuer_penger(WaitPage):
	title_text = 'Setter opp spill.'
	def after_all_players_arrive(self):
		self.group.after_all_players_arrive()
class First_deklarering3(Page):
	form_model = 'player'
	form_fields = ['deklarert']
class Waiting(WaitPage):
	title_text = 'Vanter på andre spillere'
	def after_all_players_arrive(self):
		self.group.trekker_fra_deklarering_og_tar_40_prosent_og_betaler_tilbake()
class Sannsynlighet(Page):
	form_model = 'player'
	def is_displayed(self):
		
		if self.player.random_number12 <= 10:
		    self.player.payof = -((self.player.utbetalt - self.player.deklarert)*15)
		    return True
		else:
		    #Script her. Skip.
		    return False
		    
		
	def before_next_page(self):
		pass
class Show_stat(Page):
	form_model = 'player'
	def is_displayed(self):
		if self.player.random_number12 > 10:
		    return True
		else:
		    return False
		#Implementer slik at når sansynlighet har blitt vist blir ikke denne vist.
page_sequence = [Initial_setup_distribuer_penger, First_deklarering3, Waiting, Sannsynlighet, Show_stat]
