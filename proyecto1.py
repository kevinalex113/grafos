from tkinter import ttk
from tkinter import *

#raiz
raiz = Tk()
#raiz.geometry("950x650")
raiz.config(bg= "#f3f1f1")
raiz.title("Graficas")
#frame
frame_p = Frame()
frame_ini = Frame()
#frame_gra = Frame()
frame_digra= Frame()
frame_gra_uni=Frame()
frame_clasification = Frame()

#variables
contad = 1
matriz_i=[]
matriz_ad=[]
nodos_ar=[]
#grados_nod=[]
nod_tot=1
num_nodos=int()
num_aristas=int()
textv=StringVar()
textv2=StringVar()

#-----------------------------------------portada--------------------------------------------------
def portada ():
    #frame_p = Frame()
    frame_p.pack(fill="both",expand="true") # hace que el frame se expanda junto conla raiz
    frame_p.config(bg="#7d7d7d") # da color al frame
    frame_p.config(width = "950",height = "650") # da tamaño inicial al frame


    etiqueta1 = Label(frame_p,text="Teoria de graficas",fg="#3e33ff",font=("ALGERIAN",30),bg="#7d7d7d").place(x=290,y=160)
    etiqueta2 = Label(frame_p,text="Alvarez cortes kevin Alejandro",bg="#7b7b7b",font=(13)).place(x=380,y= 250)
    etiqueta3 = Label(frame_p,text="Peñaloza Lopez Giovanni Antonio",bg="#7b7b7b",font=(13)).place(x=367,y= 280)

    start = Button(frame_p,text="Start",padx=40,pady=15,relief="groove",cursor="pencil",bg="blue",bd=10,activebackground="red",command= inicio).place(x=435,y=440)
#----------------------------------------menu inicio-------------------------------------------------    
def inicio():
    frame_p.destroy()
    frame_ini.pack()
    
    etiquetaini = Label(frame_ini,text="los campos y selecciona una opcion",fg="black",font=("CASTELLAR",15)).grid(row=0,column=1,pady=50)
    etiquetaini2 = Label(frame_ini,text="Completa",fg="black",font=("CASTELLAR",15)).grid(row=0,column=0,pady=50,padx=15,sticky="e")

    #---labels nodos 
    etiqueta1 = Label(frame_ini,text="No.Nodos:",fg="black",font=("Arial",14)).grid(row=2,column=0,sticky="e",pady=20,padx=35)
    nodos = Entry(frame_ini)
    nodos.grid(row=2,column=1,pady=20,padx=15,sticky="w")
    nodos.config(fg="blue",justify="center",font=("Arial",14))
    etiqueta_error =Label(frame_ini,textvar=textv,fg="#ff0000",font=("Arial",11)).grid(row=1,column=1,sticky="w",padx=15)
    #---labels aristas
    etiqueta2 = Label(frame_ini,text="No.Aristas:",fg="black",font=("Arial",14)).grid(row=4,column=0,sticky="e",pady=20,padx=35)
    aristas = Entry(frame_ini)
    aristas.grid(row=4,column=1,pady=20,padx=15,sticky="w")
    aristas.config(fg="blue",justify="center",font=("Arial",14))
    etiqueta2_error =Label(frame_ini,textvar=textv2,fg="#ff0000",font=("Arial",11)).grid(row=3,column=1,sticky="w",padx=15)
    etiqueta3 = Label(frame_ini,text="           ").grid(row=0,column=3)
    # ------- valida entrada menu principal
    def valida(op):
        global num_nodos
        if (not val_num(nodos.get()) or (int(nodos.get())<0)):
            textv.set("valor no valido")
        elif(not val_num(aristas.get()) or (int(aristas.get())<0) ):
            textv2.set("valor no valido")
        elif(op==1):
            num_nodos=int(nodos.get())
            num_aristas=int(aristas.get())
            matriz_adya()
            matriz_inci()
            grafo(num_aristas,num_nodos)
        else:
            num_nodos=int(nodos.get())
            num_aristas=int(aristas.get())
            matriz_adya()
            matriz_inci()
            digrafo(num_aristas,num_nodos)
    
    # --Botones
    but_digra = Button(frame_ini,text="GRAFO",padx=40,pady=15,relief="groove",cursor="pencil",bg="#00ff00",bd=10,activebackground="#0e4bef",command= lambda:valida(1)).grid(row=5,column=1,sticky="w",pady=70)
    but_nodigra = Button(frame_ini,text="DIGRAFO",padx=40,pady=15,relief="groove",cursor="pencil",bg="#e3ff00",bd=10,activebackground="red",command= lambda:valida(2)).grid(row=5,column=1,pady=70,padx=60,sticky="e")
    
