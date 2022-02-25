import requests
import json
import time
import datetime
from tkinter import *
import tkinter as tk



#//////////////////////////////////////////////// Funcón que se encarga de hacer request a los endpoint configurados en la instacia aws

def tomaderecursos():
    cerrarventana()

    while True:      
                      

        #////////////////////////////////////////// Codigo para conocer la fecha y hora actual
        
        today = datetime.datetime.now()
        datenombre = (today.strftime("%x"))
        hora= datetime.datetime.now()
        horatxt = (hora.strftime("%X"))
        today = str(today)
        #print(horatxt)
       
        #///////////////////////////////////////////Codigo para tomar valor de cpu de la instancia a traves de GET
        
        urlcpu = "http://52.23.206.65/performance"
        resultadocpu = requests.get(urlcpu)
        cpuhost = (json.dumps(resultadocpu.json(), indent=1))
        cpuhostrm = cpuhost
        cpuhostrm = cpuhostrm[0:2] + cpuhostrm[98:500]
        cpuhostrm
        carcateresnoesenciales = "n', None)"
        cpuhostrm = ''.join(cpuhostrm.split(carcateresnoesenciales,1))
        cpuhost = cpuhostrm
        
        #/////////////////////////////////////////// Codigo para tomar la version de la instancia a traves de GET
       
        urlversion = "http://52.23.206.65/version"
        resultadoversion = requests.get(urlversion)
        versionhost = (json.dumps(resultadoversion.json(), indent=1))
        verhostrm = versionhost
        pos = "(b'"
        verhostrm = ''.join(verhostrm.split(pos,1))
        carcateresnoesenciales = "n', None)"
        verhostrm = ''.join(verhostrm.split(carcateresnoesenciales,1))
        versionhost = verhostrm
                             
               
        #///////////////////// Codigo para tomar la ip de la instancia a traves de GET
       
        remoteip = "http://52.23.206.65/iphost"
        resultadoiphost = requests.get(remoteip)
        dataiphost = resultadoiphost.json()
        iphoststr =''.join([str(item) for item in dataiphost])
        iphoststr = iphoststr.rstrip("\n")
        namecsv = "%s.txt" % iphoststr
          

        #////////////////////Codigo que toma los procesos activos de la Instancia a traves de GET

        urlproceso = "http://52.23.206.65/procesos"
        resultadoproceso = requests.get(urlproceso)
        procesoshost = (json.dumps(resultadoproceso.json(), indent=1))
        
        
        #//////////////////// Codigo para crear el nombre del archivo de texto
        datenombre = datenombre.replace("/","-")
      
        nombretxt = (datenombre + "-" + "Host " + namecsv)
      
        


        #///////////////////// Se crea el archivo de texto
        with open(nombretxt, 'a') as c:
           # c.write("                                                                        ")
             c.write("///////////////////////////////////////// CPU " + " Hora: " + horatxt + "//////////////////////////////\n")
            # c.write("                                                                        ")
             c.write(cpuhost + "\n")
             #c.write("                                                                           ")
             c.write("/////////////////////////////////////// VERSION " + " Hora: " + horatxt + " ////////////////////////////\n")
           # c.write("                                                                           ")
             c.write(versionhost + "\n")
            #c.write("                                                                           ")
             c.write("/////////////////////////////////////// PROCESOS " + " Hora: " + horatxt + "////////////////////////////\n")
            #c.write("                                                                          ")
             c.write(procesoshost + "\n")

        #///////////////////// Se encarga del tiempo de espera entre toma de recursos de la nistancia
        time.sleep(tiempomonitoreo)



#//////////////////////// Función que dstruye la ventana e inicio
        
def cerrarventana():
    ventana.destroy()

#//////////////////////// Función que toma el valor de tiempo de muestreo
def valormonitoreo():
    global tiempomonitoreo
    tiempomonitoreo= int(intervalo.get())
    tomaderecursos()
    

#////////////////////////Codigo donde se crea la interface grafica para solicitar el tiempo de muestreo
    
ventana=tk.Tk()
ventana.title("MonitorAgent -  MELI")
ventana.geometry('300x200')
ventana.configure(background='yellow')

label=tk.Label(ventana, text= "Ingrese intervalo de tiempo de monitoreo ", bg="white",fg="blue2",font=(None, 9), height=1, width=50)
label.pack(side=tk.TOP)
label.pack(padx=5,pady=5,ipadx=3,ipady=3)

intervalo= tk.Entry(ventana)
intervalo.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

boton1=tk.Button(ventana,text="    submit  ",fg="black", command=valormonitoreo)
boton1.pack(side=tk.TOP)

ventana.mainloop()   


  
   
    
    
    
    
