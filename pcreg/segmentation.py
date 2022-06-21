#!/usr/bin/env python3

import cc3d
from skimage.measure import label
from skimage.measure import regionprops
from skimage.measure import label2rgb


def instance_segnmentation(img, background, arr_type):
    '''
    Perform instance segmentation of puncta
    args:   img        -> numpy array of the image
            background -> background pixel value of the image
            arr_type   -> type of array for casting (uint8, uint16 etc.)
    returns: labeled image (numpy array)
    '''

    labeled_img = label(img=img, background=background).astype(arr_type)
    return labeled_img


def connected_components(img, delta, arr_type):
    '''
    Segment a 3D section correctly
    args:   img              -> numpy array of the image
            delta            -> extent of neighbor voxel values
            arr_type(string) -> type of array for casting (uint8, uint16 etc.)
    returns: image with connected labels
    '''
    seg = np.array(img).astype(arr_type)
    labels_out = cc3d.connected_components(seg, delta=delta)
    return labels_out

