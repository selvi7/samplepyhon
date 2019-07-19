def volumeCubo( l , h , w ): 
    return (l * h * w) 
      
def surfaceAreaCubo( l , h , w ): 
    return (2 * l * w + 2 * w * h + 2 * l * h) 
  
l = 1
h =2
w = 3
print("Volume =" , volumeCubo(l, h, w)) 
print("Total Surface of the Area =", surfaceAreaCubo(l, h, w))