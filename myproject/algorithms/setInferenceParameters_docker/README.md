# Set Inference Parameters (Docker demo)
Set parameters for object detection model. For simpler demo, config files (*.weights, *.data, etc) are included and hardcoded
Version: 0.0.1
License: MIT
Homepage: []

## Parameters:
Name|Description|Required
---|---|:---:
class_of_interest|Track instances of this class across the video. Results will be output as graph on the chain output screen|Yes
img_size|Image resized to img_size x img_size during inference. If unsure, default value generally works well|
fourcc|Four character code for output video encoding|
conf_thresh|Confidence threshold for image prediction. Predictions with probabilities below this threshold are ignored.|
nms_thresh|Non-maximum suppression threshold for removing duplicate boxes around the same object.|
backend|Backend to use|
save_text|Save text file of bounding box predictions|
save_image|Save Image/Video to output folder. If image/video is not saved, it can be output to browser with outputImageToBrowser algorithm.|
output_path|Include path to output folder if save images is true|
fromDate|Twitter date window yyyymmddhhmm (minute granularity)|
toDate|Twitter date window yyyymmddhhmm (minute granularity)|
lon|Longitude of video location|
lat|Latitude of video location|

## Outputs:
Name|Description
---|---
jsonObject|Parameters JSON object for use as input to load and run inference algorithm
