import os
from PIL.Image import*
import file_manager
def list_manager():





    datadir_test = "coins_dataset-master/classified/test"
    datadir_train = "coins-dataset-master/classified/train"
    categories = ["1c", "2c", "5c", "10c", "20c", "50c", "1e", "2e"]





    n=0
    for category in categories:
        path = os.path.join(datadir_train, category)
        label = categories.index(category)
        for img in os.listdir(path):
            path = os.path.join(datadir_train, category, img)
            image = open(path, 'r')
            w,h = image.size
            n+=1
            filename = img + '.txt'
            print('creating file', n)
            for x in range (w):
                for y in range (h):
                    color = image.getpixel((x,y))
                    data = str((color, label))
                    file_manager.file(filename,data)


list_manager()
