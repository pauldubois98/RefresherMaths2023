import cv2
import numpy as np
import matplotlib.pyplot as plt


def cv2_imshow(img):
    plt.figure(figsize=(10,10))
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

def read_file(filename):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2_imshow(img)
    return img


img = read_file("full_class_.jpg")

def edge_mask(img, line_size, blur_value):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, blur_value)
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
    return edges


line_size = 5
blur_value = 7
edges = edge_mask(img, line_size, blur_value)
cv2_imshow(edges)
# save the edges image
# cv2.imwrite("edges.jpg", edges)



def color_quantization(img, k):
    # Transform the image
    data = np.float32(img).reshape((-1, 3))

    # Determine criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

    # Implementing K-Means
    ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result

def color_quantization2(img, k1, k2=None, k3=None):
    if k2 is None:
        k2 = k1
    if k3 is None:
        k3 = k1
    img2 = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    data = np.float32(img2[:,:,0].flatten())
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
    ret, label, center = cv2.kmeans(data, k1, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img2[:,:,0].shape)
    img2[:,:,0] = result

    data = np.float32(img2[:,:,1].flatten())
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
    ret, label, center = cv2.kmeans(data, k2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img2[:,:,1].shape)
    img2[:,:,1] = result

    data = np.float32(img2[:,:,2].flatten())
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
    ret, label, center = cv2.kmeans(data, k3, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img2[:,:,2].shape)
    img2[:,:,2] = result





    img3 = cv2.cvtColor(img2,cv2.COLOR_HSV2RGB)
    return img3



img = color_quantization2(img, 10)
cv2_imshow(img)

blurred = img

cv2.imwrite("full_class_less_colors.jpg", cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# blurred = cv2.bilateralFilter(img, d=7, sigmaColor=200,sigmaSpace=200)
# cv2_imshow(blurred)
cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
cv2_imshow(cartoon)
#bgr to rgb
cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
# save the image
cv2.imwrite("cartoon_class.jpg", cartoon)