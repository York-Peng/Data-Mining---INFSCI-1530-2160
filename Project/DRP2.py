import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('drp2-data.csv')
# print([df['Salary'].values,df['SAT'].values])

# plt.scatter(df['Salary'].values,df['SAT'].values)
# plt.xlabel('Salary')
# plt.ylabel('SAT')
# plt.title('Salary & SAT Relevance')
# plt.show()
#
# data = pd.DataFrame({'Salary':df['Salary'].values,'SAT':df['SAT'].values})
# # data.corr(method='spearman',min_periods=1)
#
# print('Salary & SAT Relevance')
# print(data.corr(method='spearman',min_periods=1))
# print('method:spearman')
# print('------------------------------------------------')
# print(data.corr())
# print('method:pearson')


# plt.scatter(df['Rank'].values,df['SAT'].values)
# plt.xlabel('Rank')
# plt.ylabel('SAT')
# plt.title('Rank & SAT Relevance')
# plt.show()
#
# data = pd.DataFrame({'Rank':df['Rank'].values,'SAT':df['SAT'].values})
# # data.corr(method='spearman',min_periods=1)
#
# print('Rank & SAT Relevance')
# print(data.corr(method='spearman',min_periods=1))
# print('method:spearman')
# print('------------------------------------------------')
# print(data.corr())
# print('method:pearson')


plt.scatter(df['Salary'].values,df['Faculty'].values)
plt.xlabel('Salary')
plt.ylabel('Faculty')
plt.title('Salary & Faculty Relevance')
plt.show()

plt.scatter(df['Rank'].values,df['Faculty'].values)
plt.xlabel('Rank')
plt.ylabel('Faculty')
plt.title('Rank & Faculty Relevance')
plt.show()

#
# data = pd.DataFrame({'Rank':df['Salary'].values,'SAT':df['Faculty'].values})
# # data.corr(method='spearman',min_periods=1)
#
# print('Salary & Faculty Relevance')
# print(data.corr(method='spearman',min_periods=1))
# print('method:spearman')
# print('------------------------------------------------')
# print(data.corr())
# print('method:pearson')

# data = pd.DataFrame({'Rank':df['Rank'].values,'Salary':df['Salary'].values,'Instate':df['Instate']})
# data0 = data.loc[data['Instate'] == 0]
# data1 = data.loc[data['Instate'] == 1]
#
# plt.scatter(data0['Salary'].values,data0['Rank'].values)
# plt.xlabel('Salary')
# plt.ylabel('Rank')
# plt.title('Salary & Rank Relevance')
# plt.show()
#
# plt.scatter(data1['Salary'].values,data1['Rank'].values)
# plt.xlabel('Salary')
# plt.ylabel('Rank')
# plt.title('Salary & Rank Relevance')
# plt.show()







