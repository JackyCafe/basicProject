import matplotlib.pyplot as plt


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
width = 0.35

fig, ax = plt.subplots()
ax.bar(labels,men_means,width,label='Men')
ax.bar(labels,women_means,width,bottom=men_means,label='Woman')
plt.legend()
plt.show()
