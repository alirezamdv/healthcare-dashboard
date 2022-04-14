import numpy as np
from imblearn.over_sampling.base import BaseOverSampler

class CustomPreprocess(BaseOverSampler):
    def __init__(self, addX,addY,*, sampling_strategy="auto", random_state=None):
        super().__init__(sampling_strategy=sampling_strategy)
        self.addX=addX
        self.addY=addY
        self.random_state = random_state

    def _check_X_y(self, X, y):
        return X, y, None

    def _fit_resample(self, X, y):
        ids = X.reset_index().id.values
        add = self.addX.reset_index()
        add = add[add['id'].isin(ids)]
        add = add.set_index(['id','day'])
        
        y=pd.Series(y)
        X = np.concatenate((X, add), axis=0) 
        y=y.append(self.addY[self.addY['id'].isin(ids)]['dengue_dx'])
        return (
            X,y
        )