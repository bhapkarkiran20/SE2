from System.IO import FileSystemWatcher
from System.Threading import Thread

watcher = FileSystemWatcher()
watcher.Path = 'c:\\Temp'

def onChanged(source, event):
    print 'Changed:', event.ChangeType, event.FullPath

def onRenamed(source, event):
    print 'Renamed:', event.OldFullPath, event.FullPath

watcher.Changed += onChanged
watcher.Created += onChanged
watcher.Deleted += onChanged
watcher.Renamed += onRenamed

watcher.EnableRaisingEvents = True 

# wait for an hour
Thread.Sleep(60 * 1000 * 60)
