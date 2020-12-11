import numpy as np
import logging
#
#logging.basicConfig(level=logging.INFO)
FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT,filename='myLog.log', filemode='a')

t = np.arange(0., 5., 0.2)
logging.info(t)
