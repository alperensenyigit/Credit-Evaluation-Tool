import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

if os.path.isfile('model-v1.pkl'):

    version = int(''.join(filter(str.isdigit, 'model-v1.pkl')))
    new_version = f"model-v{version + 1}.pkl"
else:
    new_version = 'model-v2.pkl'

data = pd.read_excel('userDatas.xlsx')
X = data[['Income', 'Expense', 'Findex']]
y = data['LoanAmount']

model = LinearRegression()
model.fit(X, y)

with open(new_version, 'wb') as file:
    pickle.dump(model, file)

print("Completed.")
