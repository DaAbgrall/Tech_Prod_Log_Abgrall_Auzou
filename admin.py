import mysql.connector
import sys

def creationBD():
    connec = lite.connect('projet.db')
    cur = connec.cursor("CREATE TABLE Installation(numero INT, nom TEXT,adresse TEXT, code_postale TEXT, ville TEXT, latitude)")    
