from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5
from datetime import date
from datetime import datetime
import qrcode 
#Dia actual
today = date.today()
#Fecha actual
now = datetime.now()
ruta = "C:/Users/adanz/OneDrive/Escritorio/SegundoParcial/"

c = canvas.Canvas(ruta+'Ticket.pdf', pagesize=A5)

#ancho, alto = legal
lista = []
productos = []
precio = []
cantidad = []
total = [0,0,0,0,0]



print("----Lista de productos a comprar----")
for i in range(5):
    lista.append(i)
    productos.append(input("Ingresa tu producto "))
    cantidad.append(int(input("Cuantos articulos llevas? ")))
    precio.append(float(input("Ingresa el precio del producto ")))
    total[i] = cantidad[i]*precio[i]

nombre = input(str("Con quien tengo el gusto: "))
direccion = input(str("Quien la direccion donde deseas los prodcutos: "))
correo = input(str("Correo electronico de apoyo: "))

#---------PDF----------

c.setFont('Helvetica-Bold', 20)
c.drawString(230,560,"LIVERPULGA")
c.setFont('Helvetica', 8)
c.drawString(120,540,"D i s t r i b u i d o r a  L i v e r p u l g a   S . A   d e   C . V . ")
c.setFont('Helvetica', 8)
c.drawString(100,520,"C. Mario Pani  No.  200")
c.setFont('Helvetica', 8)
c.drawString(100,510,"Col. 10 de Abril C.P 53320")
c.setFont('Helvetica', 8)
c.drawString(100,500,"Deles. CuaJimlpa de Morelos D.F")
c.setFont('Helvetica', 8)
c.drawString(100,490,"Tel: 56 22 11 73 15 RFC: DLI-93124-M69")

c.setFont('Helvetica', 10)
c.drawString(80,470,"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

c.setFont('Helvetica', 8)
c.drawString(100,450,"Ciudad de Mexico")
c.setFont('Helvetica', 8)
c.drawString(100,440,"Liverpulga Ciudad de Mexico")
c.setFont('Helvetica', 8)
c.drawString(100,430,"Av. Tulun Sur No. 260")
c.setFont('Helvetica', 8)
c.drawString(100,420,"Super Manzana 7 Benito Juarez ")
c.setFont('Helvetica', 8)
c.drawString(100,410,"Tel. (562) 21 17 315")
c.setFont('Helvetica', 8)
c.drawString(100,400,"C.P. 53320")
c.setFont('Helvetica', 8)
c.drawString(100,390,"Ciudad de Mexico, Naucalpan de Juarez")

c.setFont('Helvetica', 10)
c.drawString(80,370,"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

c.setFont('Helvetica-Bold', 15)
c.drawString(200,350,"VENTA")

c.setFont('Helvetica', 8)
c.drawString(100,330,"TERM")
c.drawString(100,320,"083")

c.drawString(150,330,"DOCTO")
c.drawString(150,320,"1101")

c.drawString(250,330,"TDA")
c.drawString(250,320,"0036")

c.drawString(300,330,"VEND")
c.drawString(300,320,"14051322")

c.drawString(130,300,"ATENDIO: CHRISTOFER ADAN ZAMUDIO IBARRA")

c.setFont('Helvetica-Bold', 8)
c.drawString(200,290,"PRODUCTO")

c.setFont('Helvetica', 8)
c.drawString(97,280,"NOMBRE")

c.setFont('Helvetica', 8)
c.drawString(200,280,"CANTIDAD")

c.setFont('Helvetica', 8)
c.drawString(300,280,"PRECIO")

c.setFont('Helvetica', 8)   
d=260
totalPagar=0
for i in range(len(productos)):
        c.drawString(97,d,productos[i])
        c.drawString(200,d,str(cantidad[i]))
        c.drawString(300,d,str(total[i]))
        totalPagar= total[i]+total[i]
        d =d-10



c.setFont('Helvetica', 10)
c.drawString(80,200,"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

c.setFont('Helvetica-Bold', 10)
c.drawString(250,190,"TOTAL: ")
#c.drawString(280,190,totalPagar)
c.setFont('Helvetica-Bold', 10)
c.drawString(200,170,"Datos del Cliente")

c.setFont('Helvetica', 10)
c.drawString(100,160,"Cliente: ")
c.drawString(140,160,nombre)

c.setFont('Helvetica', 10)
c.drawString(100,150,"Dirección: ")
c.drawString(150,150,direccion)

c.setFont('Helvetica', 10)
c.drawString(100,140,"Correo:: ")
c.drawString(140,140,correo)
#--------QR-------
h = 100
x = 100
y = h - 50

informacion = "El compra a finalizado a nombre de: "+ nombre + " a la direccion "+ direccion + " correo de apoyo " + correo
img = qrcode.make(informacion)
nombreImagen = ruta +"miQR.png"
f = open(nombreImagen, "wb")
img.save(f)
f.close()

c.drawImage(nombreImagen,190,70,70,70)
c.setFont('Helvetica', 10)
c.drawString(150,60,"GRACIAS POR SU COMPRA :) ")

c.save()
