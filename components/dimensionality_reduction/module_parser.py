""" module parameters parser"""

import argparse
def pca_parser():

    '''
     instantiate parser for module arguments

     return: argument parser
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--input-dir', help='Dataset to fit')
    parser.add_argument('--output-dir', type=str,
                        help="dataframe containing embedding to output")
    parser.add_argument('--model-output-dir',
                        help='Model for transform: fit_transform mode')
    parser.add_argument('--pca-type', type=str,
                        help='type of Principal component Analysis')
    parser.add_argument('--n-components', type=int,
                        help=f'number of components')
    parser.add_argument('--seed', type=int, default=123,
                        help='Seed for reproduciblity')

   # =============== Sparse PCA=====================
    parser.add_argument('--sparse-alpha', type=int, default=1,
                        help=f'Sparse PCA:Sparsity controlling parameter')
    parser.add_argument('--ridge-alpha', type=float, default=0.01,
                        help=f'Sparse PCA: Amount of ridge shrinkage')
    parser.add_argument('--sparse-method', type=str, default='lars',
                        help=f'Sparse PCA: method type to fit lasso')
    parser.add_argument('--sparse_iterations', type=int, default=1000,
                        help=f'Number of iteration ')
    parser.add_argument('--sparse_tolerance', type=float, default=1e-08,
                        help=f'tolerance for stopping condition')

   #================ Kernel PCA =======================
    parser.add_argument('--kernel', type=str, default='rbf',
                        help=f'Sparse PCA:Sparsity controlling parameter')
    parser.add_argument('--gamma', type=float, default=None,
                        help=f'Sparse PCA: Amount of ridge shrinkage')
    parser.add_argument('--degree', type=float, default=3,
                        help=f'Sparse PCA: method type to fit lasso')
    parser.add_argument('--coef0', type=float, default=1,
                        help=f'Sparse PCA:Sparsity controlling parameter')
    parser.add_argument('--eigen-solver', type=str, default='auto',
                        help=f'Eigensolver to use')
    parser.add_argument('--kernel-tolerance', type=float, default=0,
                        help=f'tolerance for stopping condition')
    parser.add_argument('--omit-0-eig', type=bool, default=False,
                        help=f'remove zero eigen values')
    parser.add_argument('--kernel-max-iters', type=int, default=None,
                        help=f'Arpack maximum iterations')

    #================ Incremental PCA =======================
    parser.add_argument('--inc-whiten', type=bool, default=False,
                        help=f'divide n_components by number of samples\
                          to ensure unit variance component wise')

   #===================PCA==========================
    parser.add_argument('--whiten', type=bool, default=False,
                        help=f'divide n_components by number of samples\
                          to ensure unit variance component wise')
    parser.add_argument('--svd-solver', type=str, default='auto', help=f'SVD solver to use')
    parser.add_argument('--tolerance', type=float, default=0.0,
                        help=f'tolerance for stopping condition')
    parser.add_argument('--iterated-power', type=str, default='auto',
                        help=f'number of iterations for power method\
                            when using randomized SVD solver')

    return parser
