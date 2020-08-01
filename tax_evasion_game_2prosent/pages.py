
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Initial_setup_distribuer_penger(WaitPage):
    after_all_players_arrive = 'after_all_players_arrive'
    title_text = 'Setter opp spill.'
class First_deklarering2(Page):
    form_model = 'player'
    form_fields = ['deklarert']
class Waiting(WaitPage):
    after_all_players_arrive = 'trekker_fra_deklarering_og_tar_40_prosent_og_betaler_tilbake'
    title_text = 'Vanter på andre spillere'
class Sannsynlighet(Page):
    form_model = 'player'
    def is_displayed(self):
        
        #if self.subsession.random_number <= 2:
        if self.player.random_number12 <= 2:
            if (self.player.utbetalt - self.player.deklarert) == 0:
                self.group.final_opptjent_saa_langt()
                return True
            else:
                self.player.payof = self.group.skatt_hva_man_faar_tilbake -((self.player.utbetalt - self.player.deklarert)*15) 
                self.group.final_opptjent_saa_langt()
                return True
        else:
            #Script her. Skip.
            return False
            
        
    def before_next_page(self):
        pass
class Show_stat(Page):
    form_model = 'player'
    def is_displayed(self):
        #if self.subsession.random_number > 2:
        if self.player.random_number12 > 2:
            return True
        else:
            return False
        #Implementer slik at når sansynlighet har blitt vist blir ikke denne vist.
page_sequence = [Initial_setup_distribuer_penger, First_deklarering2, Waiting, Sannsynlighet, Show_stat]