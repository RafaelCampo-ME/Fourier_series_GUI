import tkinter
from tkinter import Canvas, Scale, Variable, messagebox, ttk, DoubleVar, StringVar
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
      self.root.geometry('1300x1200')
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

      self.error_table = ttk.Treeview(self.root, 
                                      columns=['graph_type','n_aprox','avg_error'],
                                      
                                      show = "headings"
                                      )

      # define headings
      self.error_table.heading('graph_type', text='Tipo de funcion')
      self.error_table.heading('n_aprox', text='# Expansiones')
      self.error_table.heading('avg_error', text='Error promedio')

     
      ##Definig the position in the grid of every widgets

      print(f"Message: The GUI is starting. Please Wait \n")

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

      print("Message: We are ploting the graphs. Please Wait \n")

      self.plot_values()

      self.error_table.grid(row = 8, column=3, columnspan=3)
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
      print("Mesagge: We are updating the graphs \n")
      self.plot_error()
      self.plot_values()
      self.update_colum_values()
    

       
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
      
    def plot_aprox_fourier_general(self ):
      f  = Fourier()
      var_num_aprox = int(self.num_aprox_serie.get())
      var_func_name = self.name_function.get()
      if var_num_aprox >= 15:
        self.info_num_aprox()

      f = f.fourier_series_aprox(var_num_aprox,var_func_name)
      t = f[0]
      s = f[1]
      fig = plt.plot(t,s,'green', linewidth=1)
      return fig
      


    def plot_func(self):

      "Return a list of elements to be ploted"
      variable =  self.name_function.get()
      print(f"Message: The original function is going to be ploted. The function name is: {variable} \n")
 

      if variable == "Escalon":
        self.plot_square_func()
        print(f"Funcion ploteada escalon")

      elif variable == "Triangulo":
        self.plot_triangle_func()
        print(f"Funcion ploteada triangulo")

      elif variable == "Periodica senos y cosenos":
        self.plot_sin_random_func()
        print(f"Funcion ploteada es una combinacion random de senos y cosenos")

      else:
        self.plot_square_func()
        print(f"Funcion ploteada por defaulf")


 
    def plot_square_func(self):
      f = Fourier()
      f=f.function_square_pulse()
      t = f[0]
      s = f[1]
      fig = plt.plot(t,s,'r--',linewidth=1.5)
      print("Message: The square pulse function has been ploted.")
      return fig


    def plot_triangle_func(self):
      f = Fourier()
      f = f.function_triangle_pulse()
      t = f[0]
      s = f[1]
      fig = plt.plot(t,s,'r--',linewidth=1.5)
      print("Message: The triangle pulse function has been ploted")
      return fig

    def plot_sin_random_func(self):
      f = Fourier()
      f = f.function_cos_sin_random_pulse()
      t = f[0]
      s = f[1]
      fig = plt.plot(t,s,'r--',linewidth=1.5)
      print("Message: The sin and cos combination function has been ploted")
      return fig
    
    def update_colum_values(self):

      tipo_funcion = self.name_function.get()
      n_exp = self.num_aprox_serie.get()
      error = f"{self.avg_error()} %" 
      self.error_table.insert("", 'end', text= 1, values=(tipo_funcion,n_exp,error))
      print("Message: The error table has been updated")
      return "Valores actualizados"


 
    def plot_error(self ):
       f = Fourier()
       func_name_var = self.name_function.get()
       abs_error = self.error_function_name.get()
       if abs_error == "Error Porcentual":
        abs_error = False
       else:
        abs_error = True

       print(f"Message: The plot error function has started \nThe name of the error function is: {func_name_var}")

       num_exp = int(self.num_aprox_serie.get()) 
       f=f.error_function(num_exp,func_name=func_name_var, abs_error=abs_error)
       t = f[0]
       s = f[1]
       fig = plt.plot(t,s)
       return fig

    
    def avg_error(self ):
       f = Fourier()
       func_name_var = self.name_function.get()
       abs_error = self.error_function_name.get()
       if abs_error == "Error Porcentual":
        abs_error = False
       else:
        abs_error = True

       print(f"Message: The plot error function has started \nThe name of the error function is: {func_name_var}")

       num_exp = int(self.num_aprox_serie.get()) 
       f=f.error_function(num_exp,func_name=func_name_var, abs_error=abs_error)
       s = f[1]
 
       avg_error= (sum(s)/len(s))*100
         
       return avg_error

       

       

    def plot_values(self):

        self.fig_fourier, ax = plt.subplots()
        plt.grid()
        self.plot_func()
        #self.plot_aprox_fourier()
        self.plot_aprox_fourier_general()

        
        

        canvas_fourier = FigureCanvasTkAgg(self.fig_fourier, self.root)
        canvas_fourier.draw()
        canvas_fourier.get_tk_widget().grid(row=6, column= 0,columnspan=3, sticky=tkinter.W )


        self.fig_error, ax = plt.subplots()
        plt.grid()
        self.plot_error()
         
        canvas_fourier = FigureCanvasTkAgg(self.fig_error, self.root)
        canvas_fourier.draw()
        canvas_fourier.get_tk_widget().grid(row=6, column=3,columnspan=3, sticky=tkinter.E )
        return canvas_fourier


main()