# Step 1: Define the values from the confusion matrix
TP = 762  # True Positives for Cancerous
FP = 10   # False Positives for Cancerous
FN = 15   # False Negatives for Cancerous
TN = 93   # True Negatives for Cancerous

# Step 2: Calculate Precision for each class
def precision(tp, fp):
    return tp / (tp + fp)

# Calculate Precision for Cancerous
precision_cancerous = precision(TP, FP)
print(f"Precision for Cancerous: {precision_cancerous * 100:.2f}%")

# Calculate Precision for Normal
precision_normal = precision(TN, FN)
print(f"Precision for Normal: {precision_normal * 100:.2f}%")

# Step 3: Calculate Recall for each class
def recall(tp, fn):
    return tp / (tp + fn)

# Calculate Recall for Cancerous
recall_cancerous = recall(TP, FN)
print(f"Recall for Cancerous: {recall_cancerous * 100:.2f}%")

# Calculate Recall for Normal
recall_normal = recall(TN, FP)
print(f"Recall for Normal: {recall_normal * 100:.2f}%")

# Step 4: Calculate F1-Score for each class
def f1_score(precision, recall):
    return 2 * (precision * recall) / (precision + recall)

# Calculate F1-Score for Cancerous
f1_cancerous = f1_score(precision_cancerous, recall_cancerous)
print(f"F1-Score for Cancerous: {f1_cancerous * 100:.2f}%")

# Calculate F1-Score for Normal
f1_normal = f1_score(precision_normal, recall_normal)
print(f"F1-Score for Normal: {f1_normal * 100:.2f}%")

# Step 5: Calculate Overall Accuracy
def accuracy(tp, tn, fp, fn):
    return (tp + tn) / (tp + tn + fp + fn)

# Calculate Overall Accuracy
overall_accuracy = accuracy(TP, TN, FP, FN)
print(f"Overall Accuracy: {overall_accuracy * 100:.2f}%")