import time
from multiprocessing import Process, current_process
from time import perf_counter, sleep

#
# start_perf_counter = perf_counter()
#
#
# def show_name(name):
#     print(f"starting {name}")
#     sleep(3)
#     print(current_process().ident)
#     print(current_process().name)
#     print(current_process().pid)
#     print(current_process())
#     print(f"finishing {name}")
#
#
# p1 = Process(target=show_name, args=("One",), name="One")
# p2 = Process(target=show_name, args=("Tow",), name="Tow")
#
# p1.start()
# p2.start()
#
# print(p1.is_alive())
#
# p1.join()
# p2.join()
#
# end_perf_counter = perf_counter()
#
# print(round(end_perf_counter - start_perf_counter))


# -------------
# daemon

# start_perf_counter = perf_counter()
#
#
# def show_name(name):
#     print(f"starting {name}")
#     sleep(3)
#     print(f"finishing {name}")
#
#
# p1 = Process(target=show_name, args=("One",), name="One", daemon=True)
# p2 = Process(target=show_name, args=("Tow",), name="Tow", daemon=True)
#
# p1.daemon = False
# p1.start()
# p2.start()
#
# end_perf_counter = perf_counter()
#
# print(round(end_perf_counter - start_perf_counter))

# ----------------
# kill, terminate


# start_perf_counter = perf_counter()
#
#
# def show_name(name):
#     print(f"starting {name}")
#     sleep(3)
#     print(f"finishing {name}")
#
#
# p1 = Process(target=show_name, args=("One",), name="One", daemon=True)
# p2 = Process(target=show_name, args=("Tow",), name="Tow", daemon=True)
#
# p1.start()
# p2.start()
#
# p1.terminate()
# p2.kill()
#
# p1.join()
# p2.join()
#
# print(p1.exitcode)
# print(p2.exitcode)
# end_perf_counter = perf_counter()
#
# print(round(end_perf_counter - start_perf_counter))

# Queue, memory isolation

# Queue
# from multiprocessing import Queue
#
# numbers = list()
#
# qs = Queue()
# qs.put(numbers)
#
#
# def one_func(queue):
#     numbers = queue.get()
#     numbers.extend([1, 2, 3])
#     queue.put(numbers)
#     print(numbers)
#
#
# def tow_func(queue):
#     numbers = queue.get()
#     numbers.extend([4, 5, 6])
#     queue.put(numbers)
#     print(numbers)
#
#
# p1 = Process(target=one_func, args=(qs,))
# p2 = Process(target=tow_func, args=(qs,))
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()
#
# print(qs.get())

# memory isolation

# numbers = list()
#
#
# def one_func():
#     global numbers
#     numbers.extend([1, 2, 3])
#     print(numbers)
#
#
# def tow_func():
#     global numbers
#     numbers.extend([4, 5, 6])
#     print(numbers)
#
#
# p1 = Process(target=one_func)
# p2 = Process(target=tow_func)
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()
#
# print(numbers)


# Poll

# from multiprocessing.pool import Pool
# from multiprocessing import cpu_count
#
#
# def init():
#     print("start process")
#
#
# def show(name):
#     print(f"starting {name}")
#     time.sleep(3)
#     print(f"finishing {name}")
#
#
# names = ["one", "two", 'three', "four", "five", "six", "seven"]
#
# pool = Pool(processes=cpu_count(), initializer=init)
# pool.map(show, names)
# pool.close()
# pool.join()
#
#
# print(cpu_count())