
from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, Player, Group


class Sesgos(Page):

    # Variables que se utilizarán en esta sección
    form_model = 'player'
    form_fields = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    def is_displayed(self):
        if self.participant.vars['is_mobile'] is False:
            return True
        else:
            return False

    timeout_seconds = 300

class General_fam(Page):

    # Variables que se utilizarán en esta sección
    form_model = 'player'
    form_fields = ['edad', 'sexo', 'distrito', 'ciclo', 'cronica', 'agente_compra',
                   'malestar_compra1', 'malestar_compra2', 'respirat', 'digestiv',
                   'covid', 'ibuprof', 'paracet', 'amoxicil', 'loratadin', 'dexamet']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    def is_displayed(self):
        if self.participant.vars['is_mobile'] is False:
            return True
        else:
            return False

    timeout_seconds = 300

class Pagos(Page):
    form_model = 'player'
    form_fields = ['quiz_dec_2']

    def vars_for_template(self):
        return {'participant_id': self.participant.label,
                'quiz_earnings': self.participant.vars['quiz_earnings'],
                'numero' : self.participant.vars['quiz_questions_correct']
                }


    def is_displayed(self):
        if self.participant.vars['is_mobile'] is False:
            return True
        else:
            return False



# Orden en que se mostrarán las páginas
page_sequence = [Sesgos,
                 General_fam,
                 Pagos]