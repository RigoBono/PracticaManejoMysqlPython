import MySQLdb
def Test():
	db=MySQLdb.connect('localhost','root','Rigo1994')
	cursor=db.cursor()
	sql='SHOW DATABASES';
	cursor.execute(sql)
	Existe=False
	filas=cursor.fetchall()
	for fila in filas:
		fila=str(fila)
		fila=fila.replace("(","")
		fila=fila.replace(")","")
		fila=fila.replace("'","")
		fila=fila.replace(",","")
		if fila=="Libreria":
			Existe=True
			break
	if Existe==False:
		sql="CREATE DATABASE Libreria;"
		cursor.execute(sql)
		sql="USE Libreria"
		cursor.execute(sql)
		sql="CREATE TABLE Pais(IdPais INT AUTO_INCREMENT PRIMARY KEY,Pais Varchar(30));"
		cursor.execute(sql)
		sql="CREATE TABLE Autor(IdAutor INT AUTO_INCREMENT PRIMARY KEY,Autor VARCHAR(30));"
		cursor.execute(sql)
		sql="CREATE TABLE Genero(IdGenero INT AUTO_INCREMENT PRIMARY KEY,Genero VARCHAR(30));"
		cursor.execute(sql)
		sql="CREATE TABLE Editorial(IdEditorial INT AUTO_INCREMENT PRIMARY KEY,IdPais INT,Editorial VARCHAR(30),FOREIGN KEY(IdPais) REFERENCES Pais(IdPais) ON DELETE CASCADE);"
		cursor.execute(sql)
		sql="CREATE TABLE Libro(IdLibro INT AUTO_INCREMENT PRIMARY KEY,IdGenero INT,NombreLibro TEXT,ISBN VARCHAR(20),Cantidad INT,Precio DECIMAL,FOREIGN KEY(IdGenero) REFERENCES Genero(IdGenero) ON DELETE CASCADE);"
		cursor.execute(sql)
		sql="CREATE TABLE MaestraLibroAutor(IdAutor INT,IdLibro INT,FOREIGN KEY(IdLibro) REFERENCES Libro(IdLibro) ON DELETE CASCADE,FOREIGN KEY(IdAutor) REFERENCES Autor(IdAutor) ON DELETE CASCADE);"
		cursor.execute(sql)
		sql="CREATE TABLE MaestraLibroEditorial(IdEditorial INT,IdLibro INT,FOREIGN KEY(IdLibro) REFERENCES Libro(IdLibro) ON DELETE CASCADE,FOREIGN KEY(IdEditorial) REFERENCES Editorial(IdEditorial) ON DELETE CASCADE);"
		cursor.execute(sql)
		print "Base creada"
	print "Fin de test de existencia"


