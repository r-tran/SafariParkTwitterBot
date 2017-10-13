"""
Module used to apply segmentation algorithm on image
"""

from skimage import io, segmentation, color

class ImageSegmenter(object):
    """Perform segmentation on image"""
    def transform(self, i):
        labels = segmentation.slic(i, compactness=10, n_segments=1000)
        return color.label2rgb(labels, i, kind='avg')
