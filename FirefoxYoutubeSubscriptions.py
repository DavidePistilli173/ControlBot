from ControlBot import *
from SerialiseFeatures import createFeaturesDetector as createORB
from SerialiseFeatures import computeDescriptors
from SerialiseFeatures import loadDescriptor

import cv2
from mss import mss

UI_SCALE = 1
ADDRESS_BAR = np.array([313 * UI_SCALE, 53 * UI_SCALE])
FIRST_TAB_BOX = {'top': 0, 'left': 0, 'width': 224 * UI_SCALE, 'height': 30 * UI_SCALE}

# Start the controller
controller = ControlBot()
sct = mss()

# Load descriptors
newTabDescriptors = loadDescriptor("firefox_newTab")

# Create the feature matcher
orb = createORB()
bf = cv2.BFMatcher_create(cv2.NORM_HAMMING)

# Search for Firefox in the start menu
#controller.k_combination(np.array([Key.cmd, '1']))
controller.k_single_press(Key.cmd)
controller.k_type("Firefox")
time.sleep(2) # Wait for the search to finish
controller.k_single_press(Key.enter) # Start firefox

# Wait for Firefox to load
done = False
while not done:
    img = np.array(sct.grab(FIRST_TAB_BOX))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    desc = computeDescriptors(orb, img)
    matches = bf.match(newTabDescriptors, desc)
    distance = 0
    for match in matches:
        distance += match.distance
    distance /= len(matches)
    if (distance <= 55):
        done = True
    else:
        controller.k_combination(KeyCombinations.MAXIMISE_WINDOW)
    time.sleep(0.5)
    

# Activate the address bar
controller.m_move_now(ADDRESS_BAR)
controller.m_left_click()

# Go to the youtube subscription feed
controller.k_type("https://www.youtube.com/feed/subscriptions")
controller.k_single_press(Key.enter)