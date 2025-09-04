import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


from src.utils import get_dirs # function that reads directories

class XrayMap: 

  # constructor
  def __init__(self, element):
    self.element = element
    self.xray_data = self.load_data(element)
    self.xray_data_scaled = self.data.to_numpy().astype(np.float32) / 255.0
    # self.dimensions = self.xray_data.shape


  def load_data(self, element):
    try:
      # print('{a}.csv'.format(a=el))
      self.data = pd.read_csv(os.path.join(get_dirs()["DATA_DIR"],'{element}.csv'.format(element=element)),dtype="Int64", header=None)
      print('{a}.csv found!'.format(a=element))

    except:
      print("error loading map")

  def show_map(self):
    plt.imshow(self.xray_data_scaled)
    plt.show()