import os, time,sqlite3
con = sqlite3.connect( "record.db" )
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS database (filename TEXT,priority INT,content TEXT)''')



path_to_watch = "."
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (2)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])

  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]

  if added: print "Added: ", ", ".join (added)
  if removed: print "Removed: ", ", ".join (removed)
  before = after	

con.commit()
  
