import sys

def combine_inputs(file_name1, file_name2):
    "Yoav said it's criti and Adu is still a bitch"
    combined_data = []
    return combined_data


def kmeans_plus_initialization(data_points):
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
        K = int(float(K))
        iter_limit = int(float(iter_limit))
        epsilon = float(epsilon)
        initialization_centroids = kmeans_plus_initialization(data_points)
        """
        Call C code and do shit
        """
    except Exception as e:
        print("An Error Has Occurred")



if __name__ == "__main__":
    main()
