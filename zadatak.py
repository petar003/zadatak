import pandas as pd
import matplotlib.pyplot as plt

ucenici = pd.read_excel('doc.xlsx', index_col=None, header=None)
ucenici = ucenici.sort_values(by=1)
plt.figure(figsize=(10,5))
plt.bar(ucenici[0], ucenici[1])
plt.ylim()
plt.show()
plt.close()