import numpy as np
import h5py
    
    
def a():
    train_dataset = h5py.File('datasets/all.h5', "r")
    media= np.array(train_dataset["wk"][:]) # your train set features
    media = media.reshape((1, a.shape[0]))
    
    
    return media
