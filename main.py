from pydoc import text

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

import matplotlib.pyplot as plt

from kivy_garden.matplotlib import FigureCanvasKivyAgg  


class CalculadoraMetalurgica(App):

    def build(self):

        # Layout principal
        self.layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        # Título
        titulo = Label(
            text="METALCALC",
            font_size=25
        )

        self.layout.add_widget(titulo)

        # Botones
        boton_dilucion = Button(text="DILUCIÓN")
        boton_dilucion.bind(on_press=self.dilucion)

        boton_solidos = Button(text="PORCENTAJE DE SÓLIDOS")
        boton_solidos.bind(on_press=self.porcentaje_solidos)

        boton_tonelaje = Button(text="TONELAJE DE PULPA")
        boton_tonelaje.bind(on_press=self.tonelaje_pulpa)

        boton_caudal = Button(text="CAUDAL DE PULPA")
        boton_caudal.bind(on_press=self.caudal_pulpa)

        boton_densidad_pulpa = Button(text="DENSIDAD DE PULPA")
        boton_densidad_pulpa.bind(on_press=self.densidad_pulpa)

        boton_densidad_mineral = Button(text="DENSIDAD DE MINERAL")
        boton_densidad_mineral.bind(on_press=self.densidad_mineral)

        

        boton_salir = Button(text="SALIR")
        boton_salir.bind(on_press=self.salir)

        # Agregar botones
        self.layout.add_widget(boton_dilucion)
        self.layout.add_widget(boton_solidos)
        self.layout.add_widget(boton_tonelaje)
        self.layout.add_widget(boton_caudal)
        self.layout.add_widget(boton_densidad_pulpa)
        self.layout.add_widget(boton_densidad_mineral)
        self.layout.add_widget(boton_salir)

        return self.layout

    # ==========================================
    # DILUCIÓN
    # ==========================================

    def dilucion(self, instance):

        # Limpiar menú principal
        self.layout.clear_widgets()

        # Título
        titulo = Label(
            text="DILUCIÓN",
            font_size=25
        )

        self.layout.add_widget(titulo)

        # Porcentaje de sólidos
        self.layout.add_widget(
            Label(text="PORCENTAJE DE SÓLIDOS")
        )

        self.porcentaje_solidos_input = TextInput(
            hint_text="Ingrese el porcentaje de sólidos",
            input_filter="float",
            multiline=False
        )

        self.layout.add_widget(
            self.porcentaje_solidos_input
        )

        # Botón calcular
        calcular_button = Button(
            text="CALCULAR DILUCIÓN"
        )

        calcular_button.bind(
            on_press=self.calcular_dilucion
        )

        self.layout.add_widget(
            calcular_button
        )

        # Resultado
        self.resultado_label = Label(
            text="Resultado:"
        )

        self.layout.add_widget(
            self.resultado_label
        )

        # Botón regresar
        regresar_button = Button(
            text="REGRESAR AL MENÚ PRINCIPAL"
        )

        regresar_button.bind(
            on_press=self.regresar_al_menu_principal
        )

        self.layout.add_widget(
            regresar_button
        )

    # ==========================================
    # CÁLCULO DE DILUCIÓN
    # ==========================================

    def calcular_dilucion(self, instance):

        try:

            porcentaje_solidos = float(
                self.porcentaje_solidos_input.text
            )

            dilucion = (100 - porcentaje_solidos) / porcentaje_solidos

            self.resultado_label.text = (
                f"Resultado: Dilución = {dilucion:.2f}"
            )

        except ValueError:

            self.resultado_label.text = (
                "Ingrese un valor numérico válido."
            )

        except ZeroDivisionError:

            self.resultado_label.text = (
                "El porcentaje de sólidos no puede ser 0."
            )

    # ==========================================
    # REGRESAR AL MENÚ
    # ==========================================

    def regresar_al_menu_principal(self, instance):

        self.layout.clear_widgets()

        titulo = Label(
            text="METALCALC",
            font_size=25
        )

        self.layout.add_widget(titulo)

        boton_dilucion = Button(text="DILUCIÓN")
        boton_dilucion.bind(on_press=self.dilucion)

        boton_solidos = Button(text="PORCENTAJE DE SÓLIDOS")
        boton_solidos.bind(on_press=self.porcentaje_solidos)

        boton_tonelaje = Button(text="TONELAJE DE PULPA")
        boton_tonelaje.bind(on_press=self.tonelaje_pulpa)

        boton_caudal = Button(text="CAUDAL DE PULPA")
        boton_caudal.bind(on_press=self.caudal_pulpa)

        boton_densidad_pulpa = Button(text="DENSIDAD DE PULPA")
        boton_densidad_pulpa.bind(on_press=self.densidad_pulpa)

        boton_densidad_mineral = Button(text="DENSIDAD DE MINERAL")
        boton_densidad_mineral.bind(on_press=self.densidad_mineral)

        

        boton_salir = Button(text="SALIR")
        boton_salir.bind(on_press=self.salir)

        self.layout.add_widget(boton_dilucion)
        self.layout.add_widget(boton_solidos)
        self.layout.add_widget(boton_tonelaje)
        self.layout.add_widget(boton_caudal)
        self.layout.add_widget(boton_densidad_pulpa)
        self.layout.add_widget(boton_densidad_mineral)
        self.layout.add_widget(boton_salir)

    # ==========================================
    # OPCIONES PENDIENTES
    # ==========================================
    # PORCENTAJE DE SOLIDOS, TONELAJE DE PULPA, CAUDAL DE PULPA, DENSIDAD DE PULPA, DENSIDAD DE MINERAL, CURVA DE MOLIENDABILIDAD
    def porcentaje_solidos(self, instance):
        self.layout.clear_widgets() #LIMPIAR PANTALLA
        # TITULO
        titulo = Label(
            text="PORCENTAJE DE SÓLIDOS(%S)",
            font_size=25
        )
        self.layout.add_widget(titulo)
        # AGREGAR ENTRADA DE DILUCIÓN
        self.layout.add_widget(Label(text="DILUCIÓN DE PULPA"))
        self.dilucion_input = TextInput(
            hint_text="Ingrese la dilución de la pulpa: ",
            input_filter="float", multiline=False
        )
        self.layout.add_widget(self.dilucion_input)
        #BOTON CALCULAR 
        self.calcular_button = Button(text="CALCULAR PORCENTAJE DE SÓLIDOS")
        self.calcular_button.bind(on_press=self.calcular_porcentaje_solidos)
        self.layout.add_widget(self.calcular_button)

        #RESULTADO
        self.resultado_label = Label(text="Resultado:")
        self.layout.add_widget(self.resultado_label)
        # BOTON REGRESAR
        self.regresar_button = Button(text="REGRESAR AL MENÚ PRINCIPAL")
        self.regresar_button.bind(on_press=self.regresar_al_menu_principal)
        self.layout.add_widget(self.regresar_button)
    def calcular_porcentaje_solidos(self, instance):
        try:
            dilucion = float(
                self.dilucion_input.text
            )
            porcentaje_solidos = 100 / (1 + dilucion)
            self.resultado_label.text = (
                f"Resultado: Porcentaje de sólidos = {porcentaje_solidos:.2f}%"
            )
        except ValueError:
            self.resultado_label.text = (
                "Ingrese un valor numérico válido."
            )
        except ZeroDivisionError:
            self.resultado_label.text = (
                "El porcentaje de sólidos no puede ser 0."
            )
    def regresar_al_menu_principal(self, instance):
        self.layout.clear_widgets()

        titulo = Label(
            text="METALCALC",
            font_size=25
        )

        self.layout.add_widget(titulo)

        boton_dilucion = Button(text="DILUCIÓN")
        boton_dilucion.bind(on_press=self.dilucion)

        boton_solidos = Button(text="PORCENTAJE DE SÓLIDOS")
        boton_solidos.bind(on_press=self.porcentaje_solidos)

        boton_tonelaje = Button(text="TONELAJE DE PULPA")
        boton_tonelaje.bind(on_press=self.tonelaje_pulpa)

        boton_caudal = Button(text="CAUDAL DE PULPA")
        boton_caudal.bind(on_press=self.caudal_pulpa)

        boton_densidad_pulpa = Button(text="DENSIDAD DE PULPA")
        boton_densidad_pulpa.bind(on_press=self.densidad_pulpa)

        boton_densidad_mineral = Button(text="DENSIDAD DE MINERAL")
        boton_densidad_mineral.bind(on_press=self.densidad_mineral)

        
        boton_salir = Button(text="SALIR")
        boton_salir.bind(on_press=self.salir)

        self.layout.add_widget(boton_dilucion)
        self.layout.add_widget(boton_solidos)
        self.layout.add_widget(boton_tonelaje)
        self.layout.add_widget(boton_caudal)
        self.layout.add_widget(boton_densidad_pulpa)
        self.layout.add_widget(boton_densidad_mineral)
        self.layout.add_widget(boton_salir)
