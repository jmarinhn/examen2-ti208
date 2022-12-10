import imaplib
import os
SERVER = 'imap.gmail.com'
USER = 'jmarin'
MAIL = "josue.marin@usap.edu"
PASS = 'bojylcsebjrhegrw'

#3) Conectar con en el servidor:

server = imaplib.IMAP4_SSL(SERVER, 993)

#4) Iniciar sesión:

server.login(USER, PASS)

#5) Seleccionar mensaje a leer:

status, count = server.select('Inbox')
status, data = server.fetch(count[0], '(UID BODY[TEXT])')

flag=str((data[0][1]))
#print (data[0][1]) # Mensaje escogido
print (flag)
#str(flag.startswith("ON21"))

#
