#Creditos: CodeWithCurious by Shivakshi Chouhan 
#tkinter se usa para crear GUI botones, labels, input etc
import tkinter as tk
#ttk  = treeview widget para ver la informacion en una tabla
#messagebox es apra mostrar mensajes pop-up
from tkinter import ttk, messagebox

#inicilaizar la vista general que tendra el proyecto
root = tk.Tk()
root.title("Seguimiento de Gastos!")
#tamanio y caracteristicas de la ventana
root.geometry("900x550")
root.config(bg="white")

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
    for fila in tree.get_children():
        tree.delete(fila)
    #Agrega el nuevo gasto a la tabla
    for i,(desc, cat, cant) in enumerate(gastos, start=1):
        tree.insert("", "end", values = (i, desc,cat, f"${cant:.2f}"))
    
    
def actualiza_total():
        #solo toma el campo de esta tupla
        total = sum(cant for _, _, cant in gastos)
        total_resultado.config(text=f"Total: ${total:.2f}")

    
    #Rellenar la label de la descripcion
tk.Label(root, text="Descripcion", bg="white").pack()
descripcion = tk.Entry(root, width=40)
descripcion.pack()        
    
    #Rellenar la label de la categoria
tk.Label(root, text="Categoria", bg="white").pack()
categoria = tk.Entry(root, width=40)
categoria.pack()
    
tk.Label(root, text="Cantidad ($)", bg="white").pack()
cantidad = tk.Entry(root, width=40)
cantidad.pack()


agregar_btn = tk.Button(root, text="Agregar Gastos", command=agregar_gastos, bg="#4CAF50", fg="white")
agregar_btn.pack(pady=10)
    
    
    #crear vista de como se ven los gastos
    #Crea una tabla con 4 columas con: numero, descripcion, categoria, cantidad 
columna = ("#", "Descripcion", "Categoria", "Cantidad")
tree = ttk.Treeview(root, columns=columna, show="headings")
    
for col in columna:
    tree.heading(col, text=col)
tree.pack(pady=10, fill="x")

    #muestra la cantidad total de los gastos
total_resultado = tk.Label(root, text="Total: $0.00", font=("Arial", 12, "bold"), bg="white", fg="green")
total_resultado.pack(pady=10)
    
#Este en loop la ventana
root.mainloop()