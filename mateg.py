from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("titles.csv")
df = pd.DataFrame(data)
dfh = df.head(10)
dfh.plot(x="title",y="imdb_score",kind="bar",title="Top 10 movies")
plt.show()