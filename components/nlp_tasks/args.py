"""Module's arguments holder"""


import argparse


def module_args_parser():

    ''' Module Argument praser

        return argument parser
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('--train-dir', type=str)
    parser.add_argument('--eval-dir', type=str)
    parser.add_argument('--output-dir', type=str)
    parser.add_argument('--metrics-output-dir', type=str)
    parser.add_argument('--tb-logs', type=str)
    parser.add_argument('--model-output-dir', type=str)
    parser.add_argument('--task', type=str,
                        default='binary classification')
    parser.add_argument('--seed', type=int)
    parser.add_argument('--n-gpu', type=int,
                        default=1)
    parser.add_argument('--model-type', type=str,
                        default=None)
    parser.add_argument('--bert-model-name', type=str,
                        default=None)
    parser.add_argument('--xlnet-model-name', type=str,
                        default=None)
    parser.add_argument('--xlm-model-name', type=str,
                        default=None)
    parser.add_argument('--roberta-model-name', type=str,
                        default=None)
    parser.add_argument('--albert-model-name', type=str,
                        default=None)
    parser.add_argument('--camembert-model-name', type=str,
                        default=None)
    parser.add_argument('--xlmroberta-model-name', type=str,
                        default=None)
    parser.add_argument('--flaubert-model-name', type=str,
                        default=None)
    parser.add_argument('--distilbert-model-name', type=str,
                        default=None)
    parser.add_argument('--electra-model-name', type=str,
                        default=None)
    parser.add_argument('--max-seq-length', type=int,
                        default=128)
    parser.add_argument('--num-train-epochs', type=int,
                        default=1)
    parser.add_argument('--train-batch-size', type=int,
                        default=8)
    parser.add_argument('--eval-batch-size', type=int,
                        default=8)
    parser.add_argument('--learning-rate', type=float,
                        default=4e-5)
    parser.add_argument('--epsilon-adam', type=float,
                        default=1e-8)
    parser.add_argument('--warmup-steps', type=int,
                        default=0)
    parser.add_argument('--warmup-ratio', type=float,
                        default=0.06)
    parser.add_argument('--weight-decay', type=int,
                        default=0)
    parser.add_argument('--gradient-accumulation-steps', type=int,
                        default=1)
    parser.add_argument('--max-grad-norm', type=float,
                        default=1.0)
    parser.add_argument('--do-lower-case', type=bool,
                        default=False)
    parser.add_argument('--text-column', type=str)
    parser.add_argument('--label-column', type=str)

    return parser


def score_arg_parser():
    """Arugment parser for score module"""

    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', help='Dataset to score')
    parser.add_argument('--model-input-dir', type=str,
                        help="path to model input directory")
    parser.add_argument('--text-column', type=str,
                        help="Text column name")
    parser.add_argument('--output-dir', type=str, help="Output Dataframe")

    return parser
