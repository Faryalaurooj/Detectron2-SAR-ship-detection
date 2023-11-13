from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2 import model_zoo
import cv2
import shutil

# Load config from a config file
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file('COCO-Detection/retinanet_R_101_FPN_3x.yaml'))
#cfg.MODEL.WEIGHTS = './output_ssdd/model_0002999.pth'
#cfg.MODEL.WEIGHTS = './output/model_0003499.pth'
#cfg.MODEL.WEIGHTS = './output/model_0003999.pth'
#cfg.MODEL.WEIGHTS = './output_ssdd/model_0006999.pth'
#cfg.MODEL.WEIGHTS = './output/model_0020999.pth'
#cfg.MODEL.WEIGHTS = './output/model_0000499.pth'
#cfg.MODEL.WEIGHTS = './output/model_0001499.pth'
#cfg.MODEL.WEIGHTS = './output/model_0005499.pth'
cfg.MODEL.WEIGHTS = './output_MRSSD_7000ITERS_LR_0.001/model_0003499.pth'

#cfg.MODEL.WEIGHTS = './detectron2/detectron2/model_zoo/model_final_971ab9.pkl'
#/home/caic/Downloads/train-object-detector-detectron2/detectron2/detectron2/model_zoo
cfg.MODEL.DEVICE = 'cpu'

# Create predictor instance
predictor = DefaultPredictor(cfg)

# Load image
#image = cv2.imread("./data/val/imgs/3e115eab82413cd4.jpg")
def normalize(x1,y1, x2,y2, height,width):
    w = x2-x1
    h = y2-y1


    x = x1 + (w)//2
    y = y1 + (h)//2

    x = x/width
    y = y/height

    w = w/width
    h = h/height

    return [x,y,w,h]




import glob
for filess in glob.glob('MRSSD_data/val/imgs/*.jpg'):
    image = cv2.imread(filess)
    height, width, c = image.shape
    fil = filess
    name = fil.split('/')[-1].split('.')[0]


    # Perform prediction
    outputs = predictor(image)

    print(outputs)


    threshold = 0.5

    # Display predictions
    preds = outputs["instances"].pred_classes.tolist()
    scores = outputs["instances"].scores.tolist()
    bboxes = outputs["instances"].pred_boxes
    print(name)
    with open('Evaluation_MRSSD/predicted_3499/' + name + '.txt', 'w') as f:

        for j, bbox in enumerate(bboxes):
            bbox = bbox.tolist()

            score = scores[j]
            pred = preds[j]

            if score > threshold:
                x1, y1, x2, y2 = [int(i) for i in bbox]
                normalize_list = normalize(x1,y1,x2,y2, height, width)
                normalize_list.insert(0,pred)
                normalize_list = [str(x) for x in normalize_list]
                data = ' '.join(normalize_list)

                f.write(data)
                print(normalize_list)


                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 5)
    #break
    #cv2.imshow('image', image)
    #cv2.waitKey(0)