import MySQLdb
def MuestraTodoLibros():
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="SELECT *FROM Libro;"
	cursor.execute(sql)
	filas=cursor.fetchall()
	return filas

def MuestraLibros():
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="SELECT NombreLibro FROM Libro;"
	cursor.execute(sql)
	filas=cursor.fetchall()
	return filas

def MuestraLibrosISBN():
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="SELECT NombreLibro,ISBN FROM Libro;"
	cursor.execute(sql)
	filas=cursor.fetchall()
	return filas

def MuestraPaises():
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="SELECT Pais FROM Pais;"
	cursor.execute(sql)
	filas=cursor.fetchall()
	return filas

def MuestraEditoriales():
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="SELECT Editorial FROM Editorial;"
	cursor.execute(sql)
	filas=cursor.fetchall()
	return filas

def MuestraGeneros():
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="SELECT Genero FROM Genero;"
	cursor.execute(sql)
	filas=cursor.fetchall()
	return filas

def MuestraAutores():
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="SELECT Autor FROM Autor;"
	cursor.execute(sql)
	filas=cursor.fetchall()
	return filas

def MuestraLibrosAutores():
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="SELECT Libro.NombreLibro,Autor.Autor FROM Libro,Autor,MuestraLibroAutor WHERE Libro.IdLibro=MuestraLibroAutor.IdLibro AND Autor.IdAutor=MuestraLibroAutor.IdAutor;"
	cursor.execute(sql)
	filas=cursor.fetchall()
	return filas

def MuestraLibroEditorial():
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="SELECT Libro.NombreLibro,Editorial.Editorial FROM Libro,Editorial,MuestraLibroEditorial WHERE Libro.IdLibro=MuestraLibroEditorial.IdLibro AND Editorial.IdEditorial=MuestraLibroEditorial.IdEditorial;"
	cursor.execute(sql)
	filas=cursor.fetchall()
	return filas
	
