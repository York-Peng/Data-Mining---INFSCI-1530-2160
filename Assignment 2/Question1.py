import csv
import numpy as np
import matplotlib.pyplot as plt
import pylab as plb

# Read csv data
file = open('./daily_citi_bike_trip_counts_and_weather.csv')
reader = csv.reader(file)
header_row = next(reader)
trips = []
high_temp = []
week = []
year = []
month_day = []
for row in reader:
    trips.append(float(row[1]))
    high_temp.append(float(row[5]))
    week.append(int(row[8]))
    year.append(int(row[10]))
    month_day.append([int(row[8]),int(row[10]),int(row[1])])
print(month_day)
# Divide data to the training set, validation set and test set
# training_x = high_temp[0:685]
# training_y = trips[0:685]
# validation_x = high_temp[685:785]
# validation_y = trips[685:785]
# test_x = high_temp[785:885]
# test_y = trips[785:885]

training_x = high_temp[0:350]
training_y = trips[0:350]
validation_x = high_temp[350:600]
validation_y = trips[350:600]
test_x = high_temp[600:885]
test_y = trips[600:885]

# When N = 0
# Training models with training groups
z0 = np.polyfit(training_x,training_y,0)
p0 = np.poly1d(z0)
y_vals_0 = p0(validation_x)

# Calculating MSE
differ0 = []
for i in range(len(validation_y)):
    temp = (validation_y[i] - y_vals_0[i]) ** 2
    differ0.append(temp)
MSE0 = sum(differ0)/len(validation_y)

# Testing with test set data
y_test_0 = p0(test_x)
differ0_t = []
for i in range(len(test_y)):
    temp = (test_y[i] - y_test_0[i]) ** 2
    differ0_t.append(temp)
MSE0_t = sum(differ0_t)/len(test_y)


# N = 1
z1 = np.polyfit(training_x,training_y,1)
p1 = np.poly1d(z1)
y_vals_1 = p1(validation_x)

differ1 = []
for i in range(len(validation_y)):
    temp = (validation_y[i] - y_vals_1[i]) ** 2
    differ1.append(temp)
MSE1 = sum(differ1)/len(validation_y)

y_test_1 = p1(test_x)
differ1_t = []
for i in range(len(test_y)):
    temp = (test_y[i] - y_test_1[i]) ** 2
    differ1_t.append(temp)
MSE1_t = sum(differ1_t)/len(test_y)


# N = 2
z2 = np.polyfit(training_x,training_y,2)
p2 = np.poly1d(z2)
y_vals_2 = p2(validation_x)

differ2 = []
for i in range(len(validation_y)):
    temp = (validation_y[i] - y_vals_2[i]) ** 2
    differ2.append(temp)
MSE2 = sum(differ2)/len(validation_y)

y_test_2 = p2(test_x)
differ2_t = []
for i in range(len(test_y)):
    temp = (test_y[i] - y_test_2[i]) ** 2
    differ2_t.append(temp)
MSE2_t = sum(differ2_t)/len(test_y)


# N = 3
z3 = np.polyfit(training_x,training_y,3)
p3 = np.poly1d(z3)
y_vals_3 = p3(validation_x)

differ3 = []
for i in range(len(validation_y)):
    temp = (validation_y[i] - y_vals_3[i]) ** 2
    differ3.append(temp)
MSE3 = sum(differ3)/len(validation_y)

y_test_3 = p3(test_x)
differ3_t = []
for i in range(len(test_y)):
    temp = (test_y[i] - y_test_3[i]) ** 2
    differ3_t.append(temp)
MSE3_t = sum(differ3_t)/len(test_y)


# N = 4
z4 = np.polyfit(training_x,training_y,4)
p4 = np.poly1d(z4)
y_vals_4 = p4(validation_x)

differ4 = []
for i in range(len(validation_y)):
    temp = (validation_y[i] - y_vals_4[i]) ** 2
    differ4.append(temp)
MSE4 = sum(differ4)/len(validation_y)

y_test_4 = p4(test_x)
differ4_t = []
for i in range(len(test_y)):
    temp = (test_y[i] - y_test_4[i]) ** 2
    differ4_t.append(temp)
MSE4_t = sum(differ4_t)/len(test_y)


# N = 5
z5 = np.polyfit(training_x,training_y,5)
p5 = np.poly1d(z5)
y_vals_5 = p5(validation_x)

differ5 = []
for i in range(len(validation_y)):
    temp = (validation_y[i] - y_vals_5[i]) ** 2
    differ5.append(temp)
MSE5 = sum(differ5)/len(validation_y)

y_test_5 = p5(test_x)
differ5_t = []
for i in range(len(test_y)):
    temp = (test_y[i] - y_test_5[i]) ** 2
    differ5_t.append(temp)
MSE5_t = sum(differ5_t)/len(test_y)
#
# print(MSE0)
# print(MSE1)
# print(MSE2)
# print(MSE3)
# print(MSE4)
# print(MSE5)

# print(MSE0_t)
# print(MSE1_t)
# print(MSE2_t)
# print(MSE3_t)
# print(MSE4_t)
# print(MSE5_t)


# Draw Fitting graph with Model 1 and random arrays
z = np.polyfit(high_temp,trips,1)
p = np.poly1d(z)
x = np.arange(20,100,0.1)
y_vals = p(x)

plot1 = plt.plot(high_temp,trips,'*')
plot2 = plt.plot(x,y_vals)
plt.xlabel('high_temp')
plt.ylabel('trips')
plt.show()


# visualize
# Frequency corresponding to different number of trips
# plt.hist(trips,bins=80)
# plt.show()
#
# Graph of maximum temperature and trips
# plt.scatter(high_temp,trips)
# plt.xlabel('high_temp')
# plt.ylabel('trips')
# plt.show()
#
# Relationship between reaction months and trips
# plt.bar(year,trips)
# plt.xlabel('month')
# plt.ylabel('trips')
# plt.show()
#
# # Relationship between reaction day and trips
# plt.bar(week,trips)
# plt.xlabel('day of week')
# plt.ylabel('trips')
# plt.show()








