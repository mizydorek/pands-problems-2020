# plots

import matplotlib.pyplot as plt
import pandas
df = pandas.read_csv("http://www.biostat.jhsph.edu/~rpeng/useRbook/faithful.csv")

plt.plot(df["eruptions"], df["waiting"], 'b.')
plt.title('eruptions vs waiting')
plt.savefig("scatter.png")
plt.clf()

plt.hist(df['eruptions'])
plt.savefig("eruptions.png")
plt.clf()

plt.hist(df['waiting'])
plt.savefig("waiting.png")
plt.clf()