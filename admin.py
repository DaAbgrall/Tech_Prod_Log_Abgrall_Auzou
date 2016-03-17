import sqlite3 as lite
import sys

def creationBD():
    connec = lite.connect('projet.db')
    cur = connec.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS Installation(numero INT PRIMARY KEY, nom TEXT,adresse TEXT, code_postale TEXT, ville TEXT, latitude DECIMAL, longitude DECIMAL)")
    
    cur.execute("CREATE TABLE IF NOT EXISTS Equipement(numero INT PRIMARY KEY, nom TEXT, numero_installation INT, FOREIGN KEY(numero_installation) REFERENCES Installation(numero)) ")    
    
    cur.execute("CREATE TABLE IF NOT EXISTS Equipement_Activite(numero_equipement INT, numero_activite INT, FOREIGN KEY(numero_equipement) REFERENCES Equipement(numero), FOREIGN KEY(numero_activite) REFERENCES Activite(numero))")    

    cur.execute("CREATE TABLE IF NOT EXISTS Activite(numero INT PRIMARY KEY, nom TEXT)")    

