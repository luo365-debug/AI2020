python test.py  ^
--data datasets/faces.data ^
--cfg cfg/yolov4-tiny.cfg ^
--weights weights/yolov4-tiny.pt ^
--img 640 ^
--iou-thr 0.6 ^
--conf-thres 0.5 ^
--batch-size 1