#!/bin/sh
cd /atk_project
bash assets/data/download_yolov3_weights.sh
alg run --host=0.0.0.0