#............................................................
# CODIGO DE TONELAJE DE PULPA
#------------------------------------------------

    def tonelaje_pulpa(self, instance):
       self.layout.clear_widgets() #LIMPIAR PANTALLA
       # TITULO
       titulo = Label(
                text="TONELAJE DE PULPA",
                font_size=25
          )
       self.layout.add_widget(titulo)
       # AGREGAR ENTRADA DE TONELAJE
       self.layout.add_widget(Label(text="TONELAJE SECO (TPH)"))
       self.tonelaje_input = TextInput(hint_text="Ingrese el tonelaje seco", input_filter='float', multiline=False)
       self.layout.add_widget(self.tonelaje_input)

       # AGREGAR ENTRADA DE PORCENTAJE DE SOLIDOS
       self.layout.add_widget(Label(text="PORCENTAJE DE SÓLIDOS (%S)"))
       self.porcentaje_solidos_input = TextInput(hint_text="Ingrese el porcentaje de sólidos", input_filter='float', multiline=False)
       self.layout.add_widget(self.porcentaje_solidos_input)
       # BOTON CALCULAR
       self.calcular_button = Button(text="CALCULAR TONELAJE DE PULPA")
       self.calcular_button.bind(on_press=self.calcular_tonelaje_pulpa)
       self.layout.add_widget(self.calcular_button)
       #RESULTADO
       self.resultado_label = Label(text="Resultado:")
       self.layout.add_widget(self.resultado_label)
       # BOTON REGRESAR
       self.regresar_button = Button(text="REGRESAR AL MENÚ PRINCIPAL")
       self.regresar_button.bind(on_press=self.regresar_al_menu_principal)
       self.layout.add_widget(self.regresar_button)
    def calcular_tonelaje_pulpa(self, instance):
        try:
            tonelaje = float(self.tonelaje_input.text)
            porcentaje_solidos = float(self.porcentaje_solidos_input.text)
            tonelaje_pulpa = 100 * (tonelaje / porcentaje_solidos)
            self.resultado_label.text = f"Resultado: Tonelaje de pulpa = {tonelaje_pulpa:.2f} TPH"
        except ValueError:
            self.resultado_label.text = "Ingrese valores numéricos válidos."
        except ZeroDivisionError:
            self.resultado_label.text = "El porcentaje de sólidos no puede ser 0."
    def regresar_al_menu_principal(self, instance):
        self.layout.clear_widgets()

        titulo = Label(
            text="METALCALC",
            font_size=25
        )

        self.layout.add_widget(titulo)

        boton_dilucion = Button(text="DILUCIÓN")
        boton_dilucion.bind(on_press=self.dilucion)

        boton_solidos = Button(text="PORCENTAJE DE SÓLIDOS")
        boton_solidos.bind(on_press=self.porcentaje_solidos)

        boton_tonelaje = Button(text="TONELAJE DE PULPA")
        boton_tonelaje.bind(on_press=self.tonelaje_pulpa)

        boton_caudal = Button(text="CAUDAL DE PULPA")
        boton_caudal.bind(on_press=self.caudal_pulpa)

        boton_densidad_pulpa = Button(text="DENSIDAD DE PULPA")
        boton_densidad_pulpa.bind(on_press=self.densidad_pulpa)

        boton_densidad_mineral = Button(text="DENSIDAD DE MINERAL")
        boton_densidad_mineral.bind(on_press=self.densidad_mineral)

        
        boton_salir = Button(text="SALIR")
        boton_salir.bind(on_press=self.salir)

        self.layout.add_widget(boton_dilucion)
        self.layout.add_widget(boton_solidos)
        self.layout.add_widget(boton_tonelaje)
        self.layout.add_widget(boton_caudal)
        self.layout.add_widget(boton_densidad_pulpa)
        self.layout.add_widget(boton_densidad_mineral)
        self.layout.add_widget(boton_salir)

