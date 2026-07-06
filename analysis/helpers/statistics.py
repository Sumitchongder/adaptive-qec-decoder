import numpy as np


def confidence_interval(x):

    x=np.asarray(x)

    mean=x.mean()

    std=x.std(ddof=1)

    ci=1.96*std/np.sqrt(len(x))

    return mean,std,ci
