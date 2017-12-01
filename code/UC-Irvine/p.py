def ppredict(weight=None, minimum=1):
    """Predict by degree product (preferential attachment)
    Parameters
    ----------
    weight : None or string, optional
        If None, all edge weights are considered equal.
        Otherwise holds the name of the edge attribute used as weight.
    minimum : int, optional (default = 1)
        If the degree product is below this minimum, the corresponding
        prediction is ignored.
    """
    res = linkpred.predictors.Scoresheet()
    for a, b in degProduct.likely_pairs():
        w = linkpred.predictors.neighbour.neighbourhood_size(degProduct.G, a, weight) *\
            linkpred.predictors.neighbour.neighbourhood_size(degProduct.G, b, weight)
        if w >= minimum:
            res[(a, b)] = w
    return res