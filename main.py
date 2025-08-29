#Creditos: CodeWithCurious by Shivakshi Chouhan 
#tkinter se usa para crear GUI botones, labels, input etc
import tkinter as tk
#ttk  = treeview widget para ver la informacion en una tabla
#messagebox es apra mostrar mensajes pop-up
from tkinter import ttk, messagebox

#inicilaizar la vista general que tendra el proyecto
root = tk.Tk()
root.title("Seguimiento de Gastos!")

#agregar estilo
root.tk.call('source', 'forest-dark.tcl')
ttk.Style().theme_use('forest-dark')

#Hacer la app responsiva
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.columnconfigure(index=3, weight=1)

root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
root.rowconfigure(index=3, weight=1)


# Create a Frame for input widgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=4)
widgets_frame.columnconfigure(index=0, weight=1)


#lista de las categorias a elegir
#categorias del treeview (item_id)
#1 = comida
#2 = Gastos
#3 = Transporte
#4 = Ocio
#5 = Hormiga
combo_list = ["Comida", "Gastos", "Transporte", "Ocio", 'Gasto Hormiga']

#tamanio la ventana
root.geometry("850x500")

#lista de tuplas se modifica a la siguiente estructura para que sea treeview
#(padre, indice, item_id, texto,   valores)
#("",   "end",     1,   "parent, ("item 1", "Valor 1")")
#los siguientes elementos usan el 1 como padre

gastos_tree = [
    ("", "end", 1, "Comida",("","Descripcion", "Cantidad")),
    ("", "end", 2, "Gastos",("","Descripcion", "Cantidad")),
    ("", "end", 3, "Transporte",("","Descripcion", "Cantidad")),
    ("", "end", 4, "Ocio",("","Descripcion", "Cantidad")),
    ("", "end", 5, "Gasto Hormiga",("","Descripcion", "Cantidad")), 
          ]
#cada gasto esta formado por una descripcion, categoria y cantidad 



def agregar_gastos():
    
    desc = descripcion.get()
    cat = categoria.get()
    cant = cantidad.get()
    
    print(desc)
    print(cat)
    print(cant)
    #Valida que todos los campos esten
    if not desc or not cat or not cant:
        messagebox.showerror("Error de campos","Debe de completar todos los campos")
        return
    
    #valida que se ingrese un numero
    try:
        cant = float(cant)
    except ValueError:
        messagebox.showerror("Error de campos", "Debe de ingresar un numero")
        return
    
    #Agrega la lista de los gastos como una tupla
    #gastos_tree.append((desc,cat,cant))
    
    descripcion.delete(0, tk.END)
    categoria.delete(0, tk.END)
    cantidad.delete(0, tk.END)


input_frame = ttk.LabelFrame(root, text="Rellena los campos", padding=(20, 10))
input_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

descripcion = ttk.Entry(input_frame)
descripcion.insert(0, " ")
descripcion.grid(row=0, column=0, padx=3, pady=(0, 15), sticky="ew")

categoria = ttk.Combobox(input_frame, values=combo_list)
categoria.current(0)
categoria.grid(row=1, column=0, padx=5, pady=10,  sticky="ew")

cantidad = ttk.Entry(input_frame)
cantidad.insert(0, "0.0")
cantidad.grid(row=2, column=0, padx=5, pady=(0, 15), sticky="ew")

# Separator
separator = ttk.Separator(root)
separator.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="ew")

agregar_btn = ttk.Button(input_frame, text="Agregar", command=agregar_gastos)
agregar_btn.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")


#agregar_btn = tk.Button(root, text="Agregar Gastos", command=agregar_gastos, bg="#4CAF50", fg="white")
#agregar_btn.pack(pady=10)
        
#crear la tabla de como se ven los gastos
#Crea una tabla con 4 columas con: numero, descripcion, categoria, cantidad 
    
# Panedwindow
paned = ttk.PanedWindow(root)
paned.grid(row=0, column=2, pady=(35, 5), sticky="nsew", rowspan=2)

gastos_tabla = ttk.Frame(paned)
paned.add(gastos_tabla, weight=1)

treeFrame = ttk.Frame(gastos_tabla)
treeFrame.pack(expand=False, fill="both", padx=5, pady=5)

#columna = ("#", "Descripcion", "Categoria", "Cantidad")
#tree = ttk.Treeview(root, columns=columna, show="headings")
#permitir barra de scroll
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

#crear marco de la tabla
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2, 3,4), height=15)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)

#agregar columnas
treeview.column("#0",anchor="w", width=120)
treeview.column(1, width=50)
treeview.column(2, anchor="w", width=120)
treeview.column(3, anchor="w", width=120)
treeview.column(4, anchor="w", width=120)

#titulos de las columnas
treeview.heading("#0", text="Categoria", anchor="center")
treeview.heading(1, text="#", anchor="center")
treeview.heading(2, text="Descripcion", anchor="center")
treeview.heading(3, text="Cantidad", anchor="center")
treeview.heading(4, text="Total", anchor="center")

#mostrar de forma predeterminada el contenido del tree vacio
for item in gastos_tree:
    treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4])
    if item[0] == "" or item[2] in (8, 12):
       treeview.item(item[2], open=True) # Open parents



    #muestra la cantidad total de los gastos
#total_resultado = tk.Label(root, text="Total: $0.00", font=("Arial", 12, "bold"), bg="white", fg="green")
#total_resultado.pack(pady=10)
    
#exportar a excel la lista con el total 


    
#Este en loop la ventana
root.mainloop()