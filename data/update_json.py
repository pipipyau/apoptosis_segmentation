import json
import os
import glob


with open("dataset_0.json", "r") as jsonFile:
    data = json.load(jsonFile)

data['training'] = []
data['validation'] = []
data['test'] = []

new_img_tr_path = '.\\data\\dataset\\imagesTr'
new_label_tr_path = '.\\data\\dataset\\labelsTr'
new_img_ts_path = '.\\data\\data\\imagesTs'

for i, img_tr in enumerate(glob.glob(os.path.join(new_img_tr_path, '*jpg'))):
    new_data_dict = {
            "image": os.path.join('imagesTr', img_tr.split('\\')[-1]),
            "label":os.path.join('labelsTr', img_tr.split('\\')[-1]).replace('.0', '.3')
                }
    if i < 29:
        data['training'].append(new_data_dict)
    else:
        data['validation'].append(new_data_dict)


for i, img_ts in enumerate(glob.glob(os.path.join(new_img_ts_path, '*gz'))):
    new_data = os.path.join('imagesTs', img_ts.split('\\')[-1])
    data['test'].append(new_data)


with open("dataset_0.json", "w") as jsonFile:
    json.dump(data, jsonFile)