#------------------------------------------grafo------------------------------------

def grafo(num_aristas,num_nodos):
    frame_ini.destroy()
    #frame_gra.pack()
    nodos_ar=[]
    text_error1=StringVar()
    text_error2=StringVar()
    
    def validacion(nodo,nodo2):
        cont = 0
        if(not val_num(nodo)):
            text_error1="Valor erroneo"
        elif (int(nodo) > num_nodos or int(nodo) < 1):
            text_error1="Nodo no existente"
        else:
            text_error1=" "
            nodo=int(nodo)
            cont+=1
            
        if(not val_num(nodo2)):
            text_error2="Valor erroneo"
        elif(int(nodo2) > num_nodos or int(nodo2) < 1):
            text_error2="Nodo no existente"
        else:
            text_error2=" "
            nodo2=int(nodo2)
            cont+=1
        
        if cont == 2:
            arreglo(nodo,nodo2)
            
         
        
    
    def arreglo(nodo,nodo2):
        global contad 
        arr_ord=[]
        global nod_tot
        nodos_ar.append([nodo,contad])
        nodos_ar.append([nodo2,contad])
        if (contad < num_aristas):
            contad+=1
            uniones()
        else:
            
            arr_ord=ordena(nodos_ar)
            for i in range(1,len(arr_ord)):
                if arr_ord[i-1][0] != arr_ord[i][0]:
                    nod_tot+=1
                    
            if nod_tot < num_nodos:
                nod_tot = num_nodos-nod_tot
            else:
                nod_tot = 0 
                 
            print(arr_ord)
            frame_gra_uni.destroy()
            clasificacion_gra(arr_ord,1)
            
            
    def uniones():
        global contad
        textv3= StringVar()
        textv3.set(str(contad))
        frame_gra_uni.pack()

        etiqueta_ini= Label(frame_gra_uni,text="nodos  en  los  que ",fg="black",font=("CASTELLAR",15)).grid(row=0,column=1,pady=45)
        etiqueta_ini2= Label(frame_gra_uni,text="Selecciona  los ",fg="black",font=("CASTELLAR",15)).grid(row=0,column=0,pady=45,padx=15,sticky="e")
        etiqueta_ini3= Label(frame_gra_uni,text="incide  la  linea indicada",fg="black",font=("CASTELLAR",15)).grid(row=0,column=3,pady=45,padx=15,sticky="w")
        
        Label(frame_gra_uni,text="NODO",fg="black",font=("CASTELLAR",12)).grid(row=1,column=0,pady=15)
        Label(frame_gra_uni,text="NODO",fg="black",font=("CASTELLAR",12)).grid(row=1,column=3,pady=15)
        error1=Label(frame_gra_uni,textvar=text_error1,fg="#ff0000",font=("Arial",11)).grid(row=2,column=0)
        error2=Label(frame_gra_uni,textvar=text_error2,fg="#ff0000",font=("Arial",11)).grid(row=2,column=3)
        
        nodo_iz= Entry(frame_gra_uni)
        nodo_iz.grid(row=3,column=0,padx= 35)
        nodo_iz.config(fg="blue",justify="center",font=("Arial",14))
        etiqueta_lin= Label(frame_gra_uni,text="linea: ").grid(row=3,column=1)
        etiqueta_lin_num= Label(frame_gra_uni,textvar= textv3,fg="black",font=("Arial",12)).grid(row=3,column=1,sticky="e",padx=80)
        nodo_der= Entry(frame_gra_uni)
        nodo_der.grid(row=3,column=3)
        nodo_der.config(fg="blue",justify="center",font=("Arial",14))
        
        bot_start=Button(frame_gra_uni,text="Insertar",padx=40,pady=15,relief="groove",cursor="spraycan",bg="#00ff00",bd=8,activebackground="#0e4bef",command= lambda:validacion(nodo_iz.get(),nodo_der.get())).grid(row=4,column=1,pady=50)
        
    
    uniones()
    
    #frame_gra.pack()
    

