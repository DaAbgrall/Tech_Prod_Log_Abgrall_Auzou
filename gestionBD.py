import sqlite3 as lite
import sys

def connection():
    return sqlite3.connect('projet.db')


def curseur():
    return self.cursor()


def deconnection(connec):
    connec.close()
    connec.commit

def execution(v):
    cur = connec.cursor()
    cur.execute(v)
