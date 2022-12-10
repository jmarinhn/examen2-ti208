#developer
from Tkinter import *
import ttk
import os
import subprocess
import tkFont
import tkMessageBox
import time
import ScrolledText


# Crear Ventana
v0=Tk()
v0.title("Control GPIO")
v0.geometry("700x400+0+0")

# zona de Funciones
img_on=PhotoImage(file="/home/jmarin/Downloads/on.gif")
img_off=PhotoImage(file="/home/jmarin/Downloads/off.gif")
texto2=tkFont.Font(family="Helvetica",size=70)
def update1():
              #os.system("sudo cat /home/josue_marin/estado.txt > estado.txt")
              pf=open("/home/josue_marin/estado.txt","r")
              for linea in pf:
                              campo=linea.split("\n")
                              campof=campo[0]
                              if (campof=="1"):
                                                texto2=tkFont.Font(family="Arial", size=80)
                                                label_estado=Label(v0,text="1",font=texto2).place(x=100,y=120)
                                                v0.after(1000,update1)
                              if (campof=="0"):
                                               texto2=tkFont.Font(family="Arial",size=80)
                                               label_estado=Label(v0,text="0",font=texto2).place(x=100,y=120)
                                               v0.after(1000,update1)
# Llamar funcion
update1()              



# Segunda Funcion Recursiva
def update2():
              os.system("sudo cat /home/josue_marin/estado.txt > estado.txt")
              pf2=open("/home/josue_marin/estado.txt","r")
              for linea2 in pf2:
                                campo=linea2.split("\n")
                                campof=campo[0]
                                if (campof=="1"):
                                                 btn_on=Button(v0,image=img_on).place(x=200,y=120)
                                                 v0.after(1000,update2)
                                if (campof=="0"):
                                                 btn_off=Button(v0,image=img_off).place(x=200,y=120)
                                                 v0.after(1000,update2)
# Llamar segunda Funcion
update2()

def encender():
               print "Encendido"
               os.system("sudo bash /home/josue_marin/onremoto.sh")
               

def apagar():
             print "Apagado"
             os.system("sudo bash /home/josue_marin/offremoto.sh")


def ejecutarcheck():
                    c=int(check.get())
                    if (c==1):
                              os.system("sudo bash /home/josue_marin/on27.sh")
                              os.system("sudo bash /etc/ssmtp/correo1.sh")
                    if (c==0):
                              os.system("sudo bash /home/josue_marin/off27.sh")
                              os.system("sudo bash /etc/ssmtp/correo2.sh")
    

texto1=tkFont.Font(family="Helvetica",size=18)
label1=Label(v0,text="CONTROL GPIO ",font=texto1).place(x=150,y=10)

def ejecutarcombo():
                     c=str(combo.get())
                     if (c=="ON"):
                                  os.system("sudo bash /home/josue_marin/on27.sh")
                                  os.system("sudo bash /etc/ssmtp/correo1.sh")

                     if (c=="OFF"):
                                  os.system("sudo bash /home/josue_marin/off27.sh")
                                  os.system("sudo bash /etc/ssmtp/correo2.sh")

def ejecutaradio():
                   r=int(radio.get())
                   if (r==1):
                             os.system("sudo bash /home/josue_marin/on27.sh")
                                  os.system("sudo bash /etc/ssmtp/correo1.sh")
                   if (r==2):
                             os.system("sudo bash /home/josue_marin/off27.sh")
                                  os.system("sudo bash /etc/ssmtp/correo2.sh")

def limpiarcampos():
                     horai.set('')
                     minini.set('')
                     horaf.set('')
                     minf.set('')
                             
# Funcion Aplicar
def Aplicar():
              print "Guardar Tiempo"
              hi=str(horai.get())
              mi=str(minini.get())
              hf=str(horaf.get())
              mf=str(minf.get())
              tab=" "
              dia="*"
              mes="*"
              ano="*"
              user="root"
              path1="/home/josue_marin/on.sh"
              path2="/home/josue_marin/off.sh"

              cadena1=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path1))
              cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2))
              # Cambiar permisos
              os.system("sudo chmod -R 777 /etc/cron.d/evento1")
              os.system("sudo chmod -R 777 /etc/cron.d/evento2")

              # Insertar informacion en los Archivos
              pf1=open("/etc/cron.d/evento1","w")
              pf1.write(cadena1)
              pf1.write("\n")
              pf1.close()
              
              # Insertar informacion en los Archivos
              pf2=open("/etc/cron.d/evento2","w")
              pf2.write(cadena2)
              pf2.write("\n")
              pf2.close()

              #Revertir permisos de archivos
              os.system("sudo chmod -R 755 /etc/cron.d/evento1")
              os.system("sudo chmod -R 755 /etc/cron.d/evento2")

              # Pausa de seguridad
              time.sleep(0.1)
              # Ejecutar el reinicio del servicio cron
              os.system("sudo /etc/init.d/cron restart")

              # llamar Funcion limpiar campos
              limpiarcampos()

                                
# Zona de Botones 
btn_on=Button(v0,text="ON",command=encender).place(x=10,y=30)
btn_off=Button(v0,text="OFF",command=apagar).place(x=100,y=30)

# Checkbok

global check
check=IntVar()

check1=ttk.Checkbutton(v0,text="ON/OFF",variable=check,command=ejecutarcheck)
check1.place(x=10,y=80)

# --- Combobox -----
global combo
combo=StringVar()
combo=ttk.Combobox(v0,state="read only",values=["ON","OFF"])
combo.place(x=100,y=80)
btn_combo=Button(v0,text=">",command=ejecutarcombo).place(x=290,y=80)

# Radio Button
global radio
radio=IntVar()

r1=ttk.Radiobutton(v0,text="ON",variable=radio,value=1,command=ejecutaradio).place(x=350,y=80)

r2=ttk.Radiobutton(v0,text="OFF",variable=radio,value=2,command=ejecutaradio).place(x=450,y=80)

# Etiquetas
texto2=tkFont.Font(family="Arial", size=14)
label_horai=Label(v0,text="Hora Inicial:",font=texto2).place(x=350,y=120)
label_minini=Label(v0,text="Minuto Inicial:",font=texto2).place(x=350,y=150)
label_horaf=Label(v0,text="Hora Final:",font=texto2).place(x=350,y=180)
label_minf=Label(v0,text="Minuto Final:",font=texto2).place(x=350,y=210)

# Declarar Variables
global horai,minini,horaf,minif
horai=StringVar()
minini=StringVar()
horaf=StringVar()
minf=StringVar()
# Cajas de Texto
txt_horai=Entry(v0,textvariable=horai,width=10).place(x=480,y=120)
txt_minini=Entry(v0,textvariable=minini,width=10).place(x=480,y=150)
txt_horaf=Entry(v0,textvariable=horaf,width=10).place(x=480,y=180)
txt_minf=Entry(v0,textvariable=minf,width=10).place(x=480,y=210)

btn_aplicar=Button(v0,text="APPLY", command=Aplicar).place(x=600,y=180)




v0.mainloop()


