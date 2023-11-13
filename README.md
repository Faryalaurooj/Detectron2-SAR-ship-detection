# Detectron2-SAR-ship-detection
In this repo, we will train detectron2 retinanet model on SAR images of ships and perfrom object detection
Detectron2 is Facebook's new vision library that allows us to easily use and create object detection, instance segmentation, keypoint detection, and panoptic segmentation models. Here we will use it for a difficuilt computer vision task, detection of ships from synthetic aperture radar (SAR) images. We performed testing with three public datasets and got following results.
![MRSSD_7000ITERS_LR_0 001](https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection/assets/138756263/63917313-c8ee-4de9-be0b-f4d73019a6bf)
![output_SSDD_7350ITERS_LR_0 001](https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection/assets/138756263/9626dc60-94c0-4300-bba2-92cc0d2efa49)
[all_results_comparison.ods](https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection/files/13330892/all_results_comparison.ods)

# Quick Start
Download the repo and perfrom necessary installations
```
git clone https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection
pip install requirements.txt
```
#Installation 
If you find any difficuilty in installations , follow this page for torchvision and cuda installations 
```
https://detectron2.readthedocs.io/en/latest/tutorials/install.html
```
# Task introduction 
We have only one class for object detection i.e class 0 ship

We are using three datasets :
1. SAR Ship Detection Dataset (SSDD) : images = 1160  : sensors = 3
```
https://www.mdpi.com/2072-4292/13/18/3690
```
2. SAR Ships Dataset : images = 43,819  : sensors = 2
```
https://github.com/CAESAR-Radi/SAR-Ship-Dataset
```
4. iVision-MRSSD : images = 11,590   : sensors = 6
```
https://www.sciencedirect.com/science/article/pii/S2352340923006054?ssrnid=4504348&dgcid=SSRN_redirect_SD
```
# 
