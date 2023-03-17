import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import statsmodels.stats.proportion as sp

# 1.1
p1 = 1320/3250
p2 = 1250/2870

pc = (1320 + 1250)/ (3250 + 2870)

z = (p1-p2) / np.sqrt(pc * (1 - pc) * (1/3250 + 1/2870))
print(z)

z_alpha = norm.ppf(0.05)
print(z_alpha)

#
#
# # 2.1
# z_scoure, p = sp.proportions_ztest([1320,1250],[3250,2870],alternative='smaller')
# print(z_scoure,p)


#3.1
p_all = 1320/3250 + 1250/2870
choice1 = np.random.choice(2,size=3250,p=[1-p_all,p_all])
choice2 = np.random.choice(2,size=2870,p=[1-p_all,p_all])
diff = choice1.mean() - choice2.mean()
print(diff)

data_diff = 1320/3250-1250/2870
diffs = []
for i in range(10000):
    p2_diff = np.random.choice(2,size=2870,p=[1-p_all,p_all]).mean()
    p1_diff = np.random.choice(2,size=3250,p=[1-p_all,p_all]).mean()
    diffs.append(p1_diff - p2_diff)
diffs = np.array(diffs)
plt.hist(diffs)
plt.axvline(data_diff)
print((diffs<data_diff).mean())


