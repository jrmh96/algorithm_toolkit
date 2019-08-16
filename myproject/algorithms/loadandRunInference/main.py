from algorithm_toolkit import Algorithm, AlgorithmChain
import traceback
import json

from assets.detect import *

import torch

class Main(Algorithm):

    def run(self):
        cl = self.cl  # type: AlgorithmChain.ChainLedger
        params = self.params  # type: dict
        # Add your algorithm code here
        try:
            paramJsonObj = params['parametersJSON']
            print(paramJsonObj)
            #cfgpath = paramJsonObj["cfg_file_path"]
            cfgpath = 'assets/data/yolov3.cfg'
            #weightspath = paramJsonObj['weights_file_path']
            weightspath = 'assets/data/yolov3.weights'
            #dataPath = paramJsonObj['data_cfg_path']
            dataPath = 'assets/data/coco.data'
            #file_path = paramJsonObj['file_path']
            file_path = 'assets/data/raptorsParade.mp4' # hardcoded for docker demo
            output_path = paramJsonObj['output_path'] if 'output_path' in paramJsonObj else 'output'
            fourcc = paramJsonObj['fourcc'] if 'fourcc' in paramJsonObj else 'H264'
            img_size = paramJsonObj['img_size']
            conf_thresh = paramJsonObj['conf_thresh']
            nms_thresh = paramJsonObj['nms_thresh']
            backend = paramJsonObj['backend'] == 'CPU'
            #save_txt = paramJsonObj['save_text']
            #save_images = paramJsonObj['save_images']
            save_txt = False
            save_images = False
            #includetwittergraph = paramJsonObj['twitter']
            includetwittergraph = True
            twitterObj = {}
            twitterKeys = ['fromDate', 'toDate', 'lon', 'lat']
            twitterQuery = {
                'fromDate': '201906171300',
                'toDate': '201906171820',
                'lon': -79.384753,
                'lat': 43.647595
            }
            for i in twitterKeys:
                if i in paramJsonObj:
                    #twitterObj[i] = paramJsonObj[i]
                    twitterObj[i] = twitterQuery[i]

            class_of_interest = paramJsonObj['class_of_interest'] # some image of interest to track

            with torch.no_grad(): # no gradients needed bc no backprop needed
                image_data_obj = detect(
                    cfgpath,
                    dataPath,
                    weightspath,
                    file_path,
                    output_path,
                    fourcc,
                    img_size,
                    conf_thresh,
                    nms_thresh,
                    save_txt,
                    save_images,
                    backend,
                    class_of_interest,
                    includetwittergraph,
                    twitterObj
                )

            if len(image_data_obj) != 0:
                # add in twitter information here, add location and time range as inputs in config json
                cl.add_to_metadata('image_data_obj', image_data_obj)

        except json.decoder.JSONDecodeError as e:
            self.raise_client_error('Error thrown in load and run inference: error parsing json parameters: ' + str(e))
        except KeyError as e:
            self.raise_client_error('Error thrown in load and run inference: missing key value in json parameters: ' + str(e))
        except Exception as e:
            self.raise_client_error('Error thrown in load and run inference: ' + traceback.format_exc())

        # Do not edit below this line
        return cl
