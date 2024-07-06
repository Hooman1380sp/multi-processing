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


start_perf_counter = perf_counter()


def show_name(name):
    print(f"starting {name}")
    sleep(3)
    print(f"finishing {name}")


p1 = Process(target=show_name, args=("One",), name="One", daemon=True)
p2 = Process(target=show_name, args=("Tow",), name="Tow", daemon=True)

p1.start()
p2.start()

p1.terminate()
p2.kill()

p1.join()
p2.join()

print(p1.exitcode)
print(p2.exitcode)
end_perf_counter = perf_counter()

print(round(end_perf_counter - start_perf_counter))
