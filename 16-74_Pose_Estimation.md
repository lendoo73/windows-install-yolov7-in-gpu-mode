# 16-74. Pose Estimation

Pose estimation on an image.
```shell
python detect_pose.py \
    --weights yolov7-w6-pose.pt \
    --source inference/images/pose.png \
    --kpt-label \
    --view-img
```

Pose estimation on a video.
```shell
python detect_pose.py \
    --weights yolov7-w6-pose.pt \
    --source inference/video/pose-video.mp4 \
    --kpt-label \
    --view-img
```