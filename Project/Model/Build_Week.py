#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import datetime
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
# extra imports

train = pd.read_csv('train_BW.csv')
test = pd.read_csv('test_BW.csv')

date_time = ['deadline', 'state_changed_at', 'created_at', 'launched_at']
for i in date_time:
    train[i] = train[i].apply(
        lambda x: datetime.datetime.fromtimestamp(
            int(x)
            )
        .strftime('%Y-%m-%d %H:%M:%S')
        )

def Duration(d):
    launch = datetime.datetime.strptime(d[0], '%Y-%m-%d %H:%M:%S')
    deadline = datetime.datetime.strptime(d[1], '%Y-%m-%d %H:%M:%S')
    duration = deadline-launch
    weekDifference = int(duration.total_seconds()/(3600*24*7))
    return weekDifference
train['duration'] = train[['launched_at', 'deadline']].apply(
    lambda d: Duration(d), axis=1)

train['keywordsLen'] = train['keywords'].str.len()
train['descLen'] = train['desc'].str.len()
train['NameLen'] = train['name'].str.len()
train['log_goal'] = np.log10(train['goal'])
train.loc[train['duration'] <= 4, 'duration_less_31_days'] = 'True'
train.loc[train['duration'] > 4, 'duration_less_31_days'] = 'False' 


my_features = ['NameLen', 'keywordsLen','descLen','backers_count','country','currency','duration','log_goal']

dtrain= train[my_features].copy()
y = train.final_status
df_train = dtrain
# Select categorical columns with relatively low cardinality (convenient but arbitrary)
X_train, X_valid, y_train, y_valid = train_test_split(train, y, test_size=0.2, random_state=0)
categorical_cols = [cname for cname in df_train.columns if
                    df_train[cname].nunique() < 10 and 
                    df_train[cname].dtype == "object"]

# Select numerical columns
numerical_cols = [cname for cname in df_train.columns if 
                df_train[cname].dtype in ['int64', 'float64']]

# Preprocessing for numerical data
numerical_transformer = SimpleImputer(strategy='mean')

# Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse=False))
])

#Feature Scaling
sc = StandardScaler()

# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

Results = pd.DataFrame({'Model': [], 'Accuracy Score': []})

model_xgb = XGBClassifier(n_estimators= 200, learning_rate = 0.1, max_depth=2, min_child_weight = 1,nthread=4, seed=27,subsample=0.8,colsample_bytree=0.9,max_delta_step=0,
                         objective= 'multi:softmax',gamma = 0,reg_alpha=0.001,reg_lambda=0.5, eval_metric='auc',random_state=0, num_class= 6)
# Bundle preprocessing and modeling code in a pipeline
xgb = Pipeline(steps=[('preprocessor', preprocessor),
                      ('model_xgb', model_xgb)
])

# Preprocessing of training data, fit model 
xgb.fit(X_train, y_train)

# Preprocessing of validation data, get predictions
predictions = xgb.predict(X_valid)
print('Accuracy:', accuracy_score(y_valid, predictions))
print('CR:', classification_report(y_valid, predictions))
print('CM:',confusion_matrix(y_valid, predictions))

res = pd.DataFrame({'Model': ['XGB'],
                    'Accuracy Score': [accuracy_score(y_valid, predictions)]})
Results = Results.append(res)


# In[14]:





# In[12]:





# In[ ]:




