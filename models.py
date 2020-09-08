
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

doc = ''


class Constants(BaseConstants):
    """
    Description:
        Inherits oTree Class BaseConstants. Defines constants for
        the experiment these will remain unchanged
    """

    players_per_group = None
    num_rounds = 1
    timer = 20
    payment_per_answer = c(0.2)


    instructions_template = 'meds_tercero/InstruccionesB.html'
    instructions_button = "meds_tercero/Instructions_Button.html"
    contact_template = "meds_tercero/Contactenos.html"

    name_in_url = 'pxe_otr_med3'  # name in webbrowser




class Subsession(BaseSubsession):

    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):


    # Preguntas adicionales
    edad = models.IntegerField(choices=[[18, '18'], [19, '19'], [20, '20'], [21, '21'], [22, '22'], [23, '23'], [24, '24'], [25, '25'],
                                        [26, '26'], [27, '27'], [28, '28'], [29, '29'], [30, '30'], [31, '31'], [32, '32'], [33, '33'],
                                        [34, '34'], [35, '35'], [36, '36'], [37, '37'], [38, '38'], [39, '39'], [40, '40']], label='Edad')
    sexo = models.IntegerField(choices=[[0, 'Masculino'], [1, 'Femenino']], label='Sexo', widget=widgets.RadioSelect)
    distrito = models.IntegerField(choices=[[1, 'Ancón'], [2, 'Ate Vitarte'], [3, 'Barranco'], [4, 'Breña'], [5, 'Carabayllo'],
                                           [6, 'Cercado de Lima'], [7, 'Chaclacayo'], [8, 'Chorrillos'], [9, 'Cieneguilla'], [10, 'Comas'],
                                           [11, 'El Agustino'], [12, 'Independencia'], [13, 'Jesús María'], [14, 'La Molina'], [15, 'La Victoria'],
                                           [16, 'Lince'], [17, 'Los Olivos'], [18, 'Lurigancho'], [19, 'Lurín'], [20, 'Magdalena del Mar'],
                                           [21, 'Miraflores'], [22, 'Pachacamac'], [23, 'Pucusana'], [24, 'Pueblo Libre'], [25, 'Puente Piedra'],
                                           [26, 'Punta Hermosa'], [27, 'Punta Negra'], [28, 'Rímac'], [29, 'San Bartolo'], [30, 'San Borja'],
                                           [31, 'San Isidro'], [32, 'San Juan de Lurigancho'], [33, 'San Juan de Miraflores'], [34, 'San Luis'], [35, 'San Martín de Porres'],
                                           [36, 'San Miguel'], [37, 'Santa Anita'], [38, 'Santa María'], [39, 'Santa Rosa'], [40, 'Surco'],
                                           [41, 'Surquillo'], [42, 'Villa el Salvador'], [43, 'Villa María del Triunfo']], label='Distrito de residencia')
    ciclo = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'],
                                         [7, '7'], [8, '8'], [9, '9'], [10, '10'], [11, '11'], [12, '12']], label='Último ciclo cursado')
    cronica = models.IntegerField(choices=[[1, 'Sí'], [0, 'No']], label='¿Sufre de alguna enfermedad crónica?', widget=widgets.RadioSelect)
    agente_compra = models.IntegerField(choices=[[1, 'Sí'], [0, 'No']], label='Cuando en tu hogar se necesita comprar medicamentos, ¿eres tú quien realiza la compra?', widget=widgets.RadioSelect)
    malestar_compra1 = models.IntegerField(choices=[[1, 'Sí'], [0, 'No']], label='Cuando te sientes mal, ¿recurres al uso de medicamentos autorrecetados?', widget=widgets.RadioSelect)
    malestar_compra2 = models.IntegerField(choices=[[1, 'Sí'], [0, 'No']], label='Cuando te sientes mal, ¿recurres a la compra de medicamentos recetados por un médico?', widget=widgets.RadioSelect)
    respirat = models.IntegerField(choices=[[1, 'Sí'], [0, 'No']], label='¿Has sufrido recientemente de enfermedades relacionadas al aparato respiratorio?', widget=widgets.RadioSelect)
    digestiv = models.IntegerField(choices=[[1, 'Sí'], [0, 'No']], label='¿Has sufrido recientemente de enfermedades relacionadas al aparato digestivo?', widget=widgets.RadioSelect)
    covid = models.IntegerField(choices=[[1, 'Sí'], [0, 'No']], label='¿Has sufrido/sufres de síntomas de Covid-19?', widget=widgets.RadioSelect)
    ibuprof = models.IntegerField(choices=[[1, 'Sí'], [0, 'No']], label='¿Alguna vez has consumido Ibuprofeno?', widget=widgets.RadioSelect)
    paracet = models.IntegerField(choices=[[1, 'Sí'], [0, 'No']], label='¿Alguna vez has consumido Paracetamol?', widget=widgets.RadioSelect)
    amoxicil = models.IntegerField(choices=[[1, 'Sí'], [0, 'No']], label='¿Alguna vez has consumido Amoxicilina?', widget=widgets.RadioSelect)
    loratadin = models.IntegerField(choices=[[1, 'Sí'], [0, 'No']], label='¿Alguna vez has consumido Loratadina?', widget=widgets.RadioSelect)
    dexamet = models.IntegerField(choices=[[1, 'Sí'], [0, 'No']], label='¿Alguna vez has consumido Dexametasona?', widget=widgets.RadioSelect)


    # Heurísticos
    d1 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], label='Estaría dispuesto a comprar cierto tipo de medicamento solo porque mi médico me lo recomendó', widget=widgets.RadioSelectHorizontal)
    d2 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], label='Los medicamentos genéricos son de menor calidad que los medicamentos de marca', widget=widgets.RadioSelectHorizontal)
    d3 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], label='Un medicamento de marca debe costar más', widget=widgets.RadioSelectHorizontal)
    d4 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], label='Recuerdo o relaciono a los medicamentos genéricos con la existencia de una baja regulación por parte de las entidades competentes (Dirección General de Medicamentos, Insumos y Drogas y Ministerio de Salud)', widget=widgets.RadioSelectHorizontal)
    d5 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], label='Si un químico farmacéutico me recomendara comprar cierto tipo de medicamento, seguiría dicha recomendación', widget=widgets.RadioSelectHorizontal)
    d6 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], label='Un mayor precio indica una mayor calidad del medicamento', widget=widgets.RadioSelectHorizontal)
    d7 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], label='Compraría un medicamento solo porque muchas personas cercanas a mí lo usan', widget=widgets.RadioSelectHorizontal)
    d8 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], label='Si fuera a una farmacia a comprar un medicamento, preferiría el que más compra la gente', widget=widgets.RadioSelectHorizontal)
    d9 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], label='He escuchado noticias u opiniones negativas sobre los medicamentos genéricos', widget=widgets.RadioSelectHorizontal)


    # Hidden Field for detecting bots
    quiz_dec_2 = models.LongStringField(blank=True)
