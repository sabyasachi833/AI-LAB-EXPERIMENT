
from itertools import permutations


def travelling_salesman(distance):
    n = len(distance)
    start = 0
    cities = list(range(1, n))

    minimum_cost = float("inf")
    best_route = None

    for perm in permutations(cities):
        current_city = start
        current_cost = 0
        route = [start]

        for city in perm:
            current_cost += distance[current_city][city]
            current_city = city
            route.append(city)

        # Return to the starting city
        current_cost += distance[current_city][start]
        route.append(start)

        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_route = route

    return best_route, minimum_cost


if __name__ == "__main__":
    distance = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    route, cost = travelling_salesman(distance)

    print("Best route:")
    for city in route:
        print(chr(65 + city), end=" ")

    print("\nMinimum Distance:", cost)
