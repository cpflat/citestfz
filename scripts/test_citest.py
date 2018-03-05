#!/usr/bin/env python
# coding: utf-8

import numpy as np

from citestfz.ci_tests import ci_test_gauss
import gauss_testdata

dm = np.array(gauss_testdata.data)
cm = np.corrcoef(dm.T)

v = ci_test_gauss(dm, 0, 2, [1], corr_matrix = cm)
print("x = 0, y = 2, z = [1] : {0} (R:0.787275)".format(v))
v = ci_test_gauss(dm, 0, 2, [], corr_matrix = cm)
print("x = 0, y = 2, z = Null : {0} (R:1.11125330537e-53)".format(v))