#............................................................
# CODIGO DE CAUDAL DE PULPA
#------------------------------------------------

    def caudal_pulpa(self, instance):
        self.layout.clear_widgets()  # LIMPIAR PANTALLA
        # TITULO
        titulo = Label(
            text="CAUDAL DE PULPA",
            font_size=25
        )
        self.layout.add_widget(titulo)
        # AGREGAR ENTRADA DE TONELAJE
        self.layout.add_widget(Label(text="TONELAJE DE PULPA (TPH)"))
        self.tonelaje_pulpa_input = TextInput(hint_text="Ingrese el tonelaje de pulpa", input_filter='float', multiline=False)
        self.layout.add_widget(self.tonelaje_pulpa_input)
        # AGREGAMOS  ENTRADA DE PORCENTAJE DE SOLIDOS
        self.layout.add_widget(Label(text="PORCENTAJE DE SÓLIDOS (%S)"))
        self.porcentaje_solidos_input = TextInput(hint_text="Ingrese el porcentaje de sólidos", input_filter='float', multiline=False)
        self.layout.add_widget(self.porcentaje_solidos_input)
        # AGREGAMOS  ENTRADA DE DENSIDAD DEL MINERAL
        self.layout.add_widget(Label(text="DENSIDAD DEL MINERAL (g/cm³)"))
        self.densidad_mineral_input = TextInput(hint_text="Ingrese la densidad del mineral", input_filter='float', multiline=False)
        self.layout.add_widget(self.densidad_mineral_input)
        # BOTON CALCULAR
        self.calcular_button = Button(text="CALCULAR CAUDAL DE PULPA")
        self.calcular_button.bind(on_press=self.calcular_caudal_pulpa)
        self.layout.add_widget(self.calcular_button)
        # RESULTADO
        self.resultado_label = Label(text="Resultado:")
        self.layout.add_widget(self.resultado_label)
        # BOTON REGRESAR
        self.regresar_button = Button(text="REGRESAR AL MENÚ PRINCIPAL")
        self.regresar_button.bind(on_press=self.regresar_al_menu_principal)
        self.layout.add_widget(self.regresar_button)
    def calcular_caudal_pulpa(self, instance):
        try:
            tonelaje_pulpa = float(self.tonelaje_pulpa_input.text)
            porcentaje_solidos = float(self.porcentaje_solidos_input.text)
            densidad_mineral = float(self.densidad_mineral_input.text)
            caudal_pulpa = tonelaje_pulpa / densidad_mineral + tonelaje_pulpa * (100 - porcentaje_solidos) / porcentaje_solidos
            self.resultado_label.text = f"Resultado: Caudal de pulpa = {caudal_pulpa:.2f} m³/h"
        except ValueError:
            self.resultado_label.text = "Ingrese valores numéricos válidos."
        except ZeroDivisionError:
            self.resultado_label.text = "El porcentaje de sólidos no puede ser 0."
    def regresar_al_menu_principal(self, instance):
        self.layout.clear_widgets()

        titulo = Label(
            text="METALCALC",
            font_size=25
        )

        self.layout.add_widget(titulo)

        boton_dilucion = Button(text="DILUCIÓN")
        boton_dilucion.bind(on_press=self.dilucion)

        boton_solidos = Button(text="PORCENTAJE DE SÓLIDOS")
        boton_solidos.bind(on_press=self.porcentaje_solidos)

        boton_tonelaje = Button(text="TONELAJE DE PULPA")
        boton_tonelaje.bind(on_press=self.tonelaje_pulpa)

        boton_caudal = Button(text="CAUDAL DE PULPA")
        boton_caudal.bind(on_press=self.caudal_pulpa)

        boton_densidad_pulpa = Button(text="DENSIDAD DE PULPA")
        boton_densidad_pulpa.bind(on_press=self.densidad_pulpa)

        boton_densidad_mineral = Button(text="DENSIDAD DE MINERAL")
        boton_densidad_mineral.bind(on_press=self.densidad_mineral)

        
        boton_salir = Button(text="SALIR")
        boton_salir.bind(on_press=self.salir)

        self.layout.add_widget(boton_dilucion)
        self.layout.add_widget(boton_solidos)
        self.layout.add_widget(boton_tonelaje)
        self.layout.add_widget(boton_caudal)
        self.layout.add_widget(boton_densidad_pulpa)
        self.layout.add_widget(boton_densidad_mineral)
        self.layout.add_widget(boton_salir)
    #............................................................
    # CODIGO DE DENSIDAD DE PULPA
    #------------------------------------------------

    def densidad_pulpa(self, instance):
        self.layout.clear_widgets()  # LIMPIAR PANTALLA
        # TITULO
        titulo = Label(
            text="DENSIDAD DE PULPA",
            font_size=25
        )
        self.layout.add_widget(titulo)
        # AGREGAR ENTRADA DE TONELAJE DE PULPA
        self.layout.add_widget(Label(text="TONELAJE DE PULPA (TPH):"))
        self.tonelaje_pulpa_input = TextInput(hint_text="Ingrese el tonelaje de pulpa", input_filter='float', multiline=False)
        self.layout.add_widget(self.tonelaje_pulpa_input)
        # AGREGAR ENTRADA DE VOLUMEN DE PULPA
        self.layout.add_widget(Label(text="VOLUMEN DE PULPA (m³):"))
        self.volumen_pulpa_input = TextInput(hint_text="Ingrese el volumen de pulpa", input_filter='float', multiline=False)
        self.layout.add_widget(self.volumen_pulpa_input)
        # BOTON CALCULAR
        self.calcular_button = Button(text="CALCULAR DENSIDAD DE PULPA")
        self.calcular_button.bind(on_press=self.calcular_densidad_pulpa)
        self.layout.add_widget(self.calcular_button)
        # RESULTADO
        self.resultado_label = Label(text="Resultado:")
        self.layout.add_widget(self.resultado_label)
        # BOTON REGRESAR
        self.regresar_button = Button(text="REGRESAR AL MENÚ PRINCIPAL")
        self.regresar_button.bind(on_press=self.regresar_al_menu_principal)
        self.layout.add_widget(self.regresar_button)
    def calcular_densidad_pulpa(self, instance):
        try:
            tonelaje_pulpa = float(self.tonelaje_pulpa_input.text)
            volumen_pulpa = float(self.volumen_pulpa_input.text)
            densidad_pulpa = tonelaje_pulpa / volumen_pulpa
            self.resultado_label.text = f"Resultado: Densidad de pulpa = {densidad_pulpa:.2f} g/cm³"
        except ValueError:
            self.resultado_label.text = "Ingrese valores numéricos válidos."
        except ZeroDivisionError:
            self.resultado_label.text = "El volumen de pulpa no puede ser 0."
    def regresar_al_menu_principal(self, instance):
        self.layout.clear_widgets()

        titulo = Label(
            text="METALCALC",
            font_size=25
        )

        self.layout.add_widget(titulo)

        boton_dilucion = Button(text="DILUCIÓN")
        boton_dilucion.bind(on_press=self.dilucion)

        boton_solidos = Button(text="PORCENTAJE DE SÓLIDOS")
        boton_solidos.bind(on_press=self.porcentaje_solidos)

        boton_tonelaje = Button(text="TONELAJE DE PULPA")
        boton_tonelaje.bind(on_press=self.tonelaje_pulpa)

        boton_caudal = Button(text="CAUDAL DE PULPA")
        boton_caudal.bind(on_press=self.caudal_pulpa)

        boton_densidad_pulpa = Button(text="DENSIDAD DE PULPA")
        boton_densidad_pulpa.bind(on_press=self.densidad_pulpa)

        boton_densidad_mineral = Button(text="DENSIDAD DE MINERAL")
        boton_densidad_mineral.bind(on_press=self.densidad_mineral)

        

        boton_salir = Button(text="SALIR")
        boton_salir.bind(on_press=self.salir)

        self.layout.add_widget(boton_dilucion)
        self.layout.add_widget(boton_solidos)
        self.layout.add_widget(boton_tonelaje)
        self.layout.add_widget(boton_caudal)
        self.layout.add_widget(boton_densidad_pulpa)
        self.layout.add_widget(boton_densidad_mineral)
        self.layout.add_widget(boton_salir)

    def densidad_mineral(self, instance):
        self.layout.clear_widgets()  # LIMPIAR PANTALLA
        # TITULO
        titulo = Label(
            text="DENSIDAD DE MINERAL (MÉTODO DE PICNÓMETRO)",
            font_size=25
        )
        self.layout.add_widget(titulo)
        # AGREGAR ENTRADA DE MASA DEL PICNÓMETRO VACÍO
        self.layout.add_widget(Label(text="PESO DEL PICNÓMETRO VACÍO"))
        self.masa_picnometro_vacio = TextInput(hint_text="Ingrese peso del picnómetro vacío (g)", input_filter='float', multiline=False)
        self.layout.add_widget(self.masa_picnometro_vacio)
        # AGREGAR ENTRADA DE MASA DEL PICNÓMETRO CON MINERAL SECO
        self.layout.add_widget(Label(text="PESO DEL PICNÓMETRO CON MINERAL SECO"))
        self.masa_picnometro_mineral_seco = TextInput(hint_text="Ingrese peso del picnómetro con mineral seco (g)", input_filter='float', multiline=False)
        self.layout.add_widget(self.masa_picnometro_mineral_seco)
        # AGREGAR ENTRADA DE MASA DEL PICNÓMETRO CON MINERAL Y AGUA
        self.layout.add_widget(Label(text="PESO DEL PICNÓMETRO CON MINERAL Y AGUA"))
        self.masa_picnometro_mineral_agua = TextInput(hint_text="Ingrese peso del picnómetro con mineral y agua (g)", input_filter='float', multiline=False)
        self.layout.add_widget(self.masa_picnometro_mineral_agua)
        # AGREGAR ENTRADA DE MASA DEL PICNÓMETRO CON AGUA
        self.layout.add_widget(Label(text="PESO DEL PICNÓMETRO CON AGUA"))
        self.masa_picnometro_agua = TextInput(hint_text="Ingrese peso del picnómetro con agua (g)", input_filter='float', multiline=False)
        self.layout.add_widget(self.masa_picnometro_agua)
        # BOTON CALCULAR
        self.calcular_button = Button(text="CALCULAR DENSIDAD DE MINERAL")
        self.calcular_button.bind(on_press=self.calcular_densidad_mineral)
        self.layout.add_widget(self.calcular_button)
        # RESULTADO
        self.resultado_label = Label(text="Resultado:")
        self.layout.add_widget(self.resultado_label)
        # BOTON REGRESAR
        self.regresar_button = Button(text="REGRESAR AL MENÚ PRINCIPAL")
        self.regresar_button.bind(on_press=self.regresar_al_menu_principal)
        self.layout.add_widget(self.regresar_button)
    def calcular_densidad_mineral(self, instance):
        try:
            m1 = float(self.masa_picnometro_vacio.text)
            m2 = float(self.masa_picnometro_mineral_seco.text)
            m3 = float(self.masa_picnometro_mineral_agua.text)
            m4 = float(self.masa_picnometro_agua.text)

            densidad_mineral = (m2 - m1) / ((m4 - m1) - (m3 - m2))
            self.resultado_label.text = f"Resultado: Densidad del mineral = {densidad_mineral:.2f} g/cm³"
        except ValueError:
            self.resultado_label.text = "Ingrese valores numéricos válidos."
        except ZeroDivisionError:
            self.resultado_label.text = "Error en el cálculo, verifique los datos ingresados."
    def regresar_al_menu_principal(self, instance):
        self.layout.clear_widgets()

        titulo = Label(
            text="CALCULADORA METALÚRGICA",
            font_size=25
        )

        self.layout.add_widget(titulo)

        boton_dilucion = Button(text="DILUCIÓN")
        boton_dilucion.bind(on_press=self.dilucion)

        boton_solidos = Button(text="PORCENTAJE DE SÓLIDOS")
        boton_solidos.bind(on_press=self.porcentaje_solidos)

        boton_tonelaje = Button(text="TONELAJE DE PULPA")
        boton_tonelaje.bind(on_press=self.tonelaje_pulpa)

        boton_caudal = Button(text="CAUDAL DE PULPA")
        boton_caudal.bind(on_press=self.caudal_pulpa)

        boton_densidad_pulpa = Button(text="DENSIDAD DE PULPA")
        boton_densidad_pulpa.bind(on_press=self.densidad_pulpa)

        boton_densidad_mineral = Button(text="DENSIDAD DE MINERAL")
        boton_densidad_mineral.bind(on_press=self.densidad_mineral)

        
        boton_salir = Button(text="SALIR")
        boton_salir.bind(on_press=self.salir)

        self.layout.add_widget(boton_dilucion)
        self.layout.add_widget(boton_solidos)
        self.layout.add_widget(boton_tonelaje)
        self.layout.add_widget(boton_caudal)
        self.layout.add_widget(boton_densidad_pulpa)
        self.layout.add_widget(boton_densidad_mineral)
        self.layout.add_widget(boton_salir)
    
   
    # ==========================================
    # SALIR
    # ==========================================

    def salir(self, instance):
        App.get_running_app().stop()


CalculadoraMetalurgica().run()