# Data for train samples
train_samples = [
    {'soil_type': 1, 'rainfall': 350, 'temp': 22, 'crop': 'wheat'},
    {'soil_type': 2, 'rainfall': 600, 'temp': 30, 'crop': 'rice'},
    {'soil_type': 1, 'rainfall': 400, 'temp': 24, 'crop': 'wheat'},
    {'soil_type': 2, 'rainfall': 750, 'temp': 32, 'crop': 'rice'},
    {'soil_type': 1, 'rainfall': 370, 'temp': 23, 'crop': 'wheat'},
    {'soil_type': 2, 'rainfall': 780, 'temp': 33, 'crop': 'rice'},
    {'soil_type': 1, 'rainfall': 420, 'temp': 25, 'crop': 'wheat'},
    {'soil_type': 2, 'rainfall': 700, 'temp': 31, 'crop': 'rice'},
    {'soil_type': 1, 'rainfall': 390, 'temp': 22, 'crop': 'wheat'},
    {'soil_type': 2, 'rainfall': 770, 'temp': 30, 'crop': 'rice'},
]

# Data for test samples
test_samples = [
    {'soil_type': 1, 'rainfall': 360, 'temp': 22},  # Test Tuple 1
    {'soil_type': 2, 'rainfall': 720, 'temp': 31},  # Test Tuple 2
]

# Min-Max Normalization Constants
rainfall_min = 350
rainfall_max = 780
temp_min = 22
temp_max = 33


# Normalize function for Min-Max normalization
def normalize(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)


# Normalize train samples and print results
print("Normalized Train Dataset:\n")
for sample in train_samples:
    sample['n_rainfall'] = normalize(sample['rainfall'], rainfall_min, rainfall_max)
    sample['n_temp'] = normalize(sample['temp'], temp_min, temp_max)
    print(f"Soil Type: {sample['soil_type']} | Rainfall: {sample['rainfall']} | Temp: {sample['temp']} "
          f"| Normalized Rainfall: {sample['n_rainfall']:.4f} | Normalized Temp: {sample['n_temp']:.4f}")
print("\n")

# Normalize test samples and print results
print("Normalized Test Samples:\n")
for sample in test_samples:
    sample['n_rainfall'] = normalize(sample['rainfall'], rainfall_min, rainfall_max)
    sample['n_temp'] = normalize(sample['temp'], temp_min, temp_max)
    print(f"Soil Type: {sample['soil_type']} | Rainfall: {sample['rainfall']} | Temp: {sample['temp']} "
          f"| Normalized Rainfall: {sample['n_rainfall']:.4f} | Normalized Temp: {sample['n_temp']:.4f}")
print("\n")


# Function to calculate Euclidean distance
def euclidean_distance(test_tuple, train_tuple):
    n_rainfall = abs(test_tuple['n_rainfall'] - train_tuple['n_rainfall'])
    n_temp = abs(test_tuple['n_temp'] - train_tuple['n_temp'])
    return (n_rainfall * 2 + n_temp * 2) ** 0.5


# Calculate and print Euclidean distances for Test Tuple 1
print("Calculating Euclidean Distances for Test Tuple 1:\n")
distances_1 = []
for sample in train_samples:
    distance = euclidean_distance(test_samples[0], sample)
    distances_1.append({'crop': sample['crop'], 'distance': distance})
    print(f"Crop: {sample['crop']} | Distance: {distance:.4f}")
print("\n")

# Calculate and print Euclidean distances for Test Tuple 2
print("Calculating Euclidean Distances for Test Tuple 2:\n")
distances_2 = []
for sample in train_samples:
    distance = euclidean_distance(test_samples[1], sample)
    distances_2.append({'crop': sample['crop'], 'distance': distance})
    print(f"Crop: {sample['crop']} | Distance: {distance:.4f}")
print("\n")


# Function to get K nearest neighbors and calculate majority class (for K=3)
def get_knn(distances, k=3):
    distances.sort(key=lambda x: x['distance'])  # Sort by distance
    return distances[:k]  # Get K nearest neighbors


# Predict crop for Test Tuple 1 based on Euclidean distances
print("Ranked Euclidean Distances for Test Tuple 1:")
nearest_neighbors_1 = get_knn(distances_1, k=3)
for idx, neighbor in enumerate(nearest_neighbors_1):
    print(f"Rank {idx + 1}: Crop = {neighbor['crop']} | Distance = {neighbor['distance']:.4f}")


# Predict crop for Test Tuple 1
def predict_crop(nearest_neighbors):
    crops = [neighbor['crop'] for neighbor in nearest_neighbors]
    crop_prediction = max(set(crops), key=crops.count)
    return crop_prediction


prediction_1 = predict_crop(nearest_neighbors_1)
print(f"\nPrediction for Test Tuple 1: {prediction_1}\n")

# Predict crop for Test Tuple 2 based on Euclidean distances
print("Ranked Euclidean Distances for Test Tuple 2:")
nearest_neighbors_2 = get_knn(distances_2, k=3)
for idx, neighbor in enumerate(nearest_neighbors_2):
    print(f"Rank {idx + 1}: Crop = {neighbor['crop']} | Distance = {neighbor['distance']:.4f}")

# Predict crop for Test Tuple 2
prediction_2 = predict_crop(nearest_neighbors_2)
print(f"\nPrediction for Test Tuple 2: {prediction_2}")
