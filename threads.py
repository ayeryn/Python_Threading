

import threading
import time

def hello():
  print "hello"
  
threads = []

for i in range(3):

  """ create a new thread that will execute the code in the hello function """
  t = threading.Thread(target=hello)
  threads.append(t)
  // tell the thread to execute 
  t.start()
  
""" 
  Output

  hello
  hello
  hello 
  
"""

threads = []

for i in range(3):

  """ create a new thread that will execute the code in the hello function and print out the index """
  t = threading.Thread(target=hello, args=(i,)
  threads.append(t)
  // tell the thread to execute 
  t.start()
  
""" 
  Output

  hello 0
  hello 1
  hello 2
  
"""



def worker():
  print threading.currentThread().getName()
  time.sleep(2)
  print thread.currentThread().name()
  
t1 = threading.Thread(name="thread1", target=worker)
t2 = threading.Thread(name="thread2", target=worker)
t3 = threading.Thread(name="thread3", target=worker)

t1.start()
t2.start()
t3.start()
