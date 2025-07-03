import os

def get_dirs():

  SOURCE_DIR = os.path.abspath('.')
  dir_dict = {
    'SOURCE_DIR' : os.path.abspath('.'),
    'DATA_DIR' : os.path.join(SOURCE_DIR, 'data'),
    'FIGS_DIR' : os.path.join(SOURCE_DIR, 'figs'),
    'QUERY_DIR' : os.path.join(SOURCE_DIR, 'queries'),
    'PLOT_DIR' : os.path.join(SOURCE_DIR, 'plots')
  }

  return dir_dict