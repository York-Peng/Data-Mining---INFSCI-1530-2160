import csv
import matplotlib.pyplot as plt

# Question 1
import math

from sklearn.metrics import brier_score_loss
# Read csv data
file = open('./nfl_elo.csv')
reader = csv.reader(file)
header_row = next(reader)
session = []
elo_prob1 = []
score_1 = []
score_2 = []
data_resource = []
data = []
for row in reader:
    session.append(row[1])
    elo_prob1.append(row[8])
    score_1.append(row[28])
    score_2.append(row[29])
    data_resource.append([row[1],row[8],[row[28],row[29]]])

# Intercepted data from 2010 to 2018
for n in data_resource:
    if '2010' <= n[0] <= '2018':
        data.append(n)

# Remove the tie-breaker situation
for n in data:
    if n[2][0] == n[2][1]:
        data.remove(n)

# Mark the data of A victory as A, and the data of B victory as B
for n in data:
    if float(n[2][0]) > float(n[2][1]):
        n[2] = 'A'
    elif float(n[2][0]) < float(n[2][1]):
        n[2] = "B"

# Splitting the data into boxes
data_04 = []
data_45 = []
data_57 = []
data_70 = []

# Convert predicted values to float type when splitting boxes
for n in data:
    if '0' <= n[1] < '0.4':
        n[1] = float(n[1])
        data_04.append(n)
    elif '0.4' <= n[1] < '0.5':
        n[1] = float(n[1])
        data_45.append(n)
    elif '0.5' <= n[1] < '0.7':
        n[1] = float(n[1])
        data_57.append(n)
    elif '0.7' <= n[1] < '1.0':
        n[1] = float(n[1])
        data_70.append(n)

# Calculate the p-value and o-value under each class
list_04 = []
count_04 = 0
for n in data_04:
    list_04.append(n[1])
    if n[2] == 'A':
        count_04 += 1
p_04 = sum(list_04)/len(data_04)
o_04 = count_04/len(data_04)
print([p_04,o_04])

list_45 = []
count_45 = 0
for n in data_45:
    list_45.append(n[1])
    if n[2] == 'A':
        count_45 += 1
p_45 = sum(list_45)/len(data_45)
o_45 = count_45/len(data_45)
print([p_45,o_45])

list_57 = []
count_57 = 0
for n in data_57:
    list_57.append(n[1])
    if n[2] == 'A':
        count_57 += 1
p_57 = sum(list_57)/len(data_57)
o_57 = count_57/len(data_57)
print([p_57,o_57])

list_70 = []
count_70 = 0
for n in data_70:
    list_70.append(n[1])
    if n[2] == 'A':
        count_70 += 1
p_70 = sum(list_70)/len(data_70)
o_70 = count_70/len(data_70)
print([p_70,o_70])

count_A = 0
for n in data:
    if n[2] == 'A':
        count_A += 1
sum_o = count_A/len(data)

# Final Calculate
Average_bin = 4 * ((p_04-o_04)**2 + (p_45 - o_45)**2 + (p_57 - o_57)**2 + (p_70 - o_70)**2) / len(data)

Bin_base_rate = 4 * ((o_04 - sum_o)**2 + (o_45 - sum_o)**2 + (o_57 - sum_o)**2 + (o_70 - sum_o)**2) / len(data)

Base_rate = sum_o * (1- sum_o)

BS = Average_bin - Bin_base_rate + Base_rate
print(BS)
print(Average_bin)
print(Bin_base_rate)
print(Base_rate)

# Calculate Accuracy
pre_win = []
pre_loss = []
for n in data:
    if n[1] > 0.5:
        pre_win.append(n)
    elif n[1]< 0.5:
        pre_loss.append(n)

count_accuracy = 0
for n in pre_win:
    if n[2] == 'A':
        count_accuracy += 1

for n in pre_loss:
    if n[2] == 'B':
        count_accuracy += 1

Accuracy = count_accuracy/len(data)
print(Accuracy)


# Reliability curve
x = [p_04,p_45,p_57,p_70]
y = [o_04,o_45,o_57,o_70]
# Drawing line graphs
plt.plot(x,y,ls='-',c='r')
plt.show()





























