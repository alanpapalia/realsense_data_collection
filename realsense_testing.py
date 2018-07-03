import logging
logging.basicConfig(level=logging.INFO)

import hand_segmentation as hs
import realsense_controls as rsc
import image_controls as imControl


#prompt to determine stream data to save
print("Do you want to stream color data? (y/n)")
colStrm = raw_input() == 'y'
print("Do you want to stream depth data? (y/n)")
depStrm = raw_input() == 'y'
print("Frame save rate? (0 for no save)")
saveRate = raw_input()
try: saveRate = int(saveRate)
except: saveRate = 0

#if want to save frames, first clear out old ones
if saveRate != 0:
    imControl.clearTestImages()

#initialize realsense device
rs = rsc.RSControl()


if colStrm and depStrm:
    rs.addColorStream()
    rs.addDepStream()
    rs.startColorAndDepthStreams(saveRate)
elif colStrm:
    rs.addColorStream()
    rs.startColorStream(saveRate)
elif depStrm:
    rs.addColorStream()
    rs.addDepStream()
    rs.startDepthStreams(saveRate)

# print("Do you want to segment the depth images? (y/n)")
# if raw_input() == 'y':
#     hs.clearImages()
#     hs.depthImageSegmentation()
