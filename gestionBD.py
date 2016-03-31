import sqlite3
import sys

"""
Méthode qui servent à gérer la création de connection, de curseur et l'execution de requete
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
