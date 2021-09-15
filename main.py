from PIL import Image, ImageFilter, ImageOps
import math

image = Image.open('bakery.png')

image = image.convert("1");

size = 1000, 500
image = image.resize(size, Image.ANTIALIAS)
image = image.filter(ImageFilter.FIND_EDGES)
image.save('output.png')
image = ImageOps.flip(image)
width, height = image.size

print(height)
height2 = int(height)
print(height2)
width2 = int(width)
pix = image.load()
ind_pixels = []
num_pixels = height2 * width2
for j in range(height2):
  for i in range(width2):
    ind_pixels.append(pix[i,j])
for q in range(num_pixels):
  q_right = q+1
  q_below = q+width2
  column_right = (q_right % width2)
  current_row = math.floor(q/width2)
  if (current_row != height2):
    below_row = current_row+1
    below_valid = 1
  else:
    below_valid = 0
  current_col = (q % width2)
  current_pixel_value = ind_pixels[int(q)]
  right_pixel_value = ind_pixels[int(q_right)]
  below_pixel_value = ind_pixels[int(q_below)]
  if (current_pixel_value == 255):
    if (right_pixel_value == 255):
      print("y=",current_row, r"\{" , current_col, "<= x <=", column_right, r"\}")
    if (below_valid == 1):
      if (below_pixel_value == 255):
        print("x=",current_col, r"\{" , current_row, "<= y <=", below_row, r"\}")
      
 
    
