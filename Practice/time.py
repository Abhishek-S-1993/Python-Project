import time

count_seconds = 5
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='****', flush=True)
        time.sleep(1)
    else:
        print('Start')