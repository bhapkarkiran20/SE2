import sys
import os, time
import sqlite3 as lite
import shutil



try:
  con = lite.connect('test5.db')
  cur = con.cursor()
  con1 = lite.connect('test6.db')
  cur1 = con1.cursor()
  cur1.execute("CREATE TABLE IF NOT EXISTS Compress_Collection (Data TEXT, Hash_value TEXT)")
       
  con.commit()
  con1.commit()
except Exception as e:
    con.rollback()
    raise e




try:
  con = lite.connect('test5.db')
  cur = con.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS File_Collection (FileName TEXT, PRIORITY INT, File_Data TEXT)")
  def add_into_Databse(Added):
   prio=[] 
   for f in Added:
         f=f.split('.')         
         prio.append(f.pop())
        
         
   prio.sort()
   for p in prio:
       for f in Added:
            f2='.'
            f2+=p
            f3=f 
            f3=f3.replace(f2,'')
            print f3
            print f2
            f=f.split('.')
            if p==f.pop():
              f1=open(f3,'r')
              f1=f1.readlines()
              cur.execute('''INSERT INTO File_Collection VALUES(?,?,?)''',(str(f3),int(p),str(f1)))             

   
   con.commit()
   #cur.execute('SELECT FileName FROM File_Collection')
   #for i in cur:
    #    print i  
   '''request=raw_input("Do You want to Change Priority OF Existing File in Database(Y/N):")
   if request=='Y' or request=='y':
      file_name=raw_input("Enter File Name:")
      cur.execute('SELECT FileName FROM File_Collection')
      if file_name in cur:
        p_req=raw_input('Enter New Priority:')
      '''     

except Exception as e:
    con.rollback()
    raise e



  
def copyfileobj_example(source, dest, buffer_size=1024*1024):
   
    while 1:
        copy_buffer = source.read(buffer_size)
        if not copy_buffer:
            break
        dest.write(copy_buffer)

def copyfile_example(source, dest):
    with open(source, 'rb') as src, open(dest, 'wb') as dst:
        copyfileobj_example(src, dst)

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
        copyfile_example(Added[i], nFile)
        os.chmod(Added[i], 0444)
        
        
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
       

