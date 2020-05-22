from tkinter import * 

ventana = Tk()
ventana.geometry("850x550")

def grafica():
    print("numero de vertices")
    vertices = val_num()
    print("numero de lineas")
    aristas = val_num()
    print("digita")
    print("  '1'  si es un grafo")
    print("  '2'  si es un di grafo")
    opcion = val_num()
    def grafo():
        print("grafo")
    def di_grafo():
        print("di_grafica")
    dict [
        1 : grafo,
        2 : di_grafo
    ]
    dict.get(opcion,grafica)()

def val_num():
    try:
        val = float(input("> "))
    except ValueError:
        print("valor erroneo")
        val_num()
    return val

def grafos():
    print()

menu_etiqueta = Label(ventana,text= "Teoria de graficas")
menu_etiqueta.pack()
menu_button1 = Button(ventana,text ="start",padx=50,pady=20,bg = "red", command=grafica )
menu_button1.pack(side = BOTTOM)

ventana.mainloop()


