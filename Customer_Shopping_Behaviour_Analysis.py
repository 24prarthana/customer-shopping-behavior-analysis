#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

df = pd.read_csv('../data/customer_shopping_behavior.csv')
df.head()


# In[11]:


df.info()


# In[12]:


df.describe()


# In[13]:


df.isnull().sum()


# In[5]:


df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median())) 


# In[15]:


df.isnull().sum()


# In[6]:


df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[22]:


df.columns


# In[7]:


#create a new column age_group
labels=['young adults','adult','middle aged','senior']
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)


# In[24]:


df[['age','age_group']].head(10)


# In[8]:


# create column purchase_frequency_days
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


# In[26]:


df[['purchase_frequency_days', 'frequency_of_purchases']].head(10)


# In[27]:


df=df.drop('promo_code_used',axis=1)


# In[28]:


pip install psycopg2-binary sqlalchemy


# In[29]:


pip install --upgrade pip


# In[9]:


from sqlalchemy import create_engine

# Step 1: Connect to PostgreSQL
# Replace these values with your actual database details
username = "postgres"       # Default PostgreSQL username
password = "109056"  # Password set during installation
host = "localhost"          # If running locally
port = "5432"               # Default PostgreSQL port
database = "customer shopping behavior"  # Database created in pgAdmin

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# Step 2: Load DataFrame into PostgreSQL
table_name = "customer"  # Choose any table name

df.to_sql(
    table_name,
    engine,
    if_exists="replace",
    index=False
)

print(
    f"Data successfully loaded into table '{table_name}' "
    f"in database '{database}'."
)


# In[ ]:




