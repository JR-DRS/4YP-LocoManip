def dropAfterX(df,x):
    return df.drop(df[df['Step']>x].index)
