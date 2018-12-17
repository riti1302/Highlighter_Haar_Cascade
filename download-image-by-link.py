import urllib.request
import cv2
import numpy as np
import os


def store_raw_images():
	neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n00021265'
	neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()

	if not os.path.exists('negative'):
		os.makedirs('negative')


	pic_num = 392

	for i in neg_image_urls.split('\n'):
		try:
			print(i)
			urllib.request.urlretrieve(i, "negative/"+str(pic_num)+'.jpg')
			img = cv2.imread("negative/"+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
			resized_image = cv2.resize(img,(100,100))
			cv2.imwrite("negative/"+str(pic_num)+'.jpg', resized_image)
			pic_num += 1

		except Exception as e:
			print(str(e))

def find_uglies():
	for file_type in ['negative']:
		for img in os.listdir(file_type):
			for ugly in os.listdir('uglies'):
				try:
					current_image_path = str(file_type)+'/'+str(img)
					ugly = cv2.imread('uglies/'+str(ugly))
					question = cv2.imread(current_image_path)

					if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
						print ("Nigga you're ugly")
						os.remove(current_image_path) 


				except Exception as e:
					print(str(e))

def create_pos_n_neg():
	for file_type in ['negative']:
		for img in os.listdir(file_type):
			if file_type == 'negative':
				line = file_type+'/'+img+'\n'
				with open('bg.txt','a') as f:
					f.write(line)
 

def resize_pos():
	image = cv2.imread('highlighter.jpg')
	resize = cv2.resize(image, (50,50))
	cv2.imwrite('Highlighter.jpg', resize)

store_raw_images()
find_uglies()
create_pos_n_neg()
resize_pos()