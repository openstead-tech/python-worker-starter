"""Replace process() with your queue task; SIGTERM finishes the current iteration."""
import os
import signal
import time

running = True
def stop(signum, frame):
    global running
    running = False
signal.signal(signal.SIGTERM, stop)
signal.signal(signal.SIGINT, stop)

def process():
    print('Worker heartbeat: ready for tasks', flush=True)

if __name__ == '__main__':
    while running:
        process()
        if os.environ.get('RUN_ONCE') == '1':
            break
        for _ in range(30):
            if not running:
                break
            time.sleep(1)
