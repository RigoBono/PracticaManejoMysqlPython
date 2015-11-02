import MySQLdb
def InsertaPais(Pais):
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="INSERT INTO Pais(Pais) VALUES('"+Pais+"');"
	cursor.execute(sql)

def InsertaAutor(Autor):
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="INSERT INTO Autor(Autor) VALUES('"+Autor+"');"
	cursor.execute(sql)

def InsertaGenero(Genero):
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="INSERT INTO Genero(Genero) VALUES('"+Genero+"');"
	cursor.execute(sql)

def InsertaGenero(Genero,IdPais):
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="INSERT INTO Genero(Genero) VALUES('"+Genero+"',"+str(IdPais)+");"
	cursor.execute(sql)

def InsertaGenero(Genero,IdPais):
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="INSERT INTO Genero(Genero) VALUES('"+Genero+"',"+str(IdPais)+");"
	cursor.execute(sql)

def InsertaLibro(NombreLibro,ISBN,Precio,Cantidad,IdGenero):
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="INSERT INTO Libro(IdGenero,NombreLibro,ISBN,Cantidad,Precio) VALUES("+IdGenero+",'"+NombreLibro+"','"+ISBN+"',"+str(Cantidad)+","+str(Precio)+");"
	cursor.execute(sql)

def InsertaLibroAutor(IdLibro,IdAutor):
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="INSERT INTO MaestraLibroAutor VALUES("+str(IdLibro)+","+str(IdAutor)+");"
	cursor.execute(sql)

def InsertaLibroEditorial(IdLibro,IdEditorial):
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="INSERT INTO MaestraLibroEditorial VALUES("+str(IdLibro)+","+str(IdEditorial)+");"
	cursor.execute(sql)

