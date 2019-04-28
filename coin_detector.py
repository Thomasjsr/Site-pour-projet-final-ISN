import numpy as np
import os
import cv2


datadir_test = "classified/test"
datadir_train = "classified/train"
categories = ["1c", "2c", "5c", "10c", "20c", "50c", "1e", "2e"]

training_data = []
for category in categories:
    path = os.path.join(datadir_train, category)
    class_num = categories.index(category)
    for img in os.listdir(path):
        try:
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            training_data.append([img_array, class_num])
        except Exception as e:
            pass

x_train = []
y_train = []

for features, label in training_data:
    x_train.append(features)
    y_train.append(label)

x_train = np.array(x_train).reshape(-1, training_data[0][0].shape[0], training_data[0][0].shape[0], 1)

testing_data = []
for category in categories:
    path = os.path.join(datadir_test, category)
    class_num = categories.index(category)
    for img in os.listdir(path):
        try:
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            testing_data.append([img_array, class_num])
        except Exception as e:
            pass

x_test = []
y_test = []

for features, label in training_data:
    x_test.append(features)
    y_test.append(label)

x_test = np.array(x_test).reshape(-1, training_data[0][0].shape[0], training_data[0][0].shape[0], 1)

def euc(a, b):
    return np.linalg.norm(np.array(a)-np.array(b))


class KNN():
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        predictions = []
        for row in x_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self, row):
        best_dist = euc(row, self.x_train[0])
        best_index = 0
        for i in range(1, len(self.x_train)):
            dist = euc(row, self.x_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]

from sklearn.metrics import accuracy_score

clf = KNN()
clf.fit(x_train, y_train)
predictions = clf.predict(x_test)
print(accuracy_score(y_test, predictions))
