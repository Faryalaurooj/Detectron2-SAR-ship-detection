In this repo we will perfrom object detection for ships from SAR (synthtic aperture radara) images
![MRSSD_7000ITERS_LR_0 001](https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection/assets/138756263/c38a44f9-2629-4136-97cf-111aa870491c)
![SSDD_7350ITERS_LR_0 01](https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection/assets/138756263/4ba75929-b2e7-449c-8b43-fb5bc1887937)
![output_SSDD_7350ITERS_LR_0 001](https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection/assets/138756263/ac5f3a49-11de-4ef2-adbf-cee64430aa44)
[all_results_comparison.ods](https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection/files/13330960/all_results_comparison.ods)
![Alo_75_1_2](https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection/assets/138756263/4e0a5017-65b9-4dfa-af51-63de931082a0)
![Paz_14_11_20](https://github.com/Faryalaurooj/Detectron2-SAR-ship-detection/assets/138756263/9576ba26-70f5-4f8d-b259-65d5a3fb994e)

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
# Dataset 
 annotations should be provided in yolo format, this is: 
            class, xc, yc, w, h
    data needs to follow this structure:
    
    data-dir
    ----- train
    --------- imgs
    ------------ filename0001.jpg
    ------------ filename0002.jpg
    ------------ ....
    --------- anns
    ------------ filename0001.txt
    ------------ filename0002.txt
    ------------ ....
    ----- val
    --------- imgs
    ------------ filename0001.jpg
    ------------ filename0002.jpg
    ------------ ....
    --------- anns
    ------------ filename0001.txt
    ------------ filename0002.txt
    ------------ ....
    
# Train
For training perfrom following command
```
python train.py  --iterations=7000  --model = COCO-Detection/retinanet_R_101_FPN_3x.yaml  -device = gpu
```
in the train.py file set the data directory path where you have placed your training data . Set the output directory , make first a folder and give its path to save the results xyz.pth files

# Predict
To perfrom predict perfrom following command 
```
python predict.py
```

It will run prediction on all the images in val folder from data directory and save the ann labels inside evaluation folder



# Evaluation
NOw we will calculate the IOU , Precision , REcall on the results from predict
Perfrom following command
```
python eval.py
```

It will first calculate the IOU values by running evaluate.py file from the Evaluation folder. INside this folder there should be following folders : val "anns" , copied also as "labels" and third one you have to manually made predicted_xvz folder for the predicted results with whichever weight file are you perfroming evaluation. If you have trained for 7000 iterations and you only want to check the Precision REcall F1 score from last weights then make a predicted_6999 folder. IN this folder , the .txt files will automatically save when you run the predict.py. When you run the eval.py then model will compare the labels from ground truth folder saved as label and labels inside predicted folder and calculate IOU which it will evantually use to calculate remaining prformance metrices.


