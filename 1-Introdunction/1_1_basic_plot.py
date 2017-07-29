import matplotlib.pyplot as plt

x1_values = [2012, 2013, 2014, 2015]
y1_values = [4.3, 2.5, 3.5, 4.5]

x2_values = [2012, 2013, 2014, 2015]
y2_values = [2.4, 4.4, 1.8, 2.8]

x3_values = [2012, 2013, 2014, 2015]
y3_values = [2, 2, 3, 5]

plt.figure()
plt.plot(x1_values, y1_values, label='Python')
plt.plot(x2_values, y2_values, label='JavaScript')
plt.plot(x3_values, y3_values, label='R')

plt.xlim(2012, 2015)
plt.ylim(0, 6)
plt.xticks([2012, 2013, 2014, 2015], ['2012', '2013', '2014', '2015'])
plt.yticks([1, 2, 3, 4, 5])

plt.xlabel('')
plt.ylabel('Web Searches')

plt.legend(loc='upper center', ncol=3)
plt.grid(True)

# it can save the figure in any image file format you want
#  png, pdf, ps, eps, ...
plt.savefig('web-searches.png', dpi=150)

plt.show()
