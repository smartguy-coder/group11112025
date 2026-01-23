import threading


import time


def worker(num):
    time.sleep(num)
    print(num, f"Worker {num}")
    return f"Worker {num}"

threads = []

for i in range(10):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

print(888888)