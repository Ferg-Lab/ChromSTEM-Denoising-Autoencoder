import numpy as np

class utily:

    # --------------------------------------------------------------------

    def __init__(self, *list):
        self.snaps = []

        
    def normalize(self):
        xmax, xmin = self.max(), self.min()
        norm_image = np.float32((self - xmin)/(xmax - xmin))
        return(norm_image)