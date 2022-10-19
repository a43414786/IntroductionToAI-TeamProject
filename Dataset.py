import pickle as pkl
import os
import csv
from random import shuffle
import numpy as np

class Dataset:
    
    dataset_path = 'dataset'
    
    def __init__(self):
        self.data = []
        self.label = []
        self.dataset = []

    def get_data(self,motion):
        path = os.path.join(self.dataset_path,motion)
        for i in range(1,4):
            for j in range(1,21):
                data_path = os.path.join(path,f'user_{i}_sample_{j}_{motion}_A.csv')
                label_path = os.path.join(path,f'Annotation_user_{i}_sample_{j}_{motion}.csv')
                with open(data_path,'r') as f:
                    data = csv.reader(f)
                    for d in data:
                        self.data.append(d)
                with open(label_path,'r') as f:
                    label = csv.reader(f)
                    for d in label:
                        self.label.append(d)

    def get_all_motion_data(self):
        self.get_data('bend')
        self.get_data('fall')
        self.get_data('lie down')
        self.get_data('run')
        self.get_data('sitdown')
        self.get_data('standup')
        self.get_data('walk')

    def storeData(self):
        for i in range(len(self.label)):
            self.dataset.append({'label':self.label[i],'data':self.data[i]})
        with open("dataset.pkl",'wb') as f:
            pkl.dump(self.dataset,f)

    def loadData(self):
        if(os.path.exists('dataset.pkl')):
            with open("dataset.pkl",'rb') as f:
                self.dataset = pkl.load(f)
        else:
            self.get_all_motion_data()
            self.storeData()

def train_valid_split():
    train_data = []
    train_label = []
    valid_data = []
    valid_label = []
a = Dataset()
a.loadData()
a.dataset = np.array(a.dataset)

shuffle(a.dataset)

data = []
label = []

for i in a.dataset:
    data.append(i['data'])
    label.append(i['label'])

for i in range(10):
    print(label[i])