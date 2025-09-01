class XrayMap: 

  def __init__(self, element, xray_data):
    self.element = element
    self.xray_data = xray_data
    # self.xray_data_scaled = xray_data.to_numpy().astype(np.float32) / 255.0
    self.dimensions = xray_data.shape

  
  def display_map(self):
    