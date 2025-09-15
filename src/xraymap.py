import os

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from src.utils import get_dirs # function that reads directories

class XrayMap:
  """
  XrayMap class that read all x-ray maps from a specific dir. 
  It returns a list for numpy arrays, scaled to 255 and ready from diplay with plt.imgshow().

  In this example, X-ray maps are csv files without headers, have intensities as integers 
  and are located on DATA_DIR.
  """

  # constructor
  def __init__(self, element):
    self.element = element
    self.load_data(element)
    self.xray_data_scaled = self.data.to_numpy().astype(np.float32) / 255.0
    self.dimensions = self.data.shape

  
  def load_data(self, element):
    try:
      # print('{a}.csv'.format(a=el))
      self.data = pd.read_csv(os.path.join(get_dirs()["DATA_DIR"],
                                           '{element}.csv'.format(element=element)),
                                           dtype="Int64",
                                           header=None)
      print('{a}.csv found!'.format(a=element))

    except:
      print("error loading map")

  def show_map(self):
    """
    function that plots the map
    """
    plt.title("X-ray map: " + self.element)
    plt.imshow(self.xray_data_scaled)
    plt.show()

  pass