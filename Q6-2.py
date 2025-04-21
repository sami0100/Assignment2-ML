# Values for TP, FP, FN, and TN for each class
TP = {'N': 87, 'PB': 121, 'UDH': 75, 'ADH': 79, 'FEA': 148, 'DCIS': 125, 'IC': 101}
FP = {'N': 25, 'PB': 17, 'UDH': 29, 'ADH': 28, 'FEA': 15, 'DCIS': 28, 'IC': 6}
FN = {'N': 16, 'PB': 32, 'UDH': 20, 'ADH': 36, 'FEA': 37, 'DCIS': 26, 'IC': 9}
TN = {'N': 756, 'PB': 714, 'UDH': 760, 'ADH': 740, 'FEA': 711, 'DCIS': 705, 'IC': 768}

# Function to calculate precision, recall, accuracy, and F1-score
def calculate_metrics(class_name):
    precision = TP[class_name] / (TP[class_name] + FP[class_name]) * 100
    recall = TP[class_name] / (TP[class_name] + FN[class_name]) * 100
    accuracy = (TP[class_name] + TN[class_name]) / (TP[class_name] + TN[class_name] + FP[class_name] + FN[class_name]) * 100
    f1_score = TP[class_name] / (TP[class_name] + 0.5 * (FP[class_name] + FN[class_name])) * 100
    return precision, recall, accuracy, f1_score

# Calculate and print metrics for each class
metrics = {}
for class_name in TP:
    precision, recall, accuracy, f1_score = calculate_metrics(class_name)
    metrics[class_name] = {'Precision': precision, 'Recall': recall, 'Accuracy': accuracy, 'F1-score': f1_score}

# Print results
for class_name, values in metrics.items():
    print(f"For {class_name}:")
    print(f"Precision = {values['Precision']:.2f}%")
    print(f"Recall = {values['Recall']:.2f}%")
    print(f"Accuracy = {values['Accuracy']:.2f}%")
    print(f"F1-score = {values['F1-score']:.2f}%")
    print()

# Calculate overall accuracy
overall_accuracy = sum([metrics[class_name]['Accuracy'] for class_name in TP]) / len(TP)
print(f"Overall Accuracy = {overall_accuracy:.2f}%")