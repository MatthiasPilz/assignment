import time


def num_integral(f, x0, x1, n):
    del_x = (x1-x0) / n
    result = 0.0
    for i in range(1, n):
        x = x0 + del_x*i
        result += f(x)
    result = 0.5*del_x*(f(x0) + f(x1) + 2.0*result)
    return result


def main():
    start = time.time()
    result = num_integral(lambda x: 3*x**2, 0.0, 1.0, 10000000)
    end = time.time()
    print(result)
    print("Took {:.5}s".format(end-start))


if __name__ == "__main__":
    main()
    # 1.000000000000076
    # Took 1.2859s