from yacs.config import CfgNode as CN
import SimpleITK as sitk

# copied from Jack's branch (thanks man :P)
# config definition

_C = CN()

# system
_C.SYSTEM = CN()

# filter
_C.FILTER = CN()
# thresholding, denoising and masking params
_C.FILTER.FILTER_STRENGTH = 70
_C.FILTER.THRESH_LOWER = 60
_C.FILTER.THRESH_UPPER = 255
_C.FILTER.MASK_INDEX = 6
_C.FILTER.DELTA = 230

# intensity
_C.INTENSITY = CN()
# elastix params
_C.INTENSITY.RESOLUTION = [0.1625, 0.1625, 0.2500]
_C.INTENSITY.TRANSFORM_TYPE = ['affine']
_C.INTENSITY.NumberOfSamplesForExactGradient = '100000'
_C.INTENSITY.MaximumNumberOfIterations = '10000'
_C.INTENSITY.MaximumNumberOfSamplingAttempts = '15'
_C.INTENSITY.FinalBSplineInterpolationOrder = '1'

# point
_C.POINT = CN()
# point-based registration params
_C.POINT.NUM_POINTS = 7
_C.POINT.MAX_ITER = 50
_C.POINT.TOLERANCE = 1

# dataset
_C.DATASET = CN()
# dataset paths, fovs, base channels
_C.DATASET.VOL_FIX_PATH = '/path/to/vol_fix'
_C.DATASET.VOL_MOVE_PATH = '/path/to/vol_move'
_C.DATASET.BASE_CHANNEL = None


def get_cfg_defaults():
    r"""Get a yacs CfgNode object with default values for my_project."""
    # return a clone so that variables won't be altered.
    # this is for the "local variable use pattern"
    return _C.clone()

