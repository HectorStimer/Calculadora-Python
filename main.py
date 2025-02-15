from tkinter import * 
from tkinter import ttk 

#cores que vou usar
cor1= "#181a18"  #preto
cor2 = '#ffffff' #branco 
cor3="#003366" #azul
cor4= "#dedede" #cinza
cor5= "#ffa500" #laranja



#treco pra definir a janela
janela = Tk ()
janela.title('Calculadora')
janela.geometry("470x550")
janela.config(bg="#181a18")  #tela cor preta


frame_tela = Frame(janela, width=470, height= 100, bg= "#003366" ) 
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=470, height= 536) 
frame_corpo.grid(row=1, column=0)


todos_valores= ''



def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    #passando valor pra tela
    valor_texto.set(todos_valores)

def calcular():
    resultado = eval(todos_valores)
    valor_texto.set(resultado)

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')
    

#criando label
valor_texto = StringVar()
app_label= Label(frame_tela, textvariable=valor_texto, width= 38, height=4, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 15 bold'), bg= "#1c2842", fg=cor2)
app_label.place(x=0,y=0)

#definindo botoes
b_1= Button(frame_corpo, command=limpar_tela,text= "C", width= 23, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_1.place(x=0,y=0)
b_2= Button(frame_corpo, command=lambda: entrar_valores('%'), text= "%", width= 11, height=4, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x= 240,y=0)
b_3= Button(frame_corpo, command=lambda: entrar_valores('/'),text= "/", width= 11, height=4, bg=cor5,fg= cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x= 360,y=0)
b_4= Button(frame_corpo, command=lambda: entrar_valores('7'),text= "7", width= 11, height=4, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x= 0,y=90)
b_5= Button(frame_corpo, command=lambda: entrar_valores('8'),text= "8", width= 11, height=4, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x= 120,y=90)
b_6= Button(frame_corpo, command=lambda: entrar_valores('9'),text= "9", width= 11, height=4, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x= 240,y=90)
b_7= Button(frame_corpo, command=lambda: entrar_valores('*'),text= "*", width= 11, height=4, bg=cor5,fg= cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x= 360,y=90)
b_8= Button(frame_corpo, command=lambda: entrar_valores('4'),text= "4", width= 11, height=4, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x= 0,y=180)
b_9= Button(frame_corpo, command=lambda: entrar_valores('5'),text= "5", width= 11, height=4, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x= 120,y=180)
b_10= Button(frame_corpo, command=lambda: entrar_valores('6'),text= "6", width= 11, height=4, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x= 240,y=180)
b_11= Button(frame_corpo, command=lambda: entrar_valores('-'),text= "-", width= 11, height=4, bg=cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x= 360,y=180)
b_12= Button(frame_corpo, command=lambda: entrar_valores('1'),text= "1", width= 11, height=4, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x= 0,y=270)
b_13= Button(frame_corpo, command=lambda: entrar_valores('2'),text= "2", width= 11, height=4, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x= 120,y=270)
b_14= Button(frame_corpo, command=lambda: entrar_valores('3'),text= "3", width= 11, height=4, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x= 240,y=270)
b_15= Button(frame_corpo, command=lambda: entrar_valores('+'),text= "+", width= 11, height=4, bg=cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x= 360,y=270)
b_16= Button(frame_corpo, command=lambda: entrar_valores('0'),text= "0", width= 23, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_16.place(x=0,y=360)
b_17= Button(frame_corpo, command=lambda: entrar_valores('.'),text= ".", width= 11, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_17.place(x=240,y=360)
b_18= Button(frame_corpo, command= calcular,text= "=", width= 11, height=4, bg=cor5,fg= cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x= 360,y=360)





janela.mainloop()