from numpy import array

def lena():
    """
    NB this code was copied from scipy v 0.16. It is meant to be a replacement
    for scipy.misc.lena as that is no longer available. If you don't need to
    use lena, please use scipy.misc.face or scipy.misc.ascent.

    Get classic image processing example image, Lena, at 8-bit grayscale
    bit-depth, 512 x 512 size.
    Parameters
    ----------
    None
    Returns
    -------
    lena : ndarray
        Lena image
    Notes
    -----
    Though safe for work in most places, this sexualized image is drawn from
    Playboy and makes some viewers uncomfortable.  It has been very widely
    used as an example in image processing and is therefore made available
    for compatibility.  For new code that needs an example image we recommend
    `face` or `ascent`.
    Examples
    --------
    >>> import scipy.misc
    >>> lena = scipy.misc.lena()
    >>> lena.shape
    (512, 512)
    >>> lena.max()
    245
    >>> lena.dtype
    dtype('int32')
    >>> import matplotlib.pyplot as plt
    >>> plt.gray()
    >>> plt.imshow(lena)
    >>> plt.show()
    """
    import pickle
    import os
    fname = os.path.join(os.path.dirname(__file__),'lena.dat')
    f = open(fname,'rb')
    lena = array(pickle.load(f))
    f.close()
    return lena
