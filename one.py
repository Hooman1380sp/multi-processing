from multiprocessing import Process
from time import perf_counter, sleep

start_perf_counter = perf_counter()


def show_name(name):
    print(f"starting {name}")
    sleep(3)
    print(f"finishing {name}")


p1 = Process(target=show_name, args=("One",))
p2 = Process(target=show_name, args=("Tow",))

p1.start()
p2.start()

p1.join()
p2.join()

end_perf_counter = perf_counter()

print(round(end_perf_counter - start_perf_counter))
