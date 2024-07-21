import sys
import pandas as pd
import numpy as np
import math


def combine_inputs(file_name1, file_name2):
    data_points1 = pd.read_csv(file_name1)
    data_points2 = pd.read_csv(file_name2)
    combined_data_points = pd.merge(data_points1, data_points1, on=data_points1.columns[0])
    combined_data_points = combined_data_points.sort_values(by=data_points1.columns[0])
    return combined_data_points


def kmeans_plus_initialization(data_points, K):
    centroids = []
    centroids_indices = []
    return centroids, centroids_indices


def validity_check(K, iter_limit, epsilon, file_name1, file_name2):
    try:
        if not float(K) == float(int(float(K))):
            print("Invalid number of clusters!")
            return 0
    except Exception as e:
        print("Invalid number of clusters!")
        return 0
    K = int(float(K))

    try:
        if not float(iter_limit) == float(int(float(iter_limit))):
            print("Invalid maximum iteration!")
            return 0
    except Exception as e:
        print("Invalid maximum iteration!")
        return 0
    iter_limit = int(float(iter_limit))

    try:
        if not float(epsilon) >= 0.0:
            print("Invalid epsilon!")
            return 0
    except Exception as e:
        print("Invalid epsilon!")
        return 0

    if not 1 < iter_limit < 1000:
        print("Invalid maximum iteration!")
        return 0
    data_points = combine_inputs(file_name1, file_name2)
    vectors_count = len(data_points)
    if not 1 < K < vectors_count:
        print("Invalid number of clusters!")
        return 0
    return data_points


def calculate_euclidean_distance(vector1, vector2):
    sum = 0
    for i in range(len(vector1)):
        sum += math.pow(vector1[i] - vector2[i], 2)
    return math.sqrt(sum)


def parse_arguments():
    if len(sys.argv) == 6:
        K = sys.argv[1]
        iter_limit = sys.argv[2]
        epsilon = sys.argv[3]
        file_name1 = sys.argv[4]
        file_name2 = sys.argv[5]
        return K, iter_limit, epsilon, file_name1, file_name2
    elif len(sys.argv) == 5:
        K = sys.argv[1]
        iter_limit = 300
        epsilon = sys.argv[2]
        file_name1 = sys.argv[3]
        file_name2 = sys.argv[4]
        return K, iter_limit, epsilon, file_name1, file_name2


def main():
    K, iter_limit, epsilon, file_name1, file_name2 = parse_arguments()
    try:
        data_points = validity_check(K, iter_limit, epsilon, file_name1, file_name2)
        if data_points == 0:
            print("An Error Has Occurred")
            return
        data_points = data_points.iloc[:, 1:].to_numpy()
        print(data_points)
        K = int(float(K))
        iter_limit = int(float(iter_limit))
        epsilon = float(epsilon)
        initialization_centroids = kmeans_plus_initialization(data_points, K)
        """
        Call C code and do shit
        """
    except Exception as e:
        print("An Error Has Occurred")


if __name__ == "__main__":
    main()
