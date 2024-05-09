from tkinter import ttk
import tkinter as tk
from tkinter import LabelFrame, filedialog
from data_cleaning.data_operator import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import messagebox as MessageBox

fileMap = './data/newDaneMapFile.csv'
stateRoute = './data/colombia.geo.json'

def showDialog(message):
    MessageBox.showinfo("Ha ocurrido un error: ", message)

def load_csv_file(tableToInsert, tableToInsert2, labelToDraw):
    filepath = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])
    listValue = main_operations(filepath)
    insertValuesOnTable(listValue[0], tableToInsert)
    insertValuesOnTable(listValue[1], tableToInsert2)
    dataFrameCasesAll = listValue[2]
    dataFrameCasesLab = listValue[3]
    
    return filepath

def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def insertValuesOnTable(valueDictionary, tableToInsert):
    for clave, valor in valueDictionary.items():
        tableToInsert.insert("", "end", text=clave, values=(valor,))

def load_window():
    try:
        root = tk.Tk()
        contador = tk.IntVar()
        contador.set(0)
        root.geometry("1280x720")
        root.title("CSV File Loader")
        center_window(win=root)
        
        my_label = LabelFrame(root)
        my_label.pack(pady=20)
        
        # Crear un Treeview (tabla)
        tabla = ttk.Treeview(my_label, columns=("value"))
        tabla2 = ttk.Treeview(my_label, columns=("value"))

        # Configurar las columnas
        tabla.heading("#0", text="Campo")
        tabla.heading("value", text="Valor")
        
        etiqueta_casos_totales = tk.Label(my_label, text="Casos Totales",font=("Helvetica", 14, "bold"))
        
        button = tk.Button(my_label, text="Load CSV file", command=load_csv_file(tabla, tabla2, my_label))
        
        button.pack()
        

        # Configurar las columnas
        tabla2.heading("#0", text="Campo")
        tabla2.heading("value", text="Valor")
        
        etiqueta_casos_laboratorio = tk.Label(my_label, text="Casos Laboratorio",font=("Helvetica", 14, "bold"))
                                        
        # Mostrar la tabla
        etiqueta_casos_totales.pack()
        tabla.pack()

        etiqueta_casos_laboratorio.pack()
        tabla2.pack()
        
        root.mainloop()
    except Exception as e:
        showDialog(e)