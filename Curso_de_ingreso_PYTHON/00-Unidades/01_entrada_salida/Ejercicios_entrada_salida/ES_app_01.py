import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        # edad = 34 | variable del tipo entero
        # pep8: no se debe usar el + para concatenar strings
        # snake_case: nombre de variable
        # promedio_edad_jugadores_futbol = 23.3 | variable del tipo float

        nombre = "Juan" # variable del tipo string
        # apellido = None | variable del tipo None
        print(nombre)
        nombre = 11 # variable del tipo entero
        #titulo = "Hola"
        #mensaje = "estp es un mensaje"
        #alert(titulo, mensaje)

        respuesta_usuario = question("Esto es una pregunta")
        print(respuesta_usuario)
        nombre_ingresado = prompt("Ingrese su nombre", "nombre")
        print(nombre_ingresado)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
