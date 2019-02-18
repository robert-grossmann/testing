def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers

    Output:
        idx -- list of indices of the local maxima in x
    """

    idx = []

    leng = len(x)

    if leng == 1:

        idx.append(0);

    elif leng == 2:
        
        if x[0] > x[1]:
            idx.append(0)
        else:
            idx.append(1)

    else:

        if x[0] > x[1]:
            idx.append(0)

        # check the middle points
        for i in range(1,len(x)-1,1):
            # `i` is a local maximum if the signal decreases before and after it
            if x[i-1] < x[i] and x[i+1] < x[i]:
                idx.append(i)

        # check the right boundary
        leng = len(x)-1;
        if x[leng-1] < x[leng]:
            idx.append(leng)

    return idx
