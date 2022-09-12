from PIL import Image
import numpy as np

def mirror(seq):
    output = list(seq[::-1])
    output.extend(seq[1:])
    output.reverse()
    output.split
    return output

inputs = [
   ['a', 'b', 'c'],
   ['d', 'e', 'f'],
   ['g', 'h', 'i'],
]
print(mirror([mirror(sublist) for sublist in inputs]))

def random_img(data):
    data.sort()
    highestnum = int(data[len(data) - 1])
    lowestnum = int(data[0])
    Unterschied = 255 / (highestnum - lowestnum)
    #for p in data:
    return Unterschied

    #array = np.random.random_integers(0,255, (height,width,3))

    #array = np.array(array, dtype=np.uint8)
    #img = Image.fromarray(array)
    #img.save(output)


#random_img('random.png', 100, 50)