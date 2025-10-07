def get_root(x, y):
    n_sample, n_features = x.shape
    best_gain=-1.0
    best_feature, best_threshold = None, None

    for feat_idx in range(n_features):
        X_column = x[:, feat_idx]
        thresholds = np.unique(X_column)

        for thr in thresholds:
            gain = info_gain(y, X_column, thr)
            if best_gain < gain:
                best_gain = gain
                best_feature = feat_idx
                best_threshold = thr
