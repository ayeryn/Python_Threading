import threading
import time
import logging
import random

#We're using loggin to debug. Logging is thread-safe, so messages from different threads are kept distinct in the output.
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def try_lock_acquire(lock):
    logging.debug('Starting')
    num_tries = 0
    while num_tries < 2:
        time.sleep(0.5)
        logging.debug('Trying to acquire')
        have_it = lock.acquire(0)
        try:
            num_tries += 1
            if have_it:
                logging.debug('Iteration %d: Acquired',  num_tries)
            else:
                logging.debug('Iteration %d: Not acquired', num_tries)
        finally:
            if have_it:
                lock.release()
                logging.debug('Iteration %d: Lock released', num_tries)
    logging.debug('Done after %d iterations', num_tries)


lock = threading.Lock()

thread1 = threading. Thread(target=try_lock_acquire, args=(lock,), name='thread1')
thread1.start()
thread2 = threading. Thread(target=try_lock_acquire, args=(lock,), name='thread2')
thread2.start()

# (thread1  ) Starting
# (thread2  ) Starting
# (thread1  ) Trying to acquire
# (thread2  ) Trying to acquire
# (thread1  ) Iteration 1: Acquired
# (thread2  ) Iteration 1: Not acquired
# (thread1  ) Iteration 1: Lock released
# (thread2  ) Trying to acquire
# (thread1  ) Trying to acquire
# (thread2  ) Iteration 2: Acquired
# (thread1  ) Iteration 2: Not acquired
# (thread2  ) Iteration 2: Lock released
# (thread1  ) Done after 2 iterations
# (thread2  ) Done after 2 iterations