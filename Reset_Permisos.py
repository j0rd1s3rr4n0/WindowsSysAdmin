import os
import time
import getpass
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

def Pregunta():
	global opc1
	opc1 = int(input("Windows Ownership Reset\n 1) Folder\n 2) File\n\n 0) Exit\n option> "))
	os.system('cls')

def SeleccionarArchivo():
	Pregunta()
	Tk().withdraw()
	os.system('title Windows Ownership Reset ~ By Bluegraded && @echo off && cls')
	#filename = askopenfilename() 
	global filename
	if opc1 == 2:
		filename = askopenfilename(title="Windows Ownership Reset",filetypes=[
		("Select file", "*.*"),("Select folder", "*"),])
	elif opc1 == 1:
		filename = askdirectory(title="Windows Ownership Reset")
		filename = filename
	elif opc1 == 0:
		exit()
	else:
		Pregunta()

SeleccionarArchivo()
print(filename)
comando = '''icacls "'''+filename+'''" /reset /t /c /l'''
os.system(comando)
userr = getpass.getuser()
comando2 = 'mkdir "C:/Users/'+userr+'/Desktop/Copia de Seguridad/"'
os.system(comando2)
comando3 = 'copy "'+filename+'/" "C:/Users/'+userr+'/Desktop/Copia de Seguridad/"'
os.system(comando3)
#print(comando)
#print(comando2)
#print(comando3)
os.system('cls')
os.system('color 4f')
print('''
              _
             | |
             | |===( )   //////
             |_|   |||  | o o|
                    ||| (  _ )                  ____
                     ||| \= /                  ||   \_
                      ||||||                   ||     |
                      ||||||                ...||__/|-"
                      ||||||             __|________|__
                        |||             |______________|
                        |||             || ||      || ||
                        |||             || ||      || ||
------------------------|||-------------||-||------||-||-------
                        |__>            || ||      || ||

                   HIT ANY KEY TO EXIT
''')
os.system('pause > null && del null && color 0f')
exit()
