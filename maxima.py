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

        # create a canditate list
        cand = [];

        # check the left boundary
        if x[0] > x[1]:
            idx.append(0)

        # loop over the array
        for i in range(0,leng-1,1):

            # check a pair
            if x[i] < x[i+1] and len(cand) == 0: 

                # cand.append(i+1); 
                cand = [i+1]; 

            elif x[i] == x[i+1] and len(cand) > 0:

                cand.append(i+1); 

            elif x[i] > x[i+1] and len(cand) > 0: 

                for j in range(0,len(cand)):
                    idx.append(cand[j]); 

                print(idx)

                cand = [];

            elif x[i] < x[i+1] and len(cand) > 0: 

                cand = [i+1];

        if len(cand) > 0: 

            for j in range(0,len(cand)):
                idx.append(cand[j]); 

    return idx

