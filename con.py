import sys
import os, time
import sqlite3 as lite

try:
  con = lite.connect('test5.db')
  cur = con.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS File_Collection (FileName TEXT, PRIORITY INT, File_Data TEXT)")
  def add_into_Databse(Added):
   prio=[] 
   for f in Added:
         f=f.split('.')
         prio.append(f[-1:])
   prio=sorted(prio)
   for p in prio:
       for f in Added:
            f2=f
            f=f.split('.')
            if p==f[-1:]:
              f1=open(f2,'r+')
              f1=f1.readlines()
              cur.execute('''INSERT INTO File_Collection VALUES(?,?,?)''',(str(f2),int(p[0]),str(f1)))             
              print str(f2)
              print int(p[0])
              print str(f1)
   con.commit()
   cur.execute('SELECT* FROM File_Collection')

   for entry in cur:
        print entry

except Exception as e:
    con.rollback()
    raise e

def get_Priority(Added):
    
     nAdded=[]
     for i in range(0,len(Added)):
        nFile=''
        nFile=Added[i].strip()
        print "PRIORITY FOR %s"%(Added[i])
        P=raw_input()
        nFile+='.'
        nFile+=P
        nAdded.append(nFile)
        os.rename(Added[i],nFile)
        
     return nAdded
        
         

path_to_watch = "."
Before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (2)
  After = dict ([(f, None) for f in os.listdir (path_to_watch)])
  Added = [f for f in After if not f in Before]
  Added=get_Priority(Added)
  add_into_Databse(Added)
  Removed = [f for f in Before if not f in After]
#  if Added: print "Added: ", ", ".join (Added)
 # if Removed: print "Removed: ", ", ".join (Removed)
  Before = After		
  for f in Added:
      Before[f]=None
       

