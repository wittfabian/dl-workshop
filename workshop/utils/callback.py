import numpy as np
from time import time
from keras.callbacks import Callback

class TimingCallback(Callback):
    def __init__(self):
        super(TimingCallback, self).__init__()
        self.epoch_logs=[]
        self.batch_logs=[]
        self.train_logs=[]

    def on_epoch_begin(self, epoch, logs=None):
        self.epoch_starttime = time()

    def on_epoch_end(self, epoch, logs=None):
        self.epoch_logs.append(time() - self.epoch_starttime)

    def on_batch_begin(self, batch, logs=None):
        self.batch_starttime = time()

    def on_batch_end(self, batch, logs=None):
        self.batch_logs.append(time() - self.batch_starttime)

    def on_train_begin(self, logs=None):
        self.train_starttime = time()

    def on_train_end(self, logs=None):
        self.train_logs.append(time() - self.train_starttime)

    @property
    def epoch_mean_time(self):
        return np.array(self.epoch_logs).mean()

    @property
    def batch_mean_time(self):
        return np.array(self.batch_logs).mean()

    @property
    def train_mean_time(self):
        return np.array(self.train_logs).mean()