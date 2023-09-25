def calculate_distance(first, second):
    total = 0
    for i in range(len(second)):
        total += (first[i] - second[i]) ** 2
    return total ** 0.5


def predict_loaves(features_and_loaves, todays_features, k):
    distances = []

    for item in features_and_loaves:
        distance = calculate_distance(item, todays_features)
        distances.append((distance, item[-1]))
    distances.sort()
    nearest_neighbors = distances[:k]
    return round(sum([neighbor[1] for neighbor in nearest_neighbors]) / k, 2)


if __name__ == '__main__':
    training_data = [
        [5, 1, 0, 300],
        [3, 1, 1, 225],
        [1, 1, 0, 75],
        [4, 0, 1, 200],
        [4, 0, 0, 150],
        [2, 0, 0, 50]
    ]

    test_cases = [
        [5, 1, 0],
        [3, 1, 1],
        [1, 1, 0],
        [4, 0, 1],
        [4, 0, 0],
        [2, 0, 0],
        [4, 1, 0]  # This should predict 228.75 loaves! I got 218.75 @ k=4
    ]

    print('Loaf Prediction')
    for i in range(1, len(training_data)):
        print(f'K= {i}')
        for j in range(len(test_cases)):
            print(predict_loaves(training_data, test_cases[j], i))
