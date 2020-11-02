# pylint: disable=W1202

""" dimensionality reductions transformers class module"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA, SparsePCA, KernelPCA, IncrementalPCA
from azureml.core.run import Run


class PCAModule():
    """
        Dimensionality reduction class
       provide support for PCA, sparse, kernel and incremental PCA
    """

    def __init__(self, args):
        '''
            Setup transformers map &
            initialize model according to requested type
            args:dict dictionary of transformer user paramerters

        '''

        pca_type_mapper = {'PCA':('pca', PCA),\
                           'Sparse PCA':('sparse', SparsePCA),\
                           'Kernel PCA':('kernel', KernelPCA),\
                           'Incremental PCA':('incremental', IncrementalPCA)}

        assert args.pca_type in pca_type_mapper.keys()
        self.pca_type = pca_type_mapper[args.pca_type][0]

        params = self.get_signature(args)
        self.pca_instance = pca_type_mapper[args.pca_type][1](**params)

    def fit_transform(self, input_df):
        '''

        Fit PCA based on one of the supported types by PCAModule

        args:
            input_df: Pandas dataframe
            params: dictionary parameters of PCA call

        return dataframe containing principal components

        '''

        x_new = self.pca_instance.fit_transform(input_df.values)
        return pd.DataFrame(x_new, columns=[f'component_{str(i)}' for i in range(x_new.shape[1])])

    def log_metrics(self, col_names):
        '''
          track transformers attributes as run metrics

          args:list columns names

        '''
        run = Run.get_context()

        if self.pca_type in ['pca', 'incremental']:
            run.log_list('Cumulative explained variance',
                         np.cumsum(self.pca_instance.explained_variance_ratio_).tolist())
            run.log_list('Singular values', np.cumsum(self.pca_instance.singular_values_).tolist())
            for col, mean in zip(col_names, self.pca_instance.mean_.tolist()):
                run.log(f'Estimated mean_of_{col}', mean)

            if self.pca_type == 'incremental':
                for col, var in zip(col_names, self.pca_instance.var_.tolist()):
                    run.log(f'Estimated variance_of_{col}', var)
                run.log('noise variance', self.pca_instance.noise_variance_)

        elif self.pca_type == 'kernel':
            run.log_list("eigenvalues of the kernel matrix (lambdas)",
                         self.pca_instance.lambdas_.tolist())

        elif self.pca_type == 'sparse':
            run.log_list('Error vector', self.pca_instance.error_)

    def transform(self, input_df):
        '''
         Trasform dataset using previsously fitted PCA
         using on one of the supported types by PCAModule

         args:
            input_df: Pandas dataframe

        return dataframe containing principal components

        '''

        x_new = self.pca_instance.transform(input_df.values)
        return pd.DataFrame(x_new, columns=[f'component_{str(i)}' for i in range(x_new.shape[1])])

    def get_signature(self, args):
        '''
        map user parameters to transformer arguments

        args:
            args:dict user paramater
            pca_type: str requested transformer type

        '''
        if self.pca_type == 'sparse':
            pca_params = {'n_components':args.n_components, 'alpha':args.sparse_alpha,
                          'ridge_alpha':args.ridge_alpha, 'max_iter':args.sparse_iterations,
                          'tol':args.sparse_tolerance, 'method':args.sparse_method,
                          'n_jobs':None, 'U_init':None, 'V_init':None, 'verbose':False,
                          'random_state':args.seed}

        elif self.pca_type == 'kernel':
            pca_params = {'n_components':args.n_components, 'kernel':args.kernel,
                          'gamma':args.gamma, 'degree':args.degree,
                          'coef0':args.coef0, 'kernel_params':None,
                          'alpha':1.0, 'fit_inverse_transform':False,
                          'eigen_solver':args.eigen_solver, 'tol':args.kernel_tolerance,
                          'max_iter':args.kernel_max_iters, 'remove_zero_eig':args.omit_0_eig,
                          'random_state':args.seed, 'copy_X':True, 'n_jobs':None}

        elif self.pca_type == "incremental":
            pca_params = {'n_components':args.n_components, 'whiten':args.inc_whiten,
                          'copy':True, 'batch_size':None}


        elif self.pca_type == "pca":
            pca_params = {'n_components':args.n_components, 'copy':True,
                          'whiten':args.inc_whiten, 'svd_solver':args.svd_solver,
                          'tol':args.tolerance, 'iterated_power'\
                            :args.iterated_power, 'random_state':args.seed}

        return pca_params
