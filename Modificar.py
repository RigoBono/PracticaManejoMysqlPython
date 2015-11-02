import MySQLdb

def BusquedaPorNombreLibro(NombreLibro):
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="SELECT IdLibro FROM Libro WHERE NombreLibro="+NombreLibro;"
	cursor.execute(sql)
	filas=cursor.fetchall()
	for fila in filas:
		Id=fila[0];
		Id=int(Id)
		break;
	return Id

def ModificaLibro(IdLibro,IdGenero,NombreLibro,ISBN,Precio,Cantidad):
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="UPDATE Libro SET NombreLibro='"+NombreLibro+"',IdGenero="+str(IdGenero)+",ISBN='"+ISBN+"',Precio="+str(Precio)+",Cantidad="+str(Cantidad)+" WHERE IdLibro="+IdLibro+";"
	cursor.execute(sql)
