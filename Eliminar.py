import MySQLdb

def RemoverAutor(Autor):
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="DELETE FROM Autor WHERE Autor='"+Autor+"';
	cursor.execute(sql)

def RemoverGenero(Genero):
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="DELETE FROM Genero WHERE Genero='"+Genero+"';
	cursor.execute(sql)

def RemoverPais(Pais):
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="DELETE FROM Pais WHERE Pais='"+Pais+"';
	cursor.execute(sql)

def RemoverEditorial(Editorial):
	con=MySQLdb.connect('localhost','root','Rigo1994','Libreria')
	cursor=con.cursor()
	sql="DELETE FROM Editorial WHERE Editorial='"+Editorial+"';
	cursor.execute(sql)
