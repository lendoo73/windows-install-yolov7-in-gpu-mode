# 13-52. Windows : Perform training and see the accuracy graph using Tensorboard

```shell
python train.py \
    --workers 0 \
    --batch-size 4 \
    --device 0 \
    --data data/face_mask.yaml \
    --img 640 \
    --cfg cfg/training/yolov7-face_mask.yaml \
    --weights yolov7_training.pt \
    --name yolov7-face_mask \
    --hyp data/hyp.scratch.custom.yaml \
    --epochs 300
```

```shell
tensorboard --logdir=runs/train
```

## 53. Windows : How to continue an unfinished training

```shell
python train.py \
    --workers 0 \
    --batch-size 4 \
    --device 0 \
    --data data/face_mask.yaml \
    --img 640 \
    --cfg cfg/training/yolov7-face_mask.yaml \
    --weights runs/train/yolov7-face_mask/weights/last.pt \
    --name yolov7-face_mask \
    --hyp data/hyp.scratch.custom.yaml \
    --epochs 300 \
    --resume
```

## 54. Windows : Face Mask Detection

Detect face masks on images.
```shell
python detect.py \
    --weights runs/train/yolov7-face_mask/weights/best.pt \
    --source inference/images/face-mask.png \
    --box-line-width 2
```

Detect face masks on videos.
```shell
python detect.py \
    --weights runs/train/yolov7-face_mask/weights/best.pt \
    --source inference/video/face-mask-video.mp4 \
    --box-line-width 2
```

Detect face masks on webcam.
```shell
python detect.py \
    --weights runs/train/yolov7-face_mask/weights/best.pt \
    --source 0 \
    --box-line-width 2
```