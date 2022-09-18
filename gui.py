import tkinter
from tkinter import Canvas, Scale, Variable, messagebox, ttk, DoubleVar, StringVar
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

 

 

def main ():
    """Esta funcion inicializa la interfaz"""
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
      self.amplitud =  DoubleVar()
      self.name_function =  StringVar(value="Escalon")
    

      
      tkinter.Label(self.root, text= "Complemento de matemática \nEspecializacion en Optoelectronica \n Universidad de Buenos Aires").grid(row=1, column=0, columnspan=6, padx=5, pady=5)
      tkinter.Label(self.root, text=  "Rafael Santiago Campo Serrano").grid(row=2, column=0, columnspan=6, padx=5, pady=5)
      self.label_coef = tkinter.Label(self.root,text="Número de coeficientes de expansion")
       
      #tkinter.Entry(self.root,bg='black',fg='white',bd=5).grid(row=3, column=1,  padx=5, pady=5)

      self.escala=tkinter.Scale(self.root,
                                from_=1,
                                to=101,
                                tickinterval=5,
                                length=1000,
                                orient= tkinter.HORIZONTAL,  
                                command=self.update_value, 
                                variable=self.amplitud
                                )

      self.label_function_type= tkinter.Label(self.root,text="Escoja el tipo de grafica")

      self.function_menu = ttk.Combobox(self.root,
                                        state="readonly",
                                        values=["Escalon","Sierra","Triangulo"], 
                                        textvariable=self.name_function, 
                                        width= 40
      )
      self.button=tkinter.Button(self.root,text="Actualizar grafico", command=self.update_function)
      self.button_qa=tkinter.Button(bitmap="question", command=self.information_popup)

     
      ##Definig the position in the grid of every widgets
      self.label_coef=self.label_coef.grid(row=3, column=0, sticky=tkinter.W,  padx=5, pady=5)
      self.escala = self.escala.grid(row=3, column=1,columnspan=5,  padx=5, pady=5)
      

      self.label_function_type= self.label_function_type.grid(row=4, column=0, sticky=tkinter.W,  padx=5, pady=5)
      self.function_menu=self.function_menu.grid(row=4, column=1, columnspan=2, sticky=tkinter.W)

      self.button=self.button.grid(row=4,column=3,  padx=5, pady=5, sticky=tkinter.W)

      self.button_qa=self.button_qa.grid(row=4,column=5, sticky=tkinter.W)
      


      self.plot_values()
      
      
      return None

    def update_value(self,algo):
      self.fig_error.clear()
      self.fig_fourier.clear()
      self.plot_values()
      
      print(f"\n{algo} El nuervo valor de la amplitud es: {self.amplitud.get()} \n")
      print(self.amplitud.get()) 

    def update_function(self ):
      print(f" {self.name_function.get()}" )
       
    def information_popup(self):
      return messagebox.showinfo(title="Saludos",message=f"Hola \nEsta es la tarea numero 2 de complementos de matematicas, por favor clickea en 'Aceptar' para continuar " )


        
    def plot_sin(self ):
      t = np.arange(-1*np.pi,np.pi,0.01) 
      s=  self.amplitud.get()*np.sin(t)
      plt.plot(t,s)
      

    def plot_func(self):
      t = np.arange(-1*np.pi,np.pi,0.01) 
      s=  (t/np.abs(t)) 
      plt.plot(t,s)

    def plot_error(self ):
      t = np.arange(-1*np.pi,np.pi,0.01) 
      s=  (t/np.abs(t)) * self.amplitud.get()
      plt.plot(t,s)

       

       

    def plot_values(self):

        self.fig_fourier, ax = plt.subplots()
        self.plot_sin()
        self.plot_func()

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