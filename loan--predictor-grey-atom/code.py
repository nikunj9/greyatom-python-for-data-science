# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
bank=pd.DataFrame(bank_data)
#Code starts here
categorical_var = bank.select_dtypes(include = 'object')
#print(categorical_var.shape)
numerical_var= bank.select_dtypes(include = 'number')
#print(numerical_var.shape)


#-------------------------------------------
banks = bank.drop(columns=['Loan_ID'])
bank_mode = banks.mode()
#print(bank_mode)
banks = banks.fillna(bank_mode.iloc[0])
#print(banks.isnull().sum().values.sum())
#print(banks.shape)

#--------------------------------------------
avg_loan_amount=pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc='mean')
#print(avg_loan_amount)

#--------------------------------------------
loan_approved_se=banks[(banks['Self_Employed']== "Yes") & (banks['Loan_Status'] == "Y")]
loan_approved_nse=banks[(banks['Self_Employed']== "No") & (banks['Loan_Status'] == "Y")]
percentage_se=(len(loan_approved_se)/614)*100
#print(percentage_se)
percentage_nse = (len(loan_approved_nse) / 614) * 100
#print(percentage_nse)


#--------------------------------------------

loan_term=banks['Loan_Amount_Term'].apply( lambda x: int(x)/12)
big_loan_term=len(loan_term[loan_term>=25])
print(big_loan_term)
#--------------------------------------------
columns_to_show = ['ApplicantIncome', 'Credit_History']
loan_groupby = banks.groupby('Loan_Status')[columns_to_show]
mean_values = loan_groupby.agg(np.mean)
print(mean_values)




