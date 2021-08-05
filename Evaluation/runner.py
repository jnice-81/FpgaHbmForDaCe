from hbm_blas_operators import *
import numpy as np

def rand_arr(shape):
    fix = False

    if fix:
        a = np.ones(shape)
    else:
        a = np.random.rand(*shape)
    a = a.astype(np.float32)
    return a

def run_and_time(sdfg, **kwargs):
    sdfg(kwargs)

def run_axpy(input_size, vec_size, banks_per_input):
    x = rand_arr([input_size])
    y = rand_arr([input_size])

    sdfg = only_hbm_axpy_sdfg(vec_size, banks_per_input)
    run_and_time(x=x, y=y)

