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

print("___________________________________________")

# # insertion dans commune
# sql = "INSERT INTO Commune (nb_habitant, distance_agence, nom_commune,cp) VALUES (%s, %s, %s, %s)"
# val = [
#     (10000, 10, 'ville1', 59111),
#     (22222, 22, 'ville2', 59222),
#     (333, 333, 'ville3', 59003),
#     (4410222, 124, 'ville4', 59444),
#     (55, 5, 'ville5', 59557)
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted in commune.")
#
# print("___________________________________________")
#
# # insertion dans loyer
# sql = "INSERT INTO Loyer (type_Logement, mt_loyer, frais) VALUES (%s, %s, %s)"
# val = [
#     ('T1', 250, 50),
#     ('T2', 350, 60),
#     ('T3', 455, 65),
#     ('T4', 800, 140),
#     ('LOF', 1200, 200)
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted in loyer.")
#
# print("___________________________________________")
#
# # insertion dans Individu
# sql = "INSERT INTO Individu(nom, prenom, date_naissance,num_tel1, num_tel2)  VALUES (%s, %s, %s, %s, %s)"
#
# val = [
#     ('dujardin', 'franck', 19580706, '0614251859', "null"),
#     ('durand', 'jean', 19550602, '0614747578', '0321458595'),
#     ('dupont', 'jules', None, '0606060606', None),
#     ('henry', 'jeanette', 19600607, '0707070707', '0320030203'),
#     ('delattre', 'huguette', 19451102, "null", "null")
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted in Individu.")


#
# print("___________________________________________")
#
# insertion dans Logement
# sql = "INSERT INTO Logement (superficie, adresse, id_commune, id_loyer) VALUES (%s, %s, %s, %s)"
# val = [
#     (25, '1rue premiere', 1, 7),
#     (45, '2rue premiere', 1, 8),
#     (50, None, 3, 9),
#     (75, '4rue premiere', 3, 9),
#     (150, '5rue premiere', 4, 10)
# ]

# mycursor.executemany(sql, val)

# mydb.commit()
#
# print(mycursor.rowcount, "was inserted in Logement.")
#
# print("___________________________________________")
#
# insertion dans Location
sql = "INSERT INTO Location (date_debut, date_fin, id_logement, id_individu) VALUES (%s, %s, %s, %s)"
val = [
    (20200101, 20220101, 11, 11),
    (20200222, 20230101, 12, 13),
    (20200219, 20220101, 13, 14),
    (20190101, 20201001, 14, 14),
    (20190101, 20221207, 14, 14)
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted in Location.")


mycursor.execute("SELECT * FROM Location")

# fetch all the matching rows
result = mycursor.fetchall()

# loop through the rows
for row in result:
    print(row)