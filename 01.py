import random
import timeit
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr, pivot_type="middle"):
    if len(arr) < 2:
        return arr
    if pivot_type == "first":
        pivot = arr[0]
    elif pivot_type == "last":
        pivot = arr[-1]
    elif pivot_type == "middle":
        pivot = arr[len(arr) // 2]
    else:
        raise ValueError("Invalid pivot type")
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def timsort(arr):
    return arr.sort()


def array_gemerator(n):
    return [random.randint(0, n) for _ in range(n)]


def measure_time(func, *args):
    execution_time = timeit.timeit(lambda: func(*args), number=5)
    return execution_time


def plot_results(results):
    x = [x for x in results.keys()]
    randomized_quick_sort_time = [
        results[x]["randomized_quick_sort"] for x in results.keys()
    ]
    deterministic_quick_sort_first_time = [
        results[x]["deterministic_quick_sort_first"] for x in results.keys()
    ]
    deterministic_quick_sort_last_time = [
        results[x]["deterministic_quick_sort_last"] for x in results.keys()
    ]
    deterministic_quick_sort_middle_time = [
        results[x]["deterministic_quick_sort_middle"] for x in results.keys()
    ]
    tim_sort_time = [results[x]["tim_sort"] for x in results.keys()]

    plt.plot(x, randomized_quick_sort_time, label="randomized_quick_sort")
    plt.plot(
        x,
        deterministic_quick_sort_first_time,
        label="deterministic_quick_sort (pivot: first)",
    )
    plt.plot(
        x,
        deterministic_quick_sort_last_time,
        label="deterministic_quick_sort (pivot: last)",
    )
    plt.plot(
        x,
        deterministic_quick_sort_middle_time,
        label="deterministic_quick_sort (pivot: middle)",
    )
    plt.plot(x, tim_sort_time, label="tim_sort")
    plt.xlabel("Array length")
    plt.ylabel("Execution time (s)")
    plt.title("Deterministic vs Randomized Quick Sort")
    plt.legend()
    plt.show()


def main():
    arrays_len = [10000, 100000, 500000, 5000000, 10000000]
    measure_results = {}
    for n in arrays_len:
        arr = array_gemerator(n)
        print(f"Розмір масиву: {n}")
        randomized_quick_sort_time = measure_time(randomized_quick_sort, arr)
        deterministic_quick_sort_time_first = measure_time(
            deterministic_quick_sort, arr, "first"
        )
        deterministic_quick_sort_time_last = measure_time(
            deterministic_quick_sort, arr, "last"
        )
        deterministic_quick_sort_time_middle = measure_time(
            deterministic_quick_sort, arr, "middle"
        )
        tim_sort_time = measure_time(timsort, arr)
        print(
            "Час виконання randomized_quick_sort:",
            round(randomized_quick_sort_time, 4),
            " секунд",
        )
        print(
            "Час виконання deterministic_quick_sort (перший елемент):",
            round(deterministic_quick_sort_time_first, 4),
            " секунд",
        )
        print(
            "Час виконання deterministic_quick_sort (останній елемент):",
            round(deterministic_quick_sort_time_last, 4),
            " секунд",
        )
        print(
            "Час виконання deterministic_quick_sort (середній елемент):",
            round(deterministic_quick_sort_time_middle, 4),
            " секунд",
        )
        print("Час виконання tim_sort:", round(tim_sort_time, 4), " секунд")
        print("-" * 80)
        measure_results[n] = {
            "randomized_quick_sort": randomized_quick_sort_time,
            "deterministic_quick_sort_first": deterministic_quick_sort_time_first,
            "deterministic_quick_sort_last": deterministic_quick_sort_time_last,
            "deterministic_quick_sort_middle": deterministic_quick_sort_time_middle,
            "tim_sort": tim_sort_time,
        }
    # print(measure_results)
    plot_results(measure_results)


if __name__ == "__main__":
    main()
