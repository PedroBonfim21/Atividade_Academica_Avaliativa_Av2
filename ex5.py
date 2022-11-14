'''
Utilizando a biblioteca gráfica Tkinter, o aluno deve construir uma
interface que simule uma tela de login de usuário contendo o campo de login,
senha e um botão de autenticação.
'''
from tkinter import *

janela=Tk()

lab1= Label(janela, text='login: ')
lab2= Label(janela, text='senha: ')
ed1= Entry(janela,)
ed2= Entry(janela,)
btn1= Button(janela, text='Confirmar')

lab1.grid(row=0 ,column=0 )
lab2.grid(row=1 ,column=0 )
ed1.grid(row=0 ,column=1 )
ed2.grid(row=1 ,column=1 )
btn1.grid(row=2 ,column=1 )

janela.geometry('200x100+100+100')

janela.mainloop()
