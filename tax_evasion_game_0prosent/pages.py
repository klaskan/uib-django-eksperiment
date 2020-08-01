
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Initial_setup_distribuer_penger(WaitPage):
    after_all_players_arrive = 'after_all_players_arrive'
    title_text = 'Setter opp spill.'
class First_deklarering(Page):
    form_model = 'player'
    form_fields = ['deklarert']
class Waiting(WaitPage):
    after_all_players_arrive = 'trekker_fra_deklarering_og_tar_40_prosent_og_betaler_tilbake'
    title_text = 'Vanter på andre spillere'
class Show_stat(Page):
    form_model = 'player'
    def before_next_page(self):
        self.participant.vars["payof_vars"] = self.player.payof
        self.participant.vars["tatal_payof_vars"] = self.player.total_payof
        self.participant.vars["final_total_payof_vars"] = self.player.final_total_payof
        self.participant.vars["totalt_bidrag_vars"] = self.group.totalt_bidrag
page_sequence = [Initial_setup_distribuer_penger, First_deklarering, Waiting, Show_stat]