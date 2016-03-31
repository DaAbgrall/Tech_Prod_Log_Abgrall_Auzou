import sqlite3
import sys

"""
Methode qui servent à gerer la creation de connection, de curseur et l'execution de requete
"""

def connection():
    return sqlite3.connect('projet.db')


def curseur():
    return self.cursor()


def deconnection():
    connec.close()
    connec.commit

def execution(v):
    cur = connec.cursor()
    cur.execute(v)
