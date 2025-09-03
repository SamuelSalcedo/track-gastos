#Creditos: CodeWithCurious by Shivakshi Chouhan 
#tkinter se usa para crear GUI botones, labels, input etc
import tkinter as tk
import json

#ttk  = treeview widget para ver la informacion en una tabla
#messagebox es apra mostrar mensajes pop-up
from tkinter import ttk, messagebox

#inicilaizar la vista general que tendra el proyecto
root = tk.Tk()
root.title("Seguimiento de Gastos!")

#agregar estilo
root.tk.call('source', 'forest-dark.tcl')
ttk.Style().theme_use('forest-dark')
root.option_add("*tearOff", False) # This is always a good idea

#Hacer la app responsiva

# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)


# Create a Frame for input widgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 15))
widgets_frame.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="nsew", rowspan=4)
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

#menos complejo para poder usar bien el json (tmabien yo que no lo entendia)
gastos_tree = {
    "Comida":[],
    "Gastos":[],
    "Transporte":[],
    "Ocio":[],
    "Gasto Hormiga":[]
}

#cada gasto esta formado por una descripcion, categoria y cantidad 
input_frame = ttk.LabelFrame(root, text="Rellena los campos", padding=(20, 10))
input_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

descripcion = ttk.Entry(input_frame)
descripcion.insert(0, " ")
descripcion.grid(row=0, column=0, padx=5, pady=15, sticky="w")

categoria = ttk.Combobox(input_frame, values=combo_list)
categoria.current(0)
categoria.grid(row=1, column=0, padx=(10,15), pady=5, sticky="e")
categoria.set("Comida")

cantidad = ttk.Entry(input_frame)
cantidad.insert(0, "0.0")
cantidad.grid(row=2, column=0, padx=5, pady=15, sticky="w")


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
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=("#","Categoria","Descipcion","Cantidad"), height=15)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)

#agregar columnas
treeview.column("#0", anchor="w", width=150)
treeview.column(0, anchor="w", width=10)
treeview.column(1, anchor="w", width=150)
treeview.column(2, anchor="w", width=70)
treeview.column(3, anchor="w", width=50)

#titulos de las columnas
treeview.heading("#0", text="Categoria", anchor="center")
treeview.heading(0, text="#", anchor="center")
treeview.heading(1, text="Descripcion", anchor="center")
treeview.heading(2, text="Cantidad", anchor="center")
treeview.heading(3, text="Total", anchor="center")

#mejorando logica de categorias
for cate in gastos_tree.keys():
    treeview.insert("", "end", iid=cate, text=cate.capitalize(), open=True)
    #agregar un total por cada categoria
treeview.insert("","end", iid="Total", text="Total", open=True)
    
    
total = 0
contador = 0
def agregar_gastos():
    #index para cada uno de los gastos

    global contador
    global total
    desc= descripcion.get()
    cat = categoria.get()
    cant = cantidad.get()
        
    #Valida que todos los campos esten

    if not desc or not cat or not cant:
        messagebox.showerror("Error de campos","Debe de completar todos los campos")
        return
    else:
            #valida que se ingrese un numero
        try:
            cant = float(cant)
            
        except ValueError:
            messagebox.showerror("Error de campos", "Debe de ingresar un numero")
            return
        contador += 1
        
        if cat:
            total += cant
            #agregar al diccionario
            gastos_tree[cat].append((contador,desc,cant))
            #agregar a la tabla
            treeview.insert(cat, "end", values=(contador, desc, cant))
            #ir sumando el valor de la cantidad solo cuando coincide la categoria
            #total = sum(item[2] for item in gastos_tree[cat])    
            
            treeview.item("Total", values=("","","Total:", total))
        else:
            messagebox.showerror("Error de campos", "Debe de estar en una categoria")
            return
    descripcion.delete(0, tk.END)
    cantidad.delete(0, tk.END)
    return total

#AUN NO PERSISTEN 
def guardar_datos():
    with open("gastos.json", "w") as f:
        json.dump(gastos_tree, f)
        
def cargar_datos():
    try:
        with open("gastos.json", "r") as f:
            gastos_tree =json.load(f)
            return gastos_tree
    
    except FileNotFoundError:
        messagebox.showerror("Error de archivo","No existen registros")
        return []  # si no existe, empieza vacío
    

        
#agregar una fila solo para ver el total de los gastos
#treeview.insert("", "end", iid="Total", text="Total", open=True)
#treeview.insert("Total","end", values=("","","Total:",total))


guardar_btn = ttk.Button(input_frame, text="Guardar datos", command=guardar_datos)
guardar_btn.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

#cargar_btn = ttk.Button(input_frame, text="Abrir ultimo registro", command= cargar_datos)
#cargar_btn.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

agregar_btn = ttk.Button(input_frame, text="Agregar", command=agregar_gastos)
agregar_btn.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

#Hacer que aparezca en el centro
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/4) - (root.winfo_width()/3))
y_cordinate = int((root.winfo_screenheight()/3) - (root.winfo_height()/4))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

#Este en loop la ventana
root.mainloop()