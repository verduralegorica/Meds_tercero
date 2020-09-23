
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
        if self.participant.vars['MobilePhones'] is False:
            return True
        else:
            return False

    timeout_seconds = 300

class General_fam(Page):

    # Variables que se utilizarán en esta sección
    form_model = 'player'
    form_fields = ['anterior', 'edad', 'sexo', 'escala', 'educ_padre', 'educ_madre', 'distrito', 'ciclo',
                   'cronica', 'agente_compra', 'malestar_compra1', 'malestar_compra2',
                   'respirat', 'digestiv', 'covid',
                   'ibuprof', 'ranitidin', 'amoxicil', 'loratadin', 'dexamet', 'epinef',
                   'alergia', 'natural', 'natural_caso',
                   'respirat_c', 'digestiv_c', 'covid_c']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    def is_displayed(self):
        if self.participant.vars['MobilePhones'] is False:
            return True
        else:
            return False

    timeout_seconds = 480

class Pagos(Page):
    form_model = 'player'
    form_fields = ['quiz_dec_2']

    def vars_for_template(self):
        return {'participant_id': self.participant.label,
                'quiz_earnings': self.participant.vars['quiz_earnings'],
                'numero': self.participant.vars['quiz_questions_correct'],
                'ea1': self.participant.vars['ea1'],
                'ea2': self.participant.vars['ea2'],
                'ea3': self.participant.vars['ea3'],
                'ea4': self.participant.vars['ea4'],
                'pago_final': self.participant.vars['quiz_earnings'] + 5
                }


    def is_displayed(self):
        if self.participant.vars['MobilePhones'] is False:
            return True
        else:
            return False



# Orden en que se mostrarán las páginas
page_sequence = [Sesgos,
                 General_fam,
                 Pagos]