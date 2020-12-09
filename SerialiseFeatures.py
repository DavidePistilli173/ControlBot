import cv2
import numpy as np
import sys

IMAGE_FOLDER = "./images/"
IMAGE_EXTENSION = ".png"

DESCRIPTOR_FOLDER = "./descriptors/"
DESCRIPTOR_EXTENSION = ".dtr"

# Create a feature detector with suitable parameters.
def createFeaturesDetector():
    return cv2.ORB_create(nfeatures = 100, edgeThreshold=2)

# Return keypoints and descriptors from an image.
def computeKeypointsAndDescriptors(orb, img):
    keypoints, descriptors = orb.detectAndCompute(img, None)
    return keypoints, descriptors

# Return descriptors from an image.
def computeDescriptors(orb, img):
    keypoints, descriptors = orb.detectAndCompute(img, None)
    return descriptors

# Load descriptor from file.
def loadDescriptor(fileName):
    file = open(DESCRIPTOR_FOLDER + fileName + DESCRIPTOR_EXTENSION, 'rb')
    if not file.mode == 'rb':
        print("Failed to load image descriptors.")
        exit(0)

    data = np.load(file)
    file.close()
    return data

def main():

    imageName = "firefox_newTab"

    print("Loading image.")
    img = cv2.imread(IMAGE_FOLDER + imageName + IMAGE_EXTENSION, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Failed to load image.")
        exit(0)

    print("Computing features.")
    orb = createFeaturesDetector()
    keypoints, descriptors = computeKeypointsAndDescriptors(orb, img)

    print("Drawing results.")
    img_keypoints = np.empty((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    cv2.drawKeypoints(img, keypoints, img_keypoints, color=(0,255,0), flags=0)
    cv2.imshow("Test", img_keypoints)
    cv2.waitKey(0)

    print("Saving descriptors.")
    file = open(DESCRIPTOR_FOLDER + imageName + DESCRIPTOR_EXTENSION, 'wb')
    np.save(file, descriptors)
    file.close()

    print("Serialisation complete.")

if __name__ == '__main__':
    main()