from ast import literal_eval


if __name__ == '__main__':
    with open('selected_cities.txt', 'r') as file:
        selected_cities = literal_eval(file.read())

    with open('fictional_radio_stations.txt', 'r') as file:
        fictional_radio_stations = literal_eval(file.read())

    with open('station_coverage.txt', 'r') as file:
        station_coverage = literal_eval(file.read())

    cities_needed = selected_cities.copy()
    print(f'Cities Needed: {cities_needed}')

    selected_stations = set()
    while cities_needed:
        best_station = None
        cities_covered = set()

        # search for the next best station
        for station, cities_for_station in station_coverage.items():
            covered = cities_needed & cities_for_station

            if len(covered) > len(cities_covered):  # a 'good' station
                best_station = station
                cities_covered = covered

        cities_needed -= cities_covered  # remove cities we have covered
        selected_stations.add(best_station)  # selected this 'good' station

    print(f'Best Stations: {sorted(selected_stations)}')
    # print coverage cities from the selected stations
    for station in sorted(selected_stations):
        print(f'{station} covers {sorted(station_coverage[station])}')
