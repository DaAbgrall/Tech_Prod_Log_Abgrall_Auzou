import sqlite3 as lite
import sys

def connection():
    return sqlite3.connect('projet.db')
    
def curseur():
    return connec.cursor()

def deconnection():
    connec.close()
    
def execution(v):
    cur = connec.cursor()
    cur.execute(v)
    