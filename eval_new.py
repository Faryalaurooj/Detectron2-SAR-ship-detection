# conda activate detectron2 environmen
import argparse
import os
from Evaluation.evaluate import Evaluate
def main(args):
   

    if args.Eval:
        print(f'[INFO]: Model Evaluate in progress')
        evl = Evaluate()
        evl.main(args)



if __name__ == '__main__':
    
   # parser.add_argument('--preds', type=str, default='Evaluation/predicted_3499/', help='path to the predicted labels')
    for i in os.listdir('/home/caic/Downloads/train-object-detector-detectron2/Evaluation'):
        if 'model' in i:
            parser = argparse.ArgumentParser()
            parser.add_argument('--Eval', type=bool, default=True, help='if evaluate is needed')
            parser.add_argument('--labels', type=str, default='Evaluation/labels/', help='path to the ground truth')
            parser.add_argument('--preds', type=str, default='Evaluation/'+ i+ '/', help='path to the predicted labels')
            parser.add_argument('--result', type=str, default='evaluate/', help='evaluation result file path')
            args = parser.parse_args()
            main(args)
        else:
            pass
