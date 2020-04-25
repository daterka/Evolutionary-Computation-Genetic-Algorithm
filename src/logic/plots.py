import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from src.logic.configuration._Configuration import Config as cnf

def marekBest(self, best):
    self.ax.scatter(best.decode(), best.getTargetValue(), c='y', marker='o')
    plt.clf()
    plt.show()


def updateTargetPlot(self):
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm
    from matplotlib.ticker import LinearLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    x = []
    y = []
    z = []
    for chrom in self.population:
        x_val, y_val = chrom.decode()
        x.append(x_val)
        y.append(y_val)
        z.append(chrom.getTargetValue())

    self.ax.scatter(x, y, z, c='r', marker='o')
    plt.clf()
    plt.show()


def drawTarget(self):
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm
    from matplotlib.ticker import LinearLocator, FormatStrFormatter
    import matplotlib.pyplot as plt

    x = []
    y = []
    z = []
    for chrom in self.population:
        x_val, y_val = chrom.decode()
        x.append(x_val)
        y.append(y_val)
        z.append(chrom.getTargetValue())

    self.fig = plt.figure()
    self.ax = self.fig.add_subplot(111, projection='3d')
    self.ax.view_init(azim=30)
    self.ax.scatter(x, y, z, c='r', marker='o')

    plt.show()

def plotBestPerEpoch(best=[]):
    print('best : ', best)
    plt.margins(0)
    plt.figure(figsize=(6,2.5))
    plt.plot(best)
    plt.title('BEST PER EPOCH')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    # plt.legend(['best per epoch'], loc='best')
    plt.savefig('plots/' + 'best.png')
    plt.show()
    plt.close()

def plotSimple(y_vals=[], label_y='y', label_x='x', title='plot', instance_info='no_info', save_location='./plots/'):
    filename = save_location + title+'_'+ instance_info +'.png'
    plt.plot(y_vals)
    plt.title(title)
    plt.ylabel(label_y)
    plt.xlabel(label_x)
    plt.savefig(filename)
    plt.close()