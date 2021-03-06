import tensorflow as tf
import numpy as np
from scipy import ndimage
import apriori
import cv2
import sys
from misc import find_item, bbox_plot
from model import vgg16


im_dir = sys.argv[1]
features, pred_vec = vgg16(im_dir)
td = {}
d = {}
test = {}
lis = []
j = 0
for feat in features:
	for i in range(512):
		td[j, i], d[j, i] = find_item(feat[:, :, i])
	j += 1

feature_map = tf.concat((features[0, :, :, :], features[1, :, :]), axis=2)

li = [i for i in td.values() if i]
pixel = {}



for i in range(len(li)):
	pixel[i] = li[i]

freq = apriori.run(pixel, 20)
# print (freq)
mk = [eval(i) for i in freq]
support = np.zeros([14, 14])
for i in range(14):
	for j in range(14):
		if [i, j] in mk:
			support[i, j] = np.array(feature_map[i, j, :]).sum()/1024





img = np.zeros([14, 14])
for i in range(14):
	for j in range(14):
		if [i, j] in mk:
			img[i, j] = 1

new_img = np.expand_dims(img, axis=2)
new_img = tf.image.resize(new_img, (224, 224))

new = np.array(new_img[:, :, 0]).astype(int)


labeled_image, num_features = ndimage.label(new)
objs = ndimage.find_objects(labeled_image)
box = np.zeros([len(objs), 4])
# print (objs)
for i in range(len(objs)):
	x = objs[i][1].start
	y = objs[i][0].stop
	w = objs[i][1].stop - objs[i][1].start
	h = objs[i][0].start - objs[i][0].stop
	box[i][:] = x, y, w, h

img = cv2.imread(im_dir, cv2.IMREAD_UNCHANGED)
org_img = cv2.resize(img, (224, 224))
print("marwane wale se just phalae")
print(org_img)

print("box")
print(box)

print()
print("support")
print(support)
bbox_plot(org_img, box, support)