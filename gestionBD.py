import sqlite3 as lite
import sys

def connection():
    connec = lite.connect('projet.db')
    
def curseur(connec):
    cur = connec.cursor()

def deconnection(connec):
    connec.close()
    connec.commit
    
def execution(v):
    cur = connec.cursor()
    cur.execute(v)
    