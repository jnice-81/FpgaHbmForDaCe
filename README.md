# FpgaHbmForDaCe

This is a support repository containing work related to the bachelor thesis "Accelerating FPGA Applications in DaCe with High-Bandwidth Memory", that is not part of the main DaCe repository. It contains several different implementations of SCAL used to checkout the pitfalls of HBM on the Xilinx Alveo U280 FPGA. Also it contains code for evaluating the integration of HBM into DaCe. More concretly it provides implementations of some simple BLAS Applications (Axpy, Dot, Gemv, AxpyDot) for DaCe that target the use of HBM on the Xilinx Alveo U280. The associated thesis can be found at the [ETH Research Collection](https://www.research-collection.ethz.ch/handle/20.500.11850/505519).

# DaCe

[DaCe](https://github.com/spcl/dace) is a programming framework for parallel programming on heterogenous architectures. To run anything inside of [Evaluation](Evaluation) you need to have it installed.

# License

This repository is published under the New BSD license, see [LICENSE](https://github.com/jnice-81/FpgaHbmForDaCe/blob/master/LICENSE). There is one folder, namely [common](SCAL_using_HBM/common), which has it's own License, since it was partially taken from the [Xilinx Vitis examples repository](https://github.com/Xilinx/Vitis_Accel_Examples). It is licensed under Apache-License.
