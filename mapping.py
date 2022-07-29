import pandas as pd

df = pd.read_csv('career_pred.csv')
df = df.drop('Salary Range Expected',axis = 'columns')
df = df.dropna()

#separating dependent and independent variable
inputs = df.iloc[:,:37]
for col in inputs.select_dtypes(include=['object']).columns:
  inputs[col]=inputs[col].astype('category')
  inputs[col]=inputs[col].cat.codes

#dependent variable
targets = df.iloc[:,37:]
targets['job_n']=targets['Suggested Job Role'].astype('category')
targets['job_n']=targets['job_n'].cat.codes

#creating separate dataframes to map codes to actual objects for each object attribute

#Suggested Job Role
job_role = pd.DataFrame({'job':targets['Suggested Job Role'].unique(),'job_n':targets['job_n'].unique()})

#certifications
cert = df['certifications'].unique()
cert_n = inputs['certifications'].unique()
certifications = pd.DataFrame({'cert':cert,'cert_n':cert_n})

#workshops
workshops = pd.DataFrame({'workshops':df['workshops'].unique(),'workshops_n':inputs['workshops'].unique()})

#reading and writing skill
read_write = pd.DataFrame({'read_write':df['reading and writing skills'].unique(),'read_write_n':inputs['reading and writing skills'].unique()})

#memory skills
memory = pd.DataFrame({'memory':df['memory capability score'].unique(),'memory_n':inputs['memory capability score'].unique()})

#books interested
books = pd.DataFrame({'books':df['Interested Type of Books'].unique(),'books_n':inputs['Interested Type of Books'].unique()})

#type of company
company = pd.DataFrame({'company':df['Type of company want to settle in?'].unique(),'company_n':inputs['Type of company want to settle in?'].unique()})

#interested career area
interested_career = pd.DataFrame({'career':df['interested career area '].unique(),'career_n':inputs['interested career area '].unique()})

#interested subjects
interested_sub = pd.DataFrame({'sub':df['Interested subjects'].unique(),'sub_n':inputs['Interested subjects'].unique()})


