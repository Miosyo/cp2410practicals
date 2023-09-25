

def euclidean_distance(feature1, feature2):
    return ((feature1[0] - feature2[0]) ** 2 + (feature1[1] - feature2[1]) ** 2) ** 0.5


def knn_classify(features, chosen_feature, k):
    # create a list of distances
    distances = []
    for feature in features:
        distance = round(euclidean_distance(feature, chosen_feature), 2)
        name = feature[2]
        distances.append((distance, name))
    distances.sort()
    k_nearest_labels = distances[:k]
    return max(set(k_nearest_labels), key=k_nearest_labels.count)


def knn_predict_weight(features, chosen_feature, k):
    distances = []

    for feature in features:
        distance = round(euclidean_distance(feature, chosen_feature), 2)
        weight = feature[0]
        distances.append((distance, weight))

    distances.sort()
    k_nearest_labels = distances[:k]
    return round(sum([label[1] for label in k_nearest_labels]) / k, 2)


if __name__ == '__main__':
    labeled_features = [
        [140, 6, "grapefruit"],
        [170, 5.5, "grapefruit"],
        [220, 7, "grapefruit"],
        [260, 7.5, "grapefruit"],
        [300, 9, "grapefruit"],
        [400, 10, "grapefruit"],
        [140, 6.5, "orange"],
        [170, 7, "orange"],
        [200, 8, "orange"],
        [240, 7.5, "orange"],
        [280, 8, "orange"],
        [300, 9, "orange"]
    ]

    test_data = [
        [150, 6.5],  # orange
        [170, 7.5],  # orange
        [250, 7],  # orange
        [300, 8],  # grapefruit
        [350, 9],  # grapefruit
        [400, 9.5],  # grapefruit
        [200, 6],  # orange
        [250, 7],  # orange
        [350, 8],  # grapefruit
        [400, 9],  # orange
        [450, 10],  # grapefruit
        [500, 11]  # grapefruit
    ]

    print('K-Nearest Neighbor')
    for i in range(len(test_data)):
        print(knn_classify(labeled_features,
              test_data[i], 4))

    print('K-Nearest Average')
    for i in range(len(test_data)):
        print(knn_predict_weight(labeled_features,
              test_data[i], 4))
