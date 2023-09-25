from ast import literal_eval
import itertools


def power_set(input_set):
    # base case: the empty set has only one subset, the empty set
    if len(input_set) == 0:
        return [[]]

    # recursion case: take an element from the set
    subsets = []
    first_element = input_set[0]
    for subset in power_set(input_set[1:]):
        subsets.append(subset)
        subsets.append([first_element] + subset)

    return subsets


if __name__ == '__main__':
    with open('selected_cities.txt', 'r') as file:
        selected_cities = literal_eval(file.read())

    with open('fictional_radio_stations.txt', 'r') as file:
        fictional_radio_stations = literal_eval(file.read())

    with open('station_coverage.txt', 'r') as file:
        stations = literal_eval(file.read())

    # print(f'selected_cities: {selected_cities}')
    # print(f'fictional_radio_stations: {fictional_radio_stations}')
    # print(f'station_coverage: {stations}')

    cities_needed = selected_cities.copy()
    # print(f'cities_needed: {sorted(cities_needed)}')

    # all_subsets = power_set(list(fictional_radio_stations))
    # print(f'all_subsets: {all_subsets}')

    all_subsets = []
    for i in range(1, len(fictional_radio_stations) + 1):
        combination = itertools.combinations(fictional_radio_stations, i)
        all_subsets += list(combination)

    print(f'all_subsets: {all_subsets}')

    best_stations = []
    for subset in all_subsets:
        covered = set()
        for station in subset:
            covered |= stations[station]
        if covered == cities_needed:
            best_stations = subset
            break

    print(f'Best Stations: {sorted(best_stations)}')

    # print coverage cities from the best station
    for station in sorted(best_stations):
        print(f'{station} covers {stations[station]}')
