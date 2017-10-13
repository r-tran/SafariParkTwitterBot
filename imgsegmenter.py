"""
This module leverages the scikit-image image processing library:
    http://scikit-image.org/

We will use the segmentation algorithm leveraging K-means clustering to slice an
image in a 3D space.
"""

from skimage import segmentation, color

class ImageSegmenter(object):
    """Class that performs the segmentation algorithm on an image"""
    def transform(self, i):
        labels = segmentation.slic(i, compactness=10, n_segments=1000)
        return color.label2rgb(labels, i, kind='avg')
