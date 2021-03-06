import time
import multiprocessing


def num_integral_01(f, n, expected, myid):
    x0 = 0.0
    x1 = 1.0
    del_x = (x1-x0) / n
    result = 0.0
    for i in range(1, n):
        x = x0 + del_x*i
        result += f(x)
    result = 0.5*del_x*(f(x0) + f(x1) + 2.0*result)
    # print(myid, "--> error:", abs(result-expected))
    return result


def multiproc(n):
    processes = []

    for i in range(n):
        p = multiprocessing.Process(target=num_integral_01, args=(lambda x: 3*x**2, 1000000, 1.0, i))
        processes.append(p)
        p.start()

    for t in processes:
        t.join()


def main():
    start = time.time()
    multiproc(100)
    end = time.time()
    # print("Took {:.5}s".format(end-start))
    return end-start


if __name__ == "__main__":
    t = 0
    m = 100
    for i in range(m):
        t += main()
        print(str(i) + " ", end='')
    print("Took: {:.5}s on average over {} runs".format(t/m, m))
    # 0 1 ... 99 Took: 1.9376s on average over 100 runs

    # comparing to the sequential results: 12.838s
    # 12.838 / 8 = 1.605  ==>  multiprocessing results in almost linear speedup with the number of available cores
