import time
import threading


def num_integral_01(f, n, expected, myid):
    x0 = 0.0
    x1 = 1.0
    del_x = (x1-x0) / n
    result = 0.0
    for i in range(1, n):
        x = x0 + del_x*i
        result += f(x)
    result = 0.5*del_x*(f(x0) + f(x1) + 2.0*result)
    print(myid, "--> error:", abs(result-expected))
    return result


def threaded(n):
    threads = []

    for i in range(n):
        t = threading.Thread(target=num_integral_01, args=(lambda x: 3*x**2, 1000000, 1.0, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


def main():
    start = time.time()
    threaded(100)
    end = time.time()
    print("Took {:.5}s".format(end-start))


if __name__ == "__main__":
    main()
    # 0 --> error: 4.785061236134425e-13
    # ... (not in order)
    # 99 --> error: 4.785061236134425e-13
    # Took 14.881s