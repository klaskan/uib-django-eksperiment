
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = 'This is a game about love❤️x2'
class Constants(BaseConstants):
	players_per_group = None
	num_rounds = 8
	utbetalt = (0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2)
	runde1_sansynlighet = 0
	runde2_sansynlighet = 2
	runde3_sansynlighet = 10
	skatt = 40
	var_sum_deklarert = 0
	name_in_url = 'game3'
	straffe_multiplikator = 15
class Subsession(BaseSubsession):
	total_deklarering = models.FloatField(initial=0)
	random_number = models.IntegerField(initial=0)
	def creating_session(self):
		import random
		#Denne koden vil bli utført når man lager en ny session. creating_session() allows you to set initial values on fields on players, groups, participants, or the subsession.
		#Lag en variabel som gir spillerene inntektn deres. Denne vil gi inntekten deres gjennom alle rundene.
		
		#Denne distribuerer pengene fra listen tupelen listen vår.
		players = self.get_players()
		#rounds = self.in_all_rounds()
		wages = list(Constants.utbetalt)
		
		random.shuffle(wages)
		for p in players:
		    p.utbetalt = wages[p.id_in_group - 1]
		
		
		#try:
		#for r in rounds:
		#    random.shuffle(wages)
		#    for p in players:
		#        p.utbetalt = wages[p.id_in_group]
		#except:
		#    continue
		    
		    
		    #for i in range(1,9):
		        #self.id_in_group.utbetalt = wages[i]
		        #self.get_player_by_id(i).utbetalt = wages[i]
		
		#--------------------------------------        
		#KALKULERER total mengde deklarert og gang det med 2 og distribuer tilbake.
		#Men det dere deklarerer til myndighetene vil pli sammlet opp i en fellet pott og ganget med 2 for derretter å bli distribuert tilbake likt mellom alle spillerene.
		#Dette gjelder i denne subseksjonen
		#for pla in players:
		#    self.group.totalt_bidrag = self.group.totalt_bidrag + pla.deklarert
		
		
		self.random_integer()
		
	def random_integer(self):
		import random
		self.random_number = random.randint(1,100)
		
	def kalkuler_straff(self):
		pass
class Group(BaseGroup):
	totalt_bidrag = models.FloatField(initial=0)
	andel_samlet_opp_i_skatt = models.FloatField(initial=0)
	skatt_hva_man_faar_tilbake = models.FloatField(initial=0)
	def after_all_players_arrive(self):
		import random
		players = self.get_players()
		#wages = list(Constants.utbetalt)
		#random.shuffle(wages)
		#for p in players:
		#    p.payoff = wages.pop()
		
		#Kalkulerer hvor mye alle har deklarert til sammen.
		
		#self.trekker_fra_deklarering_og_tar_40_prosent_og_betaler_tilbake()
		for p in players:
		    p.random_number12 = random.randint(1,100)
		
	def trekker_fra_deklarering_og_tar_40_prosent_og_betaler_tilbake(self):
		players = self.get_players()
		
		for p in players:
		    deklarert_inntekt_fratrukket_skatt = p.deklarert * 0.60 
		    p.payof = (p.utbetalt - p.deklarert) + deklarert_inntekt_fratrukket_skatt
		    p.payof = round(p.payof, 2)
		    for r in p.in_all_rounds():
		        p.total_payof = p.total_payof + r.payof 
		        p.total_payof = round(p.total_payof, 3)
		
		self.total_mengde1_fratrukket_skatt_delt_8()
		self.final_opptjent_saa_langt()
	def total_mengde1(self):
		players = self.get_players()
		for pla in players:
		    self.totalt_bidrag = self.totalt_bidrag + pla.deklarert
	def total_mengde1_fratrukket_skatt_delt_8(self):
		self.total_mengde1()
		self.skatt_hva_man_faar_tilbake = ((self.totalt_bidrag * 0.4)*2)/8
		players = self.get_players()
		for p in players:
		    p.payof = p.payof + self.skatt_hva_man_faar_tilbake
		    p.payof = round(p.payof, 2)
		    p.total_payof
		
	def final_opptjent_saa_langt(self):
		players = self.get_players()
		
		for p in players:
		    p.final_total_payof = sum([p.payof for p in p.in_all_rounds()])
		    
class Player(BasePlayer):
	utbetalt = models.FloatField(initial=0, min=0)
	deklarert = models.FloatField(initial=0, max=0, min=0)
	totalt_opptjent = models.FloatField(initial=0)
	payof = models.FloatField(initial=0)
	total_payof = models.FloatField(initial=0)
	final_total_payof = models.FloatField(initial=0)
	straff = models.FloatField(initial=0)
	random_number12 = models.IntegerField()
	def utbetaling(self):
		import random
		self.utbetalt = Constants.utbetalt.pop(random.randrange(len(Constants.utbetalt))) 
		
		    
	def opptjent_inntekt(self):
		self.opptjening = 0
		for p in self.in_all_rounds():
		    self.opptjening = self.opptjening + p.deklarert
		    
	def deklarert_max(self):
		#Denne sørger for at deklarerings variabelene vår ikke tar inn en høyere verdi en det man får utbetalt. 
		return self.utbetalt
