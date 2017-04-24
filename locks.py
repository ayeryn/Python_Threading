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

		""" a tread calling .acquire() will hold the lock if the lock currently has no other treads holding it"""
		""" The floating-point argument will cause the thread to block for at most the number of seconds specified by timeout
		and as long as the lock cannot be acquired. """
		""" Returns true if the lock has been acquired, false if the timeout has elapsed."""
		have_it = lock.acquire(0)
		try:
			if have_it:
				logging.debug('Iteration %d: Acquired',  i+1)
			else:
				logging.debug('Iteration %d: Not acquired', i+1)
		finally:
			if have_it:
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
# (thread1  ) Done after 1 iterations
# (thread2  ) Trying to acquire
# (thread1  ) Trying to acquire
# (thread2  ) Iteration 2: Acquired
# (thread1  ) Iteration 2: Not acquired
# (thread2  ) Iteration 2: Lock released
# (thread2  ) Done after 2 iterations