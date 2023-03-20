from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.preprocessing as pre
from sklearn import decomposition

# a
df= pd.read_csv('movies.csv')
# find best K value

#['votes','gross']
#['budget','gross']
#['runtime','gross']
#['score','gross']
#['budget','runtime']
#['score','runtime']
#['votes','runtime']
#['budget','score']
#['votes','score']


# x1 = df[['votes','gross','budget','runtime','score']].values
# x1 = pre.normalize(x1)
# # inertia = []
# # for i in range(1, 20):
# #     km = KMeans(n_clusters=i)
# #     km.fit(x1)
# #     inertia.append(km.inertia_)
# # # plt.figure(figsize=(12, 6))
# # plt.plot(range(1, 20), inertia)
#
# # plt.title("Find the best K Value")
# # plt.xlabel('K')
# # plt.ylabel('inertia')
# # plt.show()
#
# # K = 4
# km = KMeans(n_clusters=4)
# y_means = km.fit_predict(x1)
# plt.figure(figsize=(12, 6))
# plt.scatter(x1[y_means == 0, 0], x1[y_means == 0, 1], s=200)
# plt.scatter(x1[y_means == 1, 0], x1[y_means == 1, 1], s=200)
# plt.scatter(x1[y_means == 2, 0], x1[y_means == 2, 1], s=200)
# plt.scatter(x1[y_means == 3, 0], x1[y_means == 3, 1], s=200)
# plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s=100, c='black', label='central point')
# plt.title('votes-gross')
# plt.xlabel('votes')
# plt.ylabel('gross')
# plt.legend()
# plt.show()





# b
x2 = pre.normalize([df["budget"].values,df["gross"].values,df["runtime"].values,df["score"].values,df["votes"].values])

df=pd.DataFrame()
df["budget"]=x2[0]
df["gross"]=x2[1]
df["runtime"]=x2[2]
df["score"]=x2[3]
df["votes"]=x2[4]

x3 = df[['votes','gross','budget','runtime','score']].values


km = KMeans(n_clusters=4)
y_means = km.fit_predict(x3)
plt.figure(figsize=(12, 6))
plt.scatter(x3[y_means == 0, 0], x3[y_means == 0, 3], s=200)
plt.scatter(x3[y_means == 1, 0], x3[y_means == 1, 3], s=200)
plt.scatter(x3[y_means == 2, 0], x3[y_means == 2, 3], s=200)
plt.scatter(x3[y_means == 3, 0], x3[y_means == 3, 3], s=200)
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 3], s=100, c='black', label='central point')
plt.title('votes-gross')
plt.xlabel('votes')
plt.ylabel('gross')
plt.legend()
plt.show()

pca = decomposition.PCA(n_components = 2)
pca.fit(df)

df2=pd.DataFrame()
df2["F1"]=pca.transform(df)[:,0]
df2["F2"]=pca.transform(df)[:,1]

x4 = df2[['F1','F2']].values

plt.scatter(x4[y_means == 0, 0], x4[y_means == 0, 1], s=200)
plt.scatter(x4[y_means == 1, 0], x4[y_means == 1, 1], s=200)
plt.scatter(x4[y_means == 2, 0], x4[y_means == 2, 1], s=200)
plt.scatter(x4[y_means == 3, 0], x4[y_means == 3, 1], s=200)
plt.show()