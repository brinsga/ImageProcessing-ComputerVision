# Applies a moving average mean filter to an image
# This mean filter leaves the edges untreated
# Mean filters help in removing Gaussian noise and also help with image smoothing



def mean_filter(image, num):
	"""
	image - input noisy image
	num - the shape of num*num square kernel
	"""
    
    boundary = num//2

    w = image.shape[0]
    h = image.shape[1]   
     
    result = np.zeros((w,h))
    for i in range(0, w):
        for j in range(0,h):
            if i-boundary < 0 or i + boundary >= w or j-boundary < 0 or j + boundary >= h:
                result[i][j] = image[i][j]
            else:
                neighbours = []
                for z in range(-boundary,boundary+1):
                    neighbours.append(image[i+z][j])
                    neighbours.append(image[i][j+z])
                    neighbours.append(image[i+z][j+z])
                result[i][j] = sum(neighbours)//9
                
    return result