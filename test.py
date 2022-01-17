import scipy.io as scio
import scipy.misc as misc
import pandas as pd
from matplotlib import pyplot as plt

data_path = "testsets/wu.mat"

data = scio.loadmat(data_path)

derain_data = data.get('derain_data')
rain_data = data.get('rain_data')

for i in range(derain_data.shape[3]):
    plt.imsave("derain/" + str(i) + ".png", derain_data[:, :, :, i])
    plt.imshow(derain_data[:, :, :, i], interpolation='nearest')
    plt.show()
# a = derain_data[:, :, :, 0]
#
# plt.imshow(a, interpolation='nearest')
#
# plt.imsave("1.png", a)
# plt.show()

