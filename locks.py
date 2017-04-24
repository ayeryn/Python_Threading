import threading
import time
import logging
import random

#We're using loggin to debug. Logging is thread-safe, so messages from different threads are kept distinct in the output.
logging.basicConfig(level=logging.DEBUG,
	format='(%(threadName)-9s) %(message)s',)

def try_lock_acquire(lock):
	""" both threads will call this function to try to acquire the lock"""
	logging.debug('Starting')
	for i in range(2):
		time.sleep(0.5)
		logging.debug('Trying to acquire')

		""".acqire() returns false if the timeout passed in has elapsed."""
		have_it = lock.acquire(0)
		try:
			if have_it:
				""" only one thread will acquire the lock each iteration """
				logging.debug('Iteration %d: Acquired',  i+1)
			else:
				""" the thread that calles .acquire() but does not have the lock blocks"""
				logging.debug('Iteration %d: Not acquired', i+1)
		finally:
			if have_it:
				""" .release() resets the state of the lock to unlocked """
				""" one of the threads proceeds to acquire the lock """
				lock.release()
				logging.debug('Iteration %d: Lock released', i+1)
				logging.debug('Thread %s done after %d iterations', threading.currentThread().getName(), i+1)


lock = threading.Lock()

thread1 = threading. Thread(target=try_lock_acquire, args=(lock,), name='thread1')
thread1.start()
thread2 = threading. Thread(target=try_lock_acquire, args=(lock,), name='thread2')
thread2.start()


""" output will differ every time the program is run due to the nature of threads."""
# (thread1  ) Starting
# (thread2  ) Starting
# (thread1  ) Trying to acquire
# (thread2  ) Trying to acquire
# (thread1  ) Iteration 1: Acquired
# (thread2  ) Iteration 1: Not acquired
# (thread1  ) Iteration 1: Lock released
# (thread1  ) Thread thread1 done after 1 iterations
# (thread2  ) Trying to acquire
# (thread2  ) Iteration 2: Acquired
# (thread1  ) Trying to acquire
# (thread2  ) Iteration 2: Lock released
# (thread1  ) Iteration 2: Acquired
# (thread2  ) Thread thread2 done after 2 iterations
# (thread1  ) Iteration 2: Lock released
# (thread1  ) Thread thread1 done after 2 iterations