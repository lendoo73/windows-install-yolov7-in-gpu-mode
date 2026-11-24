# 15-72. YOLOv7: Accuracy Measurement using Mean Average Precision

Calculating the accuracy on validation data.
```shell
python test.py \
    --weights runs/train/yolov7-face_mask/weights/best.pt \
    --batch-size 2 \
    --device 0 \
    --data data/face_mask.yaml \
    --img 640 \
    --conf-thres 0.01 \
    --iou 0.5 \
    --name yolov7-face_mask-val \
    --task val \
    --no-trace
```

Calculating the accuracy on test data.
```shell
python test.py \
    --weights runs/train/yolov7-face_mask/weights/best.pt \
    --batch-size 2 \
    --device 0 \
    --data data/face_mask.yaml \
    --img 640 \
    --conf-thres 0.01 \
    --iou 0.5 \
    --name yolov7-face_mask-test \
    --task test \
    --no-trace
```