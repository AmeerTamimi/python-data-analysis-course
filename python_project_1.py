import math
import json

# Read student data from file
file_path = "D:\\Free\\student_data.txt"
students = {}

with open(file_path , "r") as file:
    data = file.read().split("\n")
    for student in data:
        parts = student.split(",")
        name = parts[0].strip().replace('ï»¿', '')
        marks = [int(mark) for mark in  parts[1:]] # Convert to int
        students[name] = marks    


# Calculate sum of marks
def calculate_sum(marks_list):
    try:
        if not marks_list:
            raise ValueError("List is empty")
        total = 0
        for mark in marks_list:
            total += mark
        return total
    except TypeError:
        print("Error: Invalid data type")
        return None

# Find maximum mark
def find_max(marks_list):
    try:
        if not marks_list:
            raise ValueError("List is empty")
        max = marks_list[0]
        for mark in marks_list:
            if mark > max:
                max = mark
        return max
    except TypeError:
        print("Error: Invalid data")
        return None

# Find minimum mark
def find_min(marks_list):
    try:
        if not marks_list:
            raise ValueError("List is empty")
        min= marks_list[0]
        for mark in marks_list:
            if mark < min:
                min = mark
        return min
    except TypeError:
        print("Error: Invalid data")
        return None

# Calculate average
def calculate_avg(marks_list):
    try:
        if not marks_list:
            raise ValueError("List is empty")
        return round(calculate_sum(marks_list) / len(marks_list))
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None

# Sort marks using bubble sort
def custom_sort(marks_list):
    try:
        if not marks_list:
            raise ValueError("List is empty")
        for i in range(len(marks_list)):
            for j in range(len(marks_list) - 1):
                if marks_list[j] > marks_list[j + 1]:
                    marks_list[j], marks_list[j + 1] = marks_list[j + 1], marks_list[j]
        return marks_list
    except TypeError:
        print("Error: Cannot sort invalid data")
        return None
    
# Calculate standard deviation
def calculate_std_dev(marks_list):
    try:
        if not marks_list:
            raise ValueError("List is empty")
        
        # Calculate average
        avg = calculate_avg(marks_list)
        
        #Find squared differences from average
        squared_diffs = []
        for mark in marks_list:
            diff = mark - avg
            squared_diff = diff ** 2
            squared_diffs.append(squared_diff)
        
       # Calculate variance average of squared differences
        variance = calculate_avg(squared_diffs)  # or sum(squared_diffs)/len(squared_diffs)
        
        #Take square root of variance
        std_dev = math.sqrt(variance)
        
        return round(std_dev, 2)
    
    except (TypeError, ValueError):
        print("Error: Invalid data for standard deviation")
        return None

# Find first quartile (25th percentile)
def find_q1(marks_list):
    try:
        if not marks_list:
            raise ValueError("List is Empty !")
        sorted_list = custom_sort(marks_list)
        index = (0.25) * (len(sorted_list))
        ceiled_index = math.ceil(index)
        if(ceiled_index != index):
            return sorted_list[ceiled_index-1]
        else:
            median = (sorted_list[ceiled_index-1] + sorted_list[ceiled_index]) / 2
            return median
    except (TypeError, ValueError):
        print("Error: Invalid data for standard deviation")
        return None
    
# Find second quartile (median)
def find_q2(marks_list):
    try:
        if not marks_list:
            raise ValueError("List is Empty !")
        sorted_list = custom_sort(marks_list)
        index = (0.5) * (len(sorted_list))
        ceiled_index = math.ceil(index)
        if(ceiled_index != index):
            return sorted_list[ceiled_index-1]
        else:
            median = (sorted_list[ceiled_index-1] + sorted_list[ceiled_index]) / 2
            return median
    except (TypeError, ValueError):
        print("Error: Invalid data for standard deviation")
        return None
    
# Find third quartile (75th percentile)
def find_q3(marks_list):
    try:
        if not marks_list:
            raise ValueError("List is Empty !")
        sorted_list = custom_sort(marks_list)
        index = (0.75) * (len(sorted_list))
        ceiled_index = math.ceil(index)
        if(ceiled_index != index):
            return sorted_list[ceiled_index-1]
        else:
            median = (sorted_list[ceiled_index-1] + sorted_list[ceiled_index]) / 2
            return median
    except (TypeError, ValueError):
        print("Error: Invalid data for standard deviation")
        return None

# Calculate interquartile range (Q3 - Q1)
def find_interquartile_range(marks_list):
    try:
        if not marks_list:
            raise ValueError("List is Empty !")
        return find_q3(marks_list) - find_q1(marks_list)
    except (TypeError, ValueError):
        print("Error: Invalid data for standard deviation")
        return None

# Main analysis
output = {}    
average_list = []
max_mark = 0
min_mark = 100
max_mark_student = ""
min_mark_student = ""

# Find max and min marks across all students
for name,marks in students.items():
    average_list.append(calculate_avg(marks))
    current_max = find_max(marks)
    current_min = find_min(marks)
    if current_max > max_mark:
        max_mark = current_max
        max_mark_student = name
    if current_min < min_mark:
        min_mark = current_min
        min_mark_student = name

# Find students with max and min averages
max_avg = find_max(average_list)
min_avg = find_min(average_list)
max_avg_student = ""
min_avg_student = ""

for name,marks in students.items():
    avg_marks = calculate_avg(marks)
    if avg_marks == max_avg:
        max_avg_student = name
    if avg_marks == min_avg:
        min_avg_student = name

# Find most frequent mark
marks_frequency = {}
most_frequent_mark = 0
max_frequency = 0
for marks in students.values():
    for mark in marks:
        if mark not in marks_frequency:
            marks_frequency[mark] = 1
        else:
            marks_frequency[mark] += 1
            if(marks_frequency[mark] > max_frequency):
                max_frequency = marks_frequency[mark]
                most_frequent_mark = mark

# Collect all marks for quartile calculations
all_marks = []
for marks in students.values():
    all_marks.extend(marks)

# Calculate standard deviation for all marks
std_dev = calculate_std_dev(all_marks)

# Store all required information in output dictionary
# Store all required information in output dictionary
output = {
    "Maximum Average": {
        "student_name": max_avg_student,
        "value": max_avg
    },
    "Maximum Mark": {
        "student_name": max_mark_student,
        "value": max_mark
    },
    "Minimum Average": {
        "student_name": min_avg_student,
        "value": min_avg
    },
    "Minimum Mark": {
        "student_name": min_mark_student,
        "value": min_mark
    },
    "Standard Deviation": {
        "value": std_dev
    },
    "Q1": {
        "value": find_q1(all_marks)
    },
    "Q2 (Median)": {
        "value": find_q2(all_marks)
    },
    "Q3": {
        "value": find_q3(all_marks)
    },
    "IQR": {
        "value": find_interquartile_range(all_marks)
    },
    "Most Frequent Mark": {
        "value": most_frequent_mark
    }
}

# Export the output dic as a json file
with open("C:\\Users\\USER-Q\\Desktop\\student_analysis_project.json" , "w") as file:
    json.dump(output , file , indent=4)
print(output)