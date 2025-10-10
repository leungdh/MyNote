Output mol into pdf 导出pdf分子
```py
def save_pdf(df,dir_in,name,n_repr=350):
    if len(df)>n_repr:
        print('select {} to show, origin num of mols: {}'.format(n_repr,len(df)))
        mols = df["Whole.SMILES"].tolist()
        _, representative_lipids, _, _ = kmeans_molecules(mols, n_repr)
        df_showselected = df[df["Whole.SMILES"].isin(representative_lipids)]
    else:
        df_showselected = df

    img = Draw.MolsToGridImage([Chem.MolFromSmiles(smi) for smi in df_showselected["Whole.SMILES"]],
                               returnPNG=False, useSVG=False,
                         maxMols = 2000, molsPerRow= 5, subImgSize = (350, 350),
                         legends = ["MolID: {}, clogP: {:.2f}\n MW: {:.2f}, ApKa.prob: {:.2f}".
                                    format(row["MolID"],row["Whole.clogp"],row["Whole.MW"],row["Whole.apka.prob"])
                                    for index, row in df_showselected.iterrows()])
    display(img)
    img.save(os.path.join(dir_in, name))

```
