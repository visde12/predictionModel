import scipy as sp
data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")
#print(data[:10])
#print(data.shape)
x= data[:,0]
y= data[:,1]
sp.sum(sp.isnan(y))
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]
import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],
['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()

def error(f, x, y):
    return sp.sum((f(x)-y)**2)
fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
f1 = sp.poly1d(fp1)


fx = sp.linspace(0,x[-1], 1000) # generate X-values for plotting
plt.plot(fx, f1(fx), linewidth=4)
plt.legend(["d=%i" % f1.order], loc="upper left")


f2p = sp.polyfit(x,y,2)
f2 = sp.poly1d(f2p)
fx = sp.linspace(0,x[-1], 1000) # generate X-values for plotting
plt.plot(fx, f2(fx), linewidth=4)
plt.legend(["d=%i" % f2.order], loc="upper left")


f3p = sp.polyfit(x,y,3)
f3 = sp.poly1d(f3p)
fx = sp.linspace(0,x[-1], 1000) # generate X-values for plotting
plt.plot(fx, f3(fx), linewidth=4)
plt.legend(["d=%i" % f3.order], loc="upper left")


f100p = sp.polyfit(x,y,100)
f100 = sp.poly1d(f100p)
fx = sp.linspace(0,x[-1], 1000) # generate X-values for plotting
plt.plot(fx, f100(fx), linewidth=4)
plt.legend(["d=%i" % f100.order], loc="upper left")

plt.show()

