import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="marie",
    password="marikiki9283",
    database="mydatabase"
)

print(mydb)

mycursor = mydb.cursor()


mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Commune ("
    "nb_habitant INT,"
    "distance_agence SMALLINT,"
    "nom_commune VARCHAR(50) NOT NULL,"
    "cp CHAR(5),"
    "id_commune SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY"
    ")"
    "ENGINE=InnoDB;"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Loyer ("
    "id_loyer SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "type_Logement VARCHAR(3),"
    "mt_loyer SMALLINT,"
    "frais SMALLINT"
    ")"
    "ENGINE=InnoDB;"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Individu ("
    "id_individu SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "nom VARCHAR(55) NOT NULL,"
    "prenom VARCHAR(55) NOT NULL,"
    "date_naissance DATE,"
    "num_tel1 CHAR(10),"
    "num_tel2 CHAR(10)"
    ")"
    "ENGINE=InnoDB;"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Logement ("
    "superficie SMALLINT,"
    "adresse VARCHAR(255),"
    "id_commune SMALLINT UNSIGNED NOT NULL,"
    "id_loyer SMALLINT UNSIGNED NOT NULL,"
    "id_logement SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "CONSTRAINT fk_id_commune FOREIGN KEY (id_commune) REFERENCES Commune(id_commune),"
    "CONSTRAINT fk_id_loyer FOREIGN KEY (id_loyer) REFERENCES Loyer(id_loyer)"
    ")"
    "ENGINE=InnoDB;"
)

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Location ("
    "date_debut DATE,"
    "date_fin DATE,"
    "id_logement SMALLINT UNSIGNED NOT NULL,"
    "id_individu SMALLINT UNSIGNED NOT NULL,"
    "id_location SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "CONSTRAINT fk_id_logement FOREIGN KEY (id_logement) REFERENCES Logement(id_logement),"
    "CONSTRAINT fk_id_individu FOREIGN KEY (id_individu) REFERENCES Individu(id_individu)"
    ")"
    "ENGINE=InnoDB;"
)

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

print("___________________________________________________________________________________________________________")
print("___________________________________________COMMUNE_____________________________________________________")
# insertion dans commune
sql = "INSERT INTO Commune (nb_habitant, distance_agence, nom_commune,cp) VALUES (%s, %s, %s, %s)"
val = [
    (10000, 10, 'ville1', 59111),
    (22222, 22, 'ville2', 59222),
    (333, 333, 'ville3', 59003),
    (4410222, 124, 'ville4', 59444),
    (55, 5, 'ville5', 59557)
]

mycursor.executemany(sql, val)
print(mycursor.rowcount, " tuples ont été insérés :")
mycursor.execute("SELECT * FROM Commune")
result = mycursor.fetchall()
for row in result:
    print(row)

print('')

mycursor.execute("UPDATE Commune SET nom_commune = 'new_town1' WHERE cp = 59111;")
result = mycursor.fetchall()
print('modification effectuée dans commune : le cp 59111 devient new_town')
mycursor.execute("SELECT * FROM Commune")
result = mycursor.fetchall()
for row in result:
    print(row)

print('')
mycursor.execute("DELETE FROM Commune WHERE nom_commune = 'new_town1';")
result = mycursor.fetchall()
print('suppressions dans commune des "new_town"')
mycursor.execute("SELECT * FROM Commune")
result = mycursor.fetchall()
for row in result:
    print(row)

mydb.commit()


print("_______________________________________________________________________________________________________________")
print("____________________________________________________Loyer____________________________________________________")
# insertion dans loyer
sql = "INSERT INTO Loyer (type_Logement, mt_loyer, frais) VALUES (%s, %s, %s)"
val = [
    ('T1', 250, 50),
    ('T2', 350, 60),
    ('T3', 455, 65),
    ('T4', 800, 140),
    ('LOF', 1200, 200)
]
mycursor.executemany(sql, val)

print(mycursor.rowcount,  "tuples ont été insérés :")
mycursor.execute("SELECT * FROM Loyer")
result = mycursor.fetchall()
for row in result:
    print(row)

print('')

mycursor.execute("UPDATE Loyer SET type_Logement = 'T5' WHERE frais = 200;")
result = mycursor.fetchall()
print('modification effectuée dans Loyer :')
mycursor.execute("SELECT * FROM Loyer")
result = mycursor.fetchall()
for row in result:
    print(row)

print('')

print('suppressions effectuées dans Loyer : le loft devient T5')
mycursor.execute("DELETE FROM Loyer WHERE id_loyer>5;")
result = mycursor.fetchall()
mycursor.execute("SELECT * FROM Loyer")
result = mycursor.fetchall()
for row in result:
    print(row)

mydb.commit()

print("_______________________________________________________________________________________________________________")
print("____________________________________________________INDIVIDU____________________________________________________")

# insertion dans Individu
sql = "INSERT INTO Individu(nom, prenom, date_naissance,num_tel1, num_tel2)  VALUES (%s, %s, %s, %s, %s)"

val = [
    ('dujardin', 'franck', 19580706, '0614251859', "null"),
    ('durand', 'jean', 19550602, '0614747578', '0321458595'),
    ('dupont', 'jules', None, '0606060606', None),
    ('henry', 'jeanette', 19600607, '0707070707', '0320030203'),
    ('delattre', 'huguette', 19451102, "null", "null")
]
mycursor.executemany(sql, val)

print(mycursor.rowcount,  "tuples ont été insérés :")
mycursor.execute("SELECT * FROM Individu")
result = mycursor.fetchall()
for row in result:
    print(row)

print('')

mycursor.execute("UPDATE Individu SET num_tel2 = '0320506041' WHERE nom = 'delattre';")
result = mycursor.fetchall()
print('modification effectuée dans Individu : mettre un numero de tel à mr delattre')
mycursor.execute("SELECT * FROM Individu")
result = mycursor.fetchall()
for row in result:
    print(row)

print('')

print('suppressions effectuées dans Individu : suppression des "jean"')
mycursor.execute("DELETE FROM Individu WHERE prenom='jean';")
result = mycursor.fetchall()
mycursor.execute("SELECT * FROM Individu")
result = mycursor.fetchall()
for row in result:
    print(row)

mydb.commit()


print("_______________________________________________________________________________________________________________")
print("____________________________________________________Logement____________________________________________________")

# insertion dans Logement
sql = "INSERT INTO Logement (superficie, adresse, id_commune, id_loyer) VALUES (%s, %s, %s, %s)"
val = [
    (25, '1rue premiere', 2, 2),
    (45, '2rue premiere', 2, 4),
    (50, None, 3, 5),
    (75, '4rue premiere', 3, 1),
    (150, '5rue premiere', 4, 2)
]

mycursor.executemany(sql, val)

print(mycursor.rowcount,  "tuples ont été insérés :")
mycursor.execute("SELECT * FROM Logement")
result = mycursor.fetchall()
for row in result:
    print(row)

print('')

mycursor.execute("UPDATE Logement SET adresse = '30 rue solferino' WHERE adresse IS NULL;")
result = mycursor.fetchall()
print('modification effectuée dans Logement : mettre une adresse si null')
mycursor.execute("SELECT * FROM Logement")
result = mycursor.fetchall()
for row in result:
    print(row)

print('')

print('suppressions effectuées dans Logement : suppression des id_commune=4')
mycursor.execute("DELETE FROM Logement WHERE id_commune=4;")
result = mycursor.fetchall()
mycursor.execute("SELECT * FROM Logement")
result = mycursor.fetchall()
for row in result:
    print(row)

mydb.commit()


print("_______________________________________________________________________________________________________________")
print("____________________________________________________Location____________________________________________________")

# insertion dans Location
sql = "INSERT INTO Location (date_debut, date_fin, id_logement, id_individu) VALUES (%s, %s, %s, %s)"
val = [
    (20200101, 20220101, 1, 1),
    (20200222, 20230101, 1, 3),
    (20200219, 20220101, 3, 4),
    (20190101, 20201001, 4, 1),
    (20190101, 20221207, 4, 1)
]

mycursor.executemany(sql, val)

print(mycursor.rowcount,  "tuples ont été insérés :")
mycursor.execute("SELECT * FROM Location")
result = mycursor.fetchall()
for row in result:
    print(row)

print('')

mycursor.execute("UPDATE Location SET id_logement = 1 WHERE id_individu = 3;")
result = mycursor.fetchall()
print('modification effectuée dans Location :id_logement = 1 WHERE id_individu = 3')
mycursor.execute("SELECT * FROM Location")
result = mycursor.fetchall()
for row in result:
    print(row)

print('')

print('suppressions effectuées dans Location : suppression des id_commune=4')
mycursor.execute("DELETE FROM Location WHERE id_individu=4;")
result = mycursor.fetchall()
mycursor.execute("SELECT * FROM Location")
result = mycursor.fetchall()
for row in result:
    print(row)

mydb.commit()

# mydb.commit()
#
# print(mycursor.rowcount,  "tuples ont été insérés :")
#
# print('affichage du contenu de Location avant modif')
# mycursor.execute("SELECT * FROM Location")
#
# result = mycursor.fetchall()
# for row in result:
#     print(row)
#
# print('modifier dans Location')
# mycursor.execute("UPDATE Location SET id_logement = 13 WHERE id_individu = 3;")
# result = mycursor.fetchall()
#
# print('affichage du contenu de Location apres modif')
# mycursor.execute("SELECT * FROM Location")
#
# result = mycursor.fetchall()
# for row in result:
#     print(row)
#
# print('suppressions dans Location')
# mycursor.execute("DELETE FROM Location WHERE id_location>50;")
# result = mycursor.fetchall()
#
# mydb.commit()
#
# print('affichage du contenu de Location apres suppressions')
# mycursor.execute("SELECT * FROM Location")
#
# result = mycursor.fetchall()
#
# for row in result:
#     print(row)
