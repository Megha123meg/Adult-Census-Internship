import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV,KFold
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,OrdinalEncoder,StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.preprocessing import StandardScaler
import pickle
import joblib

import warnings

warnings.filterwarnings("ignore")
pd.set_option('display.max_columns',10)
# %matplotlib inline

# specifying client_id and client_secret to connect to cassandra database
client_id ="tyljnJccJsMUJWJZULcWFcwE"
client_secret="d383FAiT+o-b65G0O-+6revb1zjKE6,v7cMQ,Q_AQQMWW_wCKUa7nXlZ4tuMLradeHWHbgur48bx3j7kQgGC27cH_RI_YTL-.iFaqKLboO68hAZyXZutEMsOdBw_XF9C"
token="AstraCS:tyljnJccJsMUJWJZULcWFcwE:4a2d5e3ac085afbba9ae136b7ec042a2805760bc110007905c0c50543b57d560"



from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config = {
    'secure_connect_bundle': 'E:\\Internship\\Adult-Census-Internship\\secure-connect-census-data.zip'
}
auth_provider = PlainTextAuthProvider(client_id,client_secret)

# Create a Cluster with the USE_BETA flag set to True
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

# Set the keyspace using the USE statement
session.execute("USE income_prediction")

# Execute a query in the selected keyspace
query = "SELECT * FROM census"
result = session.execute(query)

df = pd.DataFrame(list(session.execute("SELECT * FROM census")))
df.head()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['salary'] = le.fit_transform(df['salary'])

from sklearn.preprocessing import LabelEncoder
for col in df.columns:
    if df[col].dtypes == 'object':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))

X = df.drop("salary",axis=1)
y = df.salary


ss=StandardScaler()
data=ss.fit_transform(X)
data=pd.DataFrame(data)
joblib.dump(ss, 'standard.pkl')
