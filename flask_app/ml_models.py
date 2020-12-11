'''Module for ML algorithm'''

import pandas as pd
import numpy as np
from joblib import load

df = pd.read_csv('./data/working_ratings.csv', index_col=0)
nmf = load('./models/nmf.joblib')

def simple_recommender():
    pass

def nmf_recommender(user_input, rating_data=df, model=nmf, n_movies:int =5):
    user = pd.DataFrame(user_input, columns=rating_data.columns, index=[rating_data.shape[0]+1])
    user = user.fillna(user.mean().mean())
    user_P = model.transform(user)
    user_R = pd.DataFrame(np.dot(user_P, nmf.components_), columns=rating_data.columns, index = [0])
    recommendations = user_R.drop(columns=user_input.keys())
    recommendations = recommendations.T.sort_values(by=0, ascending=False).head(n_movies)
    return recommendations

def cosim_recommender():
    pass

if __name__ == '__main__':
    input = {"Toy Story": 3, "Pulp Fiction": 5, "Forrest Gump": 4}
    print(nmf_recommender(input))