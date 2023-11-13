# conda activate atr_env_1
import argparse
from Evaluation.evaluate import Evaluate
def main(args):
   

    if args.Eval:
        print(f'[INFO]: Model Evaluate in progress')
        evl = Evaluate()
        evl.main(args)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--Eval', type=bool, default=True, help='if evaluate is needed')
    parser.add_argument('--labels', type=str, default='Evaluation_MRSSD/labels/', help='path to the ground truth')
    parser.add_argument('--preds', type=str, default='Evaluation_MRSSD/predicted_5999/', help='path to the predicted labels')
    #parser.add_argument('--preds', type=str, default='Evaluation/predicted_3999/', help='path to the predicted labels')
    parser.add_argument('--result', type=str, default='evaluate/', help='evaluation result file path')
    args = parser.parse_args()
    main(args)
    #atr_utils(args)


