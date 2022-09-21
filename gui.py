from statistics import variance
import tkinter
from tkinter import Canvas, Scale, Variable, messagebox, ttk, DoubleVar, StringVar
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from fourier import Fourier

 

 

def main ():
    """This method launch the grafical user interface"""
    root = tkinter.Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None


class Window:
    """Clase que muestra la ventana principal de mi GUI"""
    def __init__(self, root):
      self.root = root 
      self.root.title("Tarea Fourier")
      self.root.geometry('1300x800')
      self.num_aprox_serie =  DoubleVar()
      self.name_function =  StringVar(value="Escalon")
      self.error_function_name = StringVar(value="Error Porcentual")
      self.name_aprox_function =  StringVar(value="Seno")
      self.eq_expression =  StringVar(value="|x|/x")
    

      
      tkinter.Label(self.root, text= "Complemento de matemática \nEspecializacion en Optoelectronica \n Universidad de Buenos Aires").grid(row=1, column=0, columnspan=6, padx=5, pady=5)
      tkinter.Label(self.root, text=  "Rafael Santiago Campo Serrano").grid(row=2, column=0, columnspan=6, padx=5, pady=5)
      self.label_coef = tkinter.Label(self.root,text="Número de coeficientes de expansion")
       
      #tkinter.Entry(self.root,bg='black',fg='white',bd=5).grid(row=3, column=1,  padx=5, pady=5)

      self.escala=tkinter.Scale(self.root,
                                from_=1,
                                to=51,
                                tickinterval=5,
                                length=800,
                                orient= tkinter.HORIZONTAL,  
                                variable=self.num_aprox_serie
                                )
      self.button_run = tkinter.Button( self.root,
                                        text="Correr aproximación",
                                        command=self.update_value, 

      )

      self.label_function_type= tkinter.Label(self.root,
                                              text="Escoja el tipo de grafica"
                                              )


      self.function_menu = ttk.Combobox(self.root,
                                        state="readonly",
                                        values=["Escalon","Periodica senos y cosenos","Triangulo"], 
                                        textvariable=self.name_function, 
                                        width= 40
                                        )

      self.button_funct=tkinter.Button(self.root,
                                       text="Actualizar grafico", 
                                       command=self.update_function
                                       )

      self.label_error_type= tkinter.Label(self.root,
                                              text="Escoja el tipo de error"
                                              )


      self.funct_error_menu = ttk.Combobox(self.root,
                                        state="readonly",
                                        values=["Error Porcentual","Error porcentual absoluto"], 
                                        textvariable=self.error_function_name, 
                                        width= 40
                                        )

      self.button_error_funct=tkinter.Button(self.root,
                                       text="Actualizar grafico", 
                                       command=self.update_error_function
      )
      
      self.button_qa=tkinter.Button(bitmap="question", 
                                    command=self.information_popup
                                    )
      
      self.eq_label=tkinter.Label(self.root, 
                                  textvariable=self.eq_expression, 
                                  text= f"La ecuacion es: {self.eq_expression}"
                                  )
                   

     
      ##Definig the position in the grid of every widgets

      self.label_coef=self.label_coef.grid(row=3, column=0, sticky=tkinter.W,  padx=5, pady=5)
      self.escala = self.escala.grid(row=3, column=1,columnspan=4,  padx=5, pady=5, sticky=tkinter.W)
      self.button_run = self.button_run.grid(row=3, column=5)

      self.label_function_type= self.label_function_type.grid(row=4, column=0, sticky=tkinter.W,  padx=5, pady=5)
      self.function_menu=self.function_menu.grid(row=4, column=1, columnspan=1, sticky=tkinter.W)
      self.button_funct=self.button_funct.grid(row=4,column=2,  padx=5, pady=5, sticky=tkinter.W)

      self.label_error_type = self.label_error_type.grid(row=4, column = 3)
      self.funct_error_menu = self.funct_error_menu.grid(row=4, column=4)
      self.button_error_funct = self.button_error_funct.grid(row=4, column=5)

      self.button_qa=self.button_qa.grid(row=5,column=0, sticky=tkinter.W)
      self.eq_label = self.eq_label.grid(row=7, column=0)
      self.plot_values()

      return None


## TODO: this piece of code run many times the same plot its necesary to re make for just update one plot

    def update_value(self):
      self.fig_error.clear()
      self.fig_fourier.clear()
      self.plot_aprox_fourier()
      self.plot_values()
      
      print(self.num_aprox_serie.get()) 

    def update_function(self):
      self.plot_func()
      self.plot_values()
      print(f" {self.eq_expression.get()}" )
      print(f" {self.name_function.get()}" )
    
    def update_error_function(self):
      self.plot_error()
      self.plot_values()
    

       
    def information_popup(self):
      return messagebox.showinfo(title="Saludos",message=f"Hola \nEsta es la tarea numero 2 de complementos de matematicas, por favor clickea en 'Aceptar' para continuar " )


    def info_num_aprox(self):
      return messagebox.showinfo(title="Alerta",message=f"Hola \nCuando se emplea un numero de xpansiones de la serie mayor a 15, el tiempo de ejecución es largo. \n Por favor, de click en 'aceptar' y espera un minuto." )

        
    def plot_aprox_fourier(self ):
      f  = Fourier()
      variable = int(self.num_aprox_serie.get())
      if variable >= 15:
        self.info_num_aprox()

      f = f.fourier_escalon(variable)
      t = f[0]
      s = f[1]
      fig = plt.plot(t,s)
      return fig
      


    def plot_func(self):

      "Return a list of elements to be ploted"
      variable =  self.name_function.get()

      print(f"La variable cambiada es: {variable}" )
      if variable == "Escalon":
        self.plot_square_func()
        print(f"Funcion ploteada escalon")

      elif variable == "Triangulo":
        self.plot_triangle_func()
        print(f"Funcion ploteada triangulo")

      else:
        self.plot_square_func()
        print(f"Funcion ploteada por defaulf")


 
    def plot_square_func(self):
      f = Fourier()
      f=f.function_square_pulse()
      t = f[0]
      s = f[1]
      fig = plt.plot(t,s)
      return fig


    def plot_triangle_func(self):
      f = Fourier()
      t = f.function_triangle_pulse()[0]
      s = f.function_triangle_pulse()[1]
      fig = plt.plot(t,s)
      return fig
 
    def plot_error(self ):
       f = Fourier()
       abs_error = self.error_function_name.get()
       if abs_error == "Error Porcentual":
        abs_error = False
       else:
        abs_error = True

       num_exp = int(self.num_aprox_serie.get()) 
       f=f.error_function(num_exp,abs_error=abs_error)
       t = f[0]
       s = f[1]
       fig = plt.plot(t,s)
       return fig

       

       

    def plot_values(self):

        self.fig_fourier, ax = plt.subplots()
        plt.grid()
        self.plot_func()
        self.plot_aprox_fourier()

        
        

        canvas_fourier = FigureCanvasTkAgg(self.fig_fourier, self.root)
        canvas_fourier.draw()
        canvas_fourier.get_tk_widget().grid(row=6, column= 0,columnspan=3, sticky=tkinter.W )


        self.fig_error, ax = plt.subplots()
        
        self.plot_error()
         
        canvas_fourier = FigureCanvasTkAgg(self.fig_error, self.root)
        canvas_fourier.draw()
        canvas_fourier.get_tk_widget().grid(row=6, column=3,columnspan=3, sticky=tkinter.E )

        ##To do: Necesito hacer que esta funcion sea mas simple. se puede usar un unico canvas y en lugar de eso plotearlo por aparte 
        return canvas_fourier


main()