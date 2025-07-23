import random

from itertools import combinations
import time


def knapsack_combinations(items, capacity):
    max_value = 0
    best_combination = []
    for i in range(1, len(items) + 1):
        # Generate all combinations of items of length i
        for combination in combinations(items, i):
            total_weight = 0
            total_value = 0
            for x in combination:
                total_weight += x[0]
                total_value += x[1]
            if total_weight <= capacity and total_value > max_value:
                max_value = total_value
                best_combination = combination

    return max_value, best_combination



def knapsack_heuristic(items, capacity):
    # TODO: Crear método de búsqueda heurística, comparar tiempos y calidad de solución
    return


def generate_knapsack_example(num_items, max_weight, max_value):
    """Generate a random knapsack problem instance.

    """
    items = []
    for i in range(num_items):
        weight = random.randint(1, max_weight)
        value = random.randint(1, max_value)
        items.append((weight, value))

    capacity = random.randint(max_weight // 2, max_weight)

    return items, capacity


def main():
    max_weight = 20
    max_value = 100
    for n in range(5, 50, 5):
        items, capacity = generate_knapsack_example(n, max_weight, max_value)
        print(f'Generated Knapsack Input: size {n}')
        print(f"Capacity {capacity}")
        print(f"Items {items}")

        time_init = time.perf_counter()
        max_value, best_combination = knapsack_combinations(items, capacity)
        time_end = time.perf_counter()
        print(f"Best value possible: {max_value} with items {best_combination}")
        print(f"Solved in {time_end - time_init:.4f} seconds")


if __name__ == "__main__":
    main()
