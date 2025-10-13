#!/usr/bin/env python
# coding: utf-8

#
import warnings

warnings.filterwarnings("ignore")

#
import numpy as np
import pandas as pd
import itertools
import argparse

#
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score
from scipy.stats import spearmanr
from scipy.stats import pearsonr


def cross_validation(clf, X, y, prop_value):
    # 5 folds cross validation score
    from sklearn.model_selection import cross_validate, KFold
    kf = KFold(n_splits=10, random_state=0, shuffle=True)
    scoring = {'acc': 'accuracy', 'f1': 'f1', 'rc': 'recall', 'pr': 'precision', 'auc': 'roc_auc'}
    scores = cross_validate(clf, X, y, cv=kf, scoring=scoring)
    acccvmean = scores['test_acc'].mean()
    f1cvmean = scores['test_f1'].mean()
    rccvmean = scores['test_rc'].mean()
    prcvmean = scores['test_pr'].mean()
    auccvmean = scores['test_auc'].mean()

    # calculate spearman score
    spearmans = []
    pearsons = []
    for train_index, test_index in kf.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        clf.fit(X_train, y_train)
        probs = [p[1] for p in clf.predict_proba(X_test)]
        s_score = spearmanr(prop_value[test_index], probs)[0]
        spearmans.append(s_score)
        p_score = pearsonr(prop_value[test_index], probs)[0]
        pearsons.append(p_score)

    return {
        "acc": scores['test_acc'],
        "f1": scores['test_f1'],
        "spearman": spearmans,
        "pearson": pearsons,
        "auc": scores['test_auc'],
        "precision": scores['test_pr'],
        "recall": scores['test_rc'],
        # "pos.ratio": np.mean(y),
        # "sample": len(y)
    }


def main(filename):
    # in-house data for training
    df_all = pd.read_excel(filename)
    # print('filename: ', filename)

    # Reference
    REF = "value over benchmark" # example: Expression over benchmark, the columns name of label
    # df_all.dropna(subset=[REF], inplace=True)

    all_features = ['put', 'features', 'here',
                    ]

    # best_scores = {"acc":0, "f1":0}
    # best_scores = {"acc":0, "f1":0, "auc":0}
    # best_scores = {"acc":0, "auc":0}
    # best_scores = {"acc":0}
    # best_scores = {"auc":0}
    # best_scores = {"precision":0}
    best_scores = {"f1": 0}

    best_features = None

    for n in range(len(all_features), 2, -1):
        for features in itertools.combinations(all_features, n):
            features = list(features)

            # remove lipids containing NaN features and LABEL
            df_all = df_all[~df_all[features + ['label']].isna().any(axis=1)]
            df_all.reset_index(drop=True, inplace=True)

            X = np.array(df_all[features])
            y = np.array(df_all['label'].tolist())

            clf = RandomForestClassifier(random_state=0)
            clf.fit(X, y)

            perform_df = pd.DataFrame(
                cross_validation(clf, X, y, df_all[REF])
            ).T
            perform_df["Mean"] = perform_df.mean(axis=1)

            # print(perform_df)

            flag = True
            temp_d = {}
            for metric in best_scores:
                current_score = perform_df.loc[metric, "Mean"]
                temp_d[metric] = current_score
                if current_score <= best_scores[metric]:
                    flag = False
                    break

            if flag:
                print("\n\n####################\n", features, temp_d, "########################\n")
                print(filename)
                best_scores.update(temp_d)
                best_features = features[:]
                print("\nsample:", len(y))
                print("\npos ratio:", np.mean(y))
                print("\nSelect features on inhouse-CV10: F1")
                print("LABEL = ", REF)
                print("\nCurrent features: ", best_features)
                print("\n")
                print(perform_df)
                print("\nDiscarded features: ", set(all_features) - set(best_features))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch process feature selection for model")
    parser.add_argument("--filename", type=str, help="name of the input file of a dataset")
    args = parser.parse_args()
    filename = args.filename
    main(filename)
