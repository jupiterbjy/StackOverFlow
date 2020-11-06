import math
import timeit
from concurrent import futures
import multiprocessing


def run(i):
    i = i * math.pi
    return i ** 2


def wrapper_sequential():
    return [run(i) for i in range(20000)]


def wrapper_thread_pool():
    with futures.ThreadPoolExecutor(max_workers=10) as exc:
        fut = [exc.submit(run, i) for i in range(20000)]
        output = [f.result() for f in fut]

    return output


def wrapper_multiprocess():
    with multiprocessing.Pool(10) as pool:
        output = pool.map(run, (i for i in range(20000)))

    return output


if __name__ == '__main__':
    print(f"Thr: {timeit.timeit(wrapper_thread_pool, number=10):.4}")
    print(f"Seq: {timeit.timeit(wrapper_sequential, number=10):.4}")
    print(f"Mlt: {timeit.timeit(wrapper_multiprocess, number=10):.4}")