def digrafo():
    frame_ini.destroy()
    frame_digra.pack()
    print("temporalmente inhabil")
    
    for i in range(1,num_aristas+1):
        nodo_iz= Entry(frame_digra)
        nodo_iz.grid(row=i,column=0)

def val_num(a):
    val= True
    try:
        int(a)
    except ValueError:
        val= False
    return val

def ordena(arreglo):
    izquierda  = []
    derecha  = []
    centro  = []
    if  len(arreglo)> 1 :
        pivote = arreglo[0][0]
        for i in arreglo :
            if  i[0] < pivote :
                izquierda.append(i)
            elif  i[0] == pivote:
                centro.append(i)
            elif  i [0]> pivote :
                derecha.append(i)
        return  ordena(izquierda) + centro + ordena(derecha)
    else :
        return  arreglo
    
#-----------------clasificacion de graficas ---------------------------

def clasificacion_gra(arreglos,op):
    frame_clasification.pack()
    
    simp_or_gen = False
    con_or_desc= False
    regular=False
    completa=False
    simetrica=False
    balanceada=False
    verificadorBucle=0
    verificadorParalelas=0
    
    #---------------------------simple o general----------------------------------------
    for i in arreglos:
        for j in arreglos:
            if i == j:
                verificadorBucle+=1
            if i[1]==j[1] and i!=j:
                for k in arreglos:
                    for l in arreglos:
                        if k[1]== l[1]  and (k[0]==i[0] or k[0] == j[0]) and (l[0]== i[0] or l[0]== j[0]) and k!=l:
                            if (not (k[1]==i[1] or k[1] == j[1] )) and (not(l[1]==i[1] or l[1]== j[1])):
                                verificadorParalelas+=1
        if verificadorBucle > 1 or verificadorParalelas > 1 :
            simp_or_gen=True
        verificadorBucle=0
        verificadorParalelas=0
    
    # -------------------------------conectada o desconectada--------------
    
    if nod_tot> 0:
        con_or_desc= True
        
    #--------------------regular----------------------------------
    
    arr_grad_nod = grado_nodo(arreglos)
    print("grado", arr_grad_nod)
    if nod_tot == 0:        
        for i in arr_grad_nod:
            for j in arr_grad_nod:
                if i[1]!= [1]:
                    regular = True
    else:
        regular= True
    print("reg", regular)
    

def grado_nodo(arr_ord):
    global num_nodos
    arr_grad_nod=[]
    aux=0
    for i in range (1,num_nodos+1):
        for j in arr_ord:
            if j[0]== i:
                aux+=1
        arr_grad_nod.append([i,aux])
        aux=0
    return arr_grad_nod
    
def matriz_inci():
    global num_nodos
    global num_aristas
    global matriz_i
    for i in range(0,num_nodos):
        aux = []
        for j in range (0,num_aristas):
            aux.append(0)
        matriz_i.append(aux)

def matriz_adya():
    global num_nodos
    global matriz_ad
    for i in range (0,num_nodos):
        aux=[]
        for j in range (0, num_nodos):
            aux.append(0)
        matriz_ad.append(aux)
        
    
    

portada()



raiz.mainloop()