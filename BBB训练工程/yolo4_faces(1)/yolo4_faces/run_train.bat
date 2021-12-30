python train.py ^
--epochs 1000  ^
--batch-size 4 ^
--data datasets/faces.data ^
--cfg cfg/yolov4-tiny.cfg ^
--weights weights/last.pt ^
--name yolov4-tiny ^
--img 640 640 640