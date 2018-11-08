#!/usr/bin/python

import threading
import time
import webbrowser

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter,s):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.string = s
      self.counter = counter

   def run(self):
      chrome_path = '/Users/user/Documents/patent_code/match_2_SBIR_to_patents/chromedriver'
      print "Starting " + self.name
      threadLock.acquire()
      print_time(self.name,self.string, self.counter, 1)
      url = "https://www.google.com/patents/US3638502A/"
      print self.string
      webbrowser.open(url)
      threadLock.release()

def print_time(threadName,string, delay, counter):
   while counter:
      time.sleep(delay)
      print "%s: %s :%s" % (threadName, time.ctime(time.time()), string)
      counter -= 1

threadLock = threading.Lock()
threads = []
str1 = "This is us"
str2 = "This is them"

# Create new threads
thread1 = myThread(1, "Thread-1", 1,str1)
thread2 = myThread(2, "Thread-2", 2,str2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    print "Here"
    t.join()
print "Exiting Main Thread"