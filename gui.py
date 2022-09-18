import tkinter
from tkinter import Canvas, Scale, messagebox, ttk, DoubleVar
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
    

      
      tkinter.Label(self.root, text= "Complemento de matemática \nEspecializacion en Optoelectronica \n Universidad de Buenos Aires").grid(row=1, column=0, columnspan=6, padx=5, pady=5)
      tkinter.Label(self.root, text=  "Rafael Santiago Campo Serrano").grid(row=2, column=0, columnspan=6, padx=5, pady=5)

      tkinter.Label(self.root,text="Número de coeficientes de expansion").grid(row=3, column=0, sticky=tkinter.W,  padx=5, pady=5)
       
      #tkinter.Entry(self.root,bg='black',fg='white',bd=5).grid(row=3, column=1,  padx=5, pady=5)
      self.escala=tkinter.Scale(self.root,from_=0, to=100,tickinterval=5,length=1000,
      orient= tkinter.HORIZONTAL,  command=self.update_value, variable=self.amplitud)
      self.escala = self.escala.grid(row=3, column=2,columnspan=5,  padx=5, pady=5)

      tkinter.Label(self.root,text="Número de coeficientes de expansion").grid(row=4, column=0, sticky=tkinter.W,  padx=5, pady=5)

      ttk.Combobox(
        state="readonly",
        values=["Escalon","Sierra","Triangulo"]
      ).grid(row=4, column=3, columnspan=2)

      tkinter.Button(self.root,text="Actualizar grafico").grid(row=4,column=5,  padx=5, pady=5)
      
      


      self.plot_values()
      
      ##messagebox.showinfo(title="Saludos",message="Hola \nEsta es la tarea numero 2 de complementos de matematicas, por favor clickea en 'Aceptar' para continuar" )

      return None

    def update_value(self,algo):
      self.fig_error.clear()
      self.fig_fourier.clear()
      self.plot_values()
      print(f"\n{algo} El nuervo valor de la amplitud es: {self.amplitud.get()} \n")
      print(self.amplitud.get()) 
       
       

        
    def plot_sin(self ):
      t = np.arange(-1*np.pi,np.pi,0.01) 
      s=  self.amplitud.get()*np.sin(t)
      plt.plot(t,s)
      

    def plot_func(self):
      t = np.arange(-1*np.pi,np.pi,0.01) 
      s=  (t/np.abs(t)) * self.amplitud.get()
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
        
        return canvas_fourier


main()