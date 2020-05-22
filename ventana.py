from tkinter import*

raiz = Tk()

def vent_menu():
    raiz_menu =Tk()
    raiz_menu.geometry("850x550")
    menu_etiqueta1 = Label(raiz_menu,text="para empezar llena los datos siguientes")
    menu_etiqueta1.pack()
    nodos_caja = Entry(raiz_menu)
    nodos_caja.pack()
    nodos_boton = Button(raiz_menu,text="clik",padx=40,pady=10,bg="green")
    nodos_boton.pack()
    def nodoss():
        nodos = val_num(nodos_caja.get())


def val_num(num):
    try:
        num = int(num)
    except ValueError:
        print("error")
    return num   

# ventana inicial
raiz.geometry("800x500")
ini_etiqueta1 = Label(raiz,text="Teoria de graficas")
ini_etiqueta1.pack()
ini_etiqueta2 = Label(raiz, text = "preciona para comenzar")
ini_etiqueta2.pack()
ini_bot1 = Button(raiz,text="grafo",padx= 50,pady=20,bg = "green",command =vent_menu)
ini_bot1.pack()

raiz.mainloop()
