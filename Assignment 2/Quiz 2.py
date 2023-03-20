import pandas as pd
import io
import requests
import csv
import matplotlib.pyplot as plt
import pandas as pd

# # Download csv file content
# url="https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/ratings.csv"
# s=requests.get(url).content
# raw_csv = pd.read_csv(io.StringIO(s.decode('utf-8')))
# # print(raw_csv)
# book_id = []
# rating = []
# for n in raw_csv.loc[:,'book_id']:
#     book_id.append(n)
#
# for n in raw_csv.loc[:,'rating']:
#     rating.append(n)
#
# book_rating = []
# for x in range(len(rating)):
#     book_rating.append([book_id[x],rating[x]])
#
#
# f = open('../good_book.csv', 'w')
# writer = csv.writer(f)
# for x in book_rating:
#      writer.writerow(x)
# f.close()
#

file = open('./good_book.csv')
reader = csv.reader(file)
book_rating_only  = []
book_id = []
book_rating = []
for row in reader:
    book_id.append(row[0])
    book_rating_only.append(int(row[1]))
    book_rating.append([row[0],row[1]])

dict = {}
for i in book_id:
    dict[int(i)] = []

for a in book_rating:
    if int(a[0]) in dict.keys():
        dict[int(a[0])].append(int(a[1]))
# print(dict)

# Calculate the average of all ratings for each book and plot it as a dictionary
book_rating_avg1 = {}
for i in dict:
    book_rating_avg1[i] = sum(dict[i])/len(dict[i])
print(book_rating_avg1)

# Calculate the average score of all books
Avg_all_prodecut = sum(book_rating_only)/len(book_rating_only)
print(Avg_all_prodecut)


# Average number of all book ratings
book_rating_count = []
for i in dict:
    temp = len(dict[i])
    book_rating_count.append(temp)
book_rating_avg = sum(book_rating_count)/len(dict)
# print(book_rating_avg)

print('Bayesian average:')
# Bayesian average
book_bayesian_average = {}
for i in dict:
    bayesian_average = (Avg_all_prodecut * book_rating_avg + sum(dict[i]))/(book_rating_avg + len(dict[i]))
    book_bayesian_average[i] = bayesian_average
print(book_bayesian_average)

# difference
book_avg_difference = {}
x = []
y = []
for i in dict:
    book_avg_difference[i] = []
    count = len(dict[i])
    differ = book_bayesian_average[i] - book_rating_avg1[i]
    if differ < 0 :
        differ = -1 * differ
    book_avg_difference[i].append(count)
    book_avg_difference[i].append(differ)
    x.append(count)
    y.append(differ)
print(book_avg_difference)

plt.scatter(x,y)
plt.xlabel("number of book's rating")
plt.ylabel('difference')
plt.show()




