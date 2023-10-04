import tkinter as tk

constante1,constante2,constante3,constante4, constante5, constante6 = 0,0,0,0,0,0
# Función para manejar el cierre de la ventana
def cerrar_ventana():
    global constante1, constante2, constante3, constante4, constante5, constante6
    constante1 = float(entry_constante1.get())
    constante2 = float(entry_constante2.get())
    constante3 = float(entry_constante3.get())
    constante4 = float(entry_constante4.get())
    constante5 = float(entry_constante5.get())
    constante6 = float(entry_constante6.get())
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.geometry("800x600")
root.title("Ingresar Constantes")

# Crear etiquetas y campos de entrada para las constantes
tk.Label(root, text="PosX - Bola 0:").pack()
entry_constante1 = tk.Entry(root)
entry_constante1.pack()

tk.Label(root, text="PosY - Bola 0:").pack()
entry_constante2 = tk.Entry(root)
entry_constante2.pack()

tk.Label(root, text="PosX - Bola 1:").pack()
entry_constante3 = tk.Entry(root)
entry_constante3.pack()

tk.Label(root, text="PosY - Bola 1:").pack()
entry_constante4 = tk.Entry(root)
entry_constante4.pack()

tk.Label(root, text="Carga (C) - Bola 0:").pack()
entry_constante5 = tk.Entry(root)
entry_constante5.pack()

tk.Label(root, text="Carga (C) - Bola 1:").pack()
entry_constante6 = tk.Entry(root)
entry_constante6.pack()


# Botón para cerrar la ventana y almacenar las constantes
btn_cerrar = tk.Button(root, text="Guardar posiciones", command=cerrar_ventana)
btn_cerrar.pack()

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()