from AudiPy.Input import read_dataset_img

#defines input
image_path = "examples/Tyler_the_creator_ac.webp"
#converts image to numarray
img_array = read_dataset_img(image_path)
print(img_array)
#this line needs to process the numarray to sound
#output_sound_path = "output.wav"
#print(f'Processing Complete. Sound saved to{output_sound_path}.')
