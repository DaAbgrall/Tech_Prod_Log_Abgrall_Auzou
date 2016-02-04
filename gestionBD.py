import sqlite3 as lite
import sys

def connection():
    connec = lite.connect('test.db')
    
def curseur():
    cur = connec.cursor()

def deconnection():
    connec.close()
    
def execution(v):
    cur.execute(v)
    