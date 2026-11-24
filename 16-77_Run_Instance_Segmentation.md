# 16-77. Run Instance Segmentation

Instance segmentation on an image.
```shell
python detect_mask.py \
    --weights yolov7-mask.pt \
    --source inference/images/bus.jpg \
    --view-img
```

Instance segmentation on a video.
```shell
python detect_mask.py \
    --weights yolov7-mask.pt \
    --source inference/video/road.mp4 \
    --view-img
```

Instance segmentation on a webcam.
```shell
python detect_mask.py \
    --weights yolov7-mask.pt \
    --source 0
```