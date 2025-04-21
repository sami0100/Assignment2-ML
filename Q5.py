import math

# Step 1: Dataset (from your table)
dataset = [
    {"ID": 1, "Age": "young", "Has_Job": False, "Own_House": False, "Credit_Rating": "fair", "Class": "No"},
    {"ID": 2, "Age": "young", "Has_Job": False, "Own_House": False, "Credit_Rating": "good", "Class": "No"},
    {"ID": 3, "Age": "young", "Has_Job": True, "Own_House": False, "Credit_Rating": "good", "Class": "Yes"},
    {"ID": 4, "Age": "young", "Has_Job": True, "Own_House": True, "Credit_Rating": "fair", "Class": "Yes"},
    {"ID": 5, "Age": "young", "Has_Job": False, "Own_House": False, "Credit_Rating": "fair", "Class": "No"},
    {"ID": 6, "Age": "middle", "Has_Job": False, "Own_House": False, "Credit_Rating": "fair", "Class": "No"},
    {"ID": 7, "Age": "middle", "Has_Job": False, "Own_House": False, "Credit_Rating": "good", "Class": "No"},
    {"ID": 8, "Age": "middle", "Has_Job": True, "Own_House": True, "Credit_Rating": "good", "Class": "Yes"},
    {"ID": 9, "Age": "middle", "Has_Job": False, "Own_House": True, "Credit_Rating": "excellent", "Class": "Yes"},
    {"ID": 10, "Age": "middle", "Has_Job": False, "Own_House": True, "Credit_Rating": "excellent", "Class": "Yes"},
    {"ID": 11, "Age": "old", "Has_Job": False, "Own_House": True, "Credit_Rating": "excellent", "Class": "Yes"},
    {"ID": 12, "Age": "old", "Has_Job": False, "Own_House": True, "Credit_Rating": "good", "Class": "Yes"},
    {"ID": 13, "Age": "old", "Has_Job": True, "Own_House": False, "Credit_Rating": "good", "Class": "Yes"},
    {"ID": 14, "Age": "old", "Has_Job": True, "Own_House": False, "Credit_Rating": "excellent", "Class": "Yes"},
    {"ID": 15, "Age": "old", "Has_Job": False, "Own_House": False, "Credit_Rating": "fair", "Class": "No"},
]


# Step 2: Calculate Entropy
def entropy(rows):
    total = len(rows)
    if total == 0:
        return 0
    count = {"Yes": 0, "No": 0}
    for row in rows:
        count[row["Class"]] += 1
    p_yes = count["Yes"] / total
    p_no = count["No"] / total

    def log2(x):
        return math.log(x, 2) if x > 0 else 0

    return -p_yes * log2(p_yes) - p_no * log2(p_no)


# Step 3: Split data by attribute value
def split_data(rows, attribute):
    result = {}
    for row in rows:
        key = row[attribute]
        if key not in result:
            result[key] = []
        result[key].append(row)
    return result


# Step 4: Calculate information gain
def info_gain(rows, attribute):
    total_entropy = entropy(rows)
    subsets = split_data(rows, attribute)
    weighted_entropy = 0
    print(f"\nEvaluating attribute: {attribute}")
    for val, subset in subsets.items():
        e = entropy(subset)
        weight = len(subset) / len(rows)
        weighted_entropy += weight * e
        print(f" - {attribute} = {val}: {len(subset)} samples, Entropy = {round(e, 4)}")
    gain = total_entropy - weighted_entropy
    print(f" > Weighted Entropy: {round(weighted_entropy, 4)}")
    print(f" > Information Gain: {round(gain, 4)}")
    return gain


# Step 5: Build the tree recursively using ID3
def id3(rows, attributes, depth=0):
    indent = "  " * depth
    classes = [row["Class"] for row in rows]

    if classes.count(classes[0]) == len(classes):
        return classes[0]  # Pure class

    if not attributes:
        return max(set(classes), key=classes.count)  # Majority vote

    print(f"\n{indent}--- Node at Depth {depth} ---")
    print(f"{indent}Entropy of current dataset: {round(entropy(rows), 4)}")

    # Calculate gains
    gains = [(attr, info_gain(rows, attr)) for attr in attributes]
    best_attr = max(gains, key=lambda x: x[1])[0]
    print(f"{indent}=> Best Attribute: {best_attr}")

    tree = {best_attr: {}}
    splits = split_data(rows, best_attr)
    remaining_attrs = [a for a in attributes if a != best_attr]

    for val, subset in splits.items():
        print(f"{indent}Splitting {best_attr} = {val}")
        tree[best_attr][val] = id3(subset, remaining_attrs, depth + 1)

    return tree


# Step 6: Pretty-print the final tree
def print_tree(tree, indent=""):
    if isinstance(tree, str):
        print(indent + "-> " + tree)
    else:
        for attr, branches in tree.items():
            for val, subtree in branches.items():
                print(f"{indent}[{attr} == {val}]")
                print_tree(subtree, indent + "  ")


# Step 7: Run it
attributes = ["Age", "Has_Job", "Own_House", "Credit_Rating"]
print("=== ID3 Decision Tree Construction ===")
tree = id3(dataset, attributes)

print("\n=== Final Decision Tree ===")
print_tree(tree)