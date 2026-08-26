#I turned a garde-2 bar chart from Khan acedamy into a system that can also run other similar types of bar charts.
#I foused on the following five questions.


data = {"Ishann": {"midterm": 90, "finale": 100}, 
        "Emily": {"midterm": 90, "finale": 100},
        "Daniel": {"midterm": 60, "finale": 100},
        "Jessica": {"midterm": 100, "finale": 75},
        "William": {"midterm": 80, "finale": 80}}

#What was the median score for the finale exam?

median = []

for key, value in data.items():
    median.append(value["finale"])

n = sorted(median)
m = len(median)

if m % 2 == 1:
    median = n[m // 2]
else:
    median = (n[(m // 2) - 1] + n[m // 2]) / 2

print(f"Median: {median}")

#What is the midrange of the midterm scores?

medium = []
for names, scores in data.items():
    medium.append(scores["midterm"])

mid = (max(medium) + min(medium)) / 2

print(mid)

#What was the average student score for the finale exam?

finale_average = []
for students, scores in data.items():
    finale_average.append(scores["finale"])
average = sum(finale_average) / len(finale_average)
print(average)

#What was the mode for the finale exam scores?


mode = []
for students, marks in data.items():
    mode.append(marks["finale"])

max_count = 0
mode_set = set()

for i in range(len(mode)):
    rn = mode[i]
    count = 0 
    for j in range(len(mode)):
        if mode[j] == rn:
            count += 1
    if count > max_count:
        max_count = count
        mode_set = {rn}
    elif count == max_count:
        mode_set.add(rn)

print(*mode_set)

#What is the range of the midterm scores?

range = []
for humans, integers in data.items():
    range.append(integers["midterm"])

rng = max(range) - min(range)
print(rng)