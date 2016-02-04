import sqlite3 as lite
import sys

def connection():
    connec = lite.connect('projet.db')
    
def curseur():
    cur = connec.cursor()

def deconnection():
    connec.close()
    
def execution(v):
    cur = connec.cursor()
    cur.execute(v)
    