import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('train_LZdllcl.csv')
print(df.head())
#plotting relationship b/w gender and recruitment_channel
plt.hist(list(df.gender))
plt.xlabel('gender')
plt.ylabel('age')
plt.title('gender age representation')
plt.show()
