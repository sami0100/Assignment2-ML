def calculate_iqr_and_median(data):
    data.sort()
    n = len(data)

    def get_median(lst):
        l = len(lst)
        if l % 2 == 0:
            return (lst[l//2 - 1] + lst[l//2]) / 2
        else:
            return lst[l//2]

    # Median of full data
    median = get_median(data)

    # Q1 and Q3
    if n % 2 == 0:
        lower_half = data[:n//2]
        upper_half = data[n//2:]
    else:
        lower_half = data[:n//2]
        upper_half = data[n//2+1:]

    Q1 = get_median(lower_half)
    Q3 = get_median(upper_half)
    IQR = Q3 - Q1

    # Outlier bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filtered data (no outliers)
    clean_data = [x for x in data if lower_bound <= x <= upper_bound]

    # Return results
    return {
        "Sorted Data": data,
        "Median": median,
        "Q1": Q1,
        "Q3": Q3,
        "IQR": IQR,
        "Lower Bound": lower_bound,
        "Upper Bound": upper_bound,
        "Filtered (No Outliers)": clean_data
    }

# === Dataset ===
presentation = [78, 35, 80, 75, 79, 92, 76, 77, 81, 84, 83, 79, 30, 100, 80]
development  = [82, 40, 78, 84, 77, 95, 80, 83, 79, 88, 81, 82, 40, 99, 83]
topic_strength = [88, 31, 86, 85, 87, 89, 90, 92, 86, 90, 88, 87, 40, 99, 85]

# === Apply and Print Results ===
def print_results(title, result):
    print(f"\n----- {title} -----")
    for k, v in result.items():
        print(f"{k}: {v}")

print_results("Presentation Scores", calculate_iqr_and_median(presentation))
print_results("Development Scores", calculate_iqr_and_median(development))
print_results("Topic Strength Scores", calculate_iqr_and_median(topic_strength))