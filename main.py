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
combo_list = ["Comida", "Gastos", "Transporte", "Ocio", 'Gasto Hormiga']

#tamanio y caracteristicas de la ventana
root.geometry("1000x650")

#lista pricnipal para el seguimiento de costos
gastos = []
#cada gasto esta formado por una descripcion, categoria y cantidad 

#funcion para agregar nuevos gastos

def agregar_gastos():
    
    desc = descripcion.get()
    cat = categoria.get()
    cant = cantidad.get()
    
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
    gastos.append((desc,cat,cant))
    
    #Funciones helper para actualizar la tabla y el total
    actualiza_gastos()
    actualiza_total()
    
    descripcion.delete(0, tk.END)
    categoria.delete(0, tk.END)
    cantidad.delete(0, tk.END)

def actualiza_gastos():
    #borra la fila anterior
    for fila in treeview.get_children():
        treeview.delete(fila)
        
    #Agrega el nuevo gasto a la tabla
    for i,(desc, cat, cant) in enumerate(gastos, start=1):
        treeview.insert("", "end", values = (i, desc,cat, f"${cant:.2f}"))
    
    
def actualiza_total():
        print("Nuevo gasto")
        #solo toma el campo de esta tupla
        total = sum(cant for _, _, cant in gastos)
        total_resultado.config(text=f"Total: ${total:.2f}")

    
#hace run placeholder que se borra cuando el usuario haga clik

def on_focus_in(event):
    if descripcion.get() == placeholder:
            descripcion.delete(0, tk.END)

def on_focus_out(event):
    if not descripcion.get():
        descripcion.insert(0, placeholder)

placeholder = 'Descripcion'
descripcion = ttk.Entry(widgets_frame, )
descripcion.insert(0, placeholder)
descripcion.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

descripcion.bind("<FocusIn>", on_focus_in)
descripcion.bind("<FocusOut>", on_focus_out) 

categoria = ttk.Combobox(widgets_frame, values=combo_list)
categoria.current(0)
categoria.grid(row=1, column=0, padx=5, pady=10,  sticky="ew")

cantidad = ttk.Entry(widgets_frame)
cantidad.insert(0, "cantidad")
cantidad.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="ew")


agregar_btn = ttk.Button(widgets_frame, text="Agregar")
agregar_btn.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

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
treeview.column("#0", width=50)
treeview.column(1, anchor="w", width=120)
treeview.column(2, anchor="w", width=120)
treeview.column(3, anchor="w", width=120)
treeview.column(4, anchor="w", width=120)

#titulos de las columnas
treeview.heading("#0", text="#", anchor="center")
treeview.heading(1, text="Categoria", anchor="center")
treeview.heading(2, text="Descripcion", anchor="center")
treeview.heading(3, text="Cantidad", anchor="center")
treeview.heading(4, text="Total", anchor="center")


#Rellenar la tabla
#for col in columna:
 #   tree.heading(col, text=col)
#tree.pack(pady=10, fill="x")
# Insert treeview data
#for item in treeview:
 #   treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4])
#treeview.pack();

# Select and scroll
#treeview.selection_set(10)
#treeview.see(7)


    #muestra la cantidad total de los gastos
#total_resultado = tk.Label(root, text="Total: $0.00", font=("Arial", 12, "bold"), bg="white", fg="green")
#total_resultado.pack(pady=10)
    
#exportar a excel la lista con el total 


    
#Este en loop la ventana
root.mainloop()