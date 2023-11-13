In this repo we will perfrom object detection for ships from SAR (synthtic aperture radara) images
![MRSSD_7000ITERS_LR_0 001](https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection/assets/138756263/c38a44f9-2629-4136-97cf-111aa870491c)
![SSDD_7350ITERS_LR_0 01](https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection/assets/138756263/4ba75929-b2e7-449c-8b43-fb5bc1887937)
![output_SSDD_7350ITERS_LR_0 001](https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection/assets/138756263/ac5f3a49-11de-4ef2-adbf-cee64430aa44)
[all_results_comparison.ods](https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection/files/13330960/all_results_comparison.ods)

#Quick Start
Download the git 
```
https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection/edit/main/README.md
```

#Requirements
for the installations follow this 
```
pip install requirements.txt
```
and here is an additional link 
```
https://detectron2.readthedocs.io/en/latest/tutorials/install.html
```

#TAsk introductiion
We have trained detectron2 retinanet model on three public datasets for ship detection task:

1. SAR Ship Detection Dataset (SSDD)   : Images = 1160  : Sensor = 3
2. SAR-Ships Dataset   : Images = 43,819 :  Sensor = 2
3. iVision-MRSSD Dataset : Images =  11,590 :  Sensor = 06

We have only one class i.e. class 0 = ship.
We perfromed training on Windows 10 Pro operating system, Intel core-i7 CPU, 32 GB RAM, 2TB HDD and NVIDIA RTX GeForce 2080 GPU with 8 GB graphics memory.
