from math import log
from anytree import Node, RenderTree

# Dataset and Attribute Names
data = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
]

attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind']


# ---------- Helper Functions ----------
def log2(x):
    return log(x) / log(2)


def entropy(dataset):
    total = len(dataset)
    counts = {'Yes': 0, 'No': 0}
    for row in dataset:
        counts[row[-1]] += 1
    ent = 0
    for k in counts:
        if counts[k] == 0:
            continue
        p = counts[k] / total
        ent -= p * log2(p)
    return ent


def info_gain(dataset, attr_index, attr_name):
    total_entropy = entropy(dataset)
    subsets = {}
    for row in dataset:
        key = row[attr_index]
        subsets.setdefault(key, []).append(row)

    weighted_entropy = sum((len(subset) / len(dataset)) * entropy(subset) for subset in subsets.values())
    gain = total_entropy - weighted_entropy

    print(f"\nInformation Gain for {attr_name}:")
    print(f"  Total Entropy: {round(total_entropy, 4)}")
    for val, subset in subsets.items():
        print(f"  {attr_name} = {val}, Subset entropy: {round(entropy(subset), 4)}")
    print(f"  → Information Gain: {round(gain, 4)}")

    return gain


def best_attribute(dataset, attributes):
    best_gain = -1
    best_index = -1
    for i, attr in enumerate(attributes):
        gain = info_gain(dataset, i, attr)
        if gain > best_gain:
            best_gain = gain
            best_index = i
    return best_index


def majority_class(dataset):
    yes = sum(1 for row in dataset if row[-1] == 'Yes')
    no = len(dataset) - yes
    return 'Yes' if yes >= no else 'No'


# ---------- ID3 Recursive Tree Builder ----------
def id3(dataset, attributes, parent_node=None):
    labels = [row[-1] for row in dataset]

    # All same class
    if labels.count(labels[0]) == len(labels):
        return Node(f"[Leaf: {labels[0]}]", parent=parent_node)

    # No more attributes
    if len(attributes) == 0:
        majority = majority_class(dataset)
        return Node(f"[Leaf: {majority}]", parent=parent_node)

    # Select best attribute
    best_idx = best_attribute(dataset, attributes)
    best_attr = attributes[best_idx]
    root = Node(f"{best_attr}", parent=parent_node)

    # Split data and recurse
    attr_values = {}
    for row in dataset:
        val = row[best_idx]
        attr_values.setdefault(val, []).append(row)

    for val, subset in attr_values.items():
        print(f"\nSplitting on {best_attr} = {val}")
        reduced_subset = [row[:best_idx] + row[best_idx + 1:] for row in subset]
        new_attrs = attributes[:best_idx] + attributes[best_idx + 1:]
        branch = Node(f"{best_attr} = {val}", parent=root)
        id3(reduced_subset, new_attrs, parent_node=branch)

    return root


# ---------- Run and Render ----------
print("=== Building ID3 Tree ===")
tree = id3(data, attributes)

print("\n=== Final Decision Tree ===")
for pre, fill, node in RenderTree(tree):
    print(f"{pre}{node.name}")