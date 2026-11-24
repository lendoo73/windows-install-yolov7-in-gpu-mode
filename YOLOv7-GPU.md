# YOLOv7 GPU

Change:

```txt
numpy>=1.18.5,<1.24.0
```

to:

```txt
numpy>=1.26.4
```

Then:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python detect.py --weights yolov7.pt --source inference/images/horses.jpg
```

Then you can see the result in `runs/detect/exp` folder.

## 11-41. Windows : YOLOv7 Object Detection on image (GPU Mode)

```shell
python detect.py --weights yolov7.pt --conf-thres 0.5 --img-size 640 --source inference/images --view-img --save-txt
```

## 11-42. Windows : YOLOv7 Object Detection on video and webcam (GPU Mode)

video:
```shell
python detect.py --weights yolov7.pt --conf-thres 0.5 --img-size 640 --source inference/video --view-img
```

webcam:
```shell
python detect.py --weights yolov7.pt --conf-thres 0.5 --img-size 640 --source 0 --view-img
```
