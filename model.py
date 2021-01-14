from keras.preprocessing.image import ImageDataGenerator,array_to_img,img_to_array,load_img

datagen = ImageDataGenerator(
    width_shift_range=0.25,
    height_shift_range=0.25,
    rotation_range=40,
    horizontal_flip=True,
    vertical_flip=True
)

img = load_img(r"C:\Users\chand\Desktop\Anaconda\New folder\download.jpg")
x=img_to_array(img)
x = x.reshape((1,)+ x.shape)

i=0
for data in datagen.flow(x,batch_size=1,save_to_dir=r'C:\Users\chand\Desktop\Anaconda\New folder',save_prefix='flower',save_format='jpg'):
  i=i+1
  if i>5:
    break
