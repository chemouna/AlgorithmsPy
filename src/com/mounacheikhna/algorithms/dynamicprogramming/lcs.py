def lcs(xs, ys):
    """
    Return a longest common subsequence of xs and ys.
    """
    if xs and ys:
        *xb, xe = xs  # split xs into its beginning, xb, and its final element xe
        *yb, ye = ys
        if xe == ye:
            return lcs(xb, ys) + [xe]
        else:
            return max(lcs(xb, ys), lcs(xs, yb))
    else:
        return []


print(lcs("HUMAN", "CHIMPANZEE"))

