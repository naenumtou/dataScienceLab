
import pandas as pd

# Data input
data = {
        'Date': ['04-Feb-18', '10-Mar-18', '14-Jan-18',
                 '18-Jan-18', '13-Mar-18', '31-Mar-18'],
        'Name': ['A', 'A', 'B', 'B', 'B', 'B'],
        'Amount': [120, -230, 500, -250, -170, 80]
        }

# Create dataframe
savingAccount = pd.DataFrame(data)

# Create output
months = pd.date_range(start = '30/09/2017',
                       end = '31/05/2018',
                       freq = 'M')

# Create dataframe
remainingBalance = pd.DataFrame({'Month': months})

# Convert date time format
savingAccount['Date'] = pd.to_datetime(savingAccount['Date'])
savingAccount['Date'] = savingAccount['Date'].dt.strftime('%b-%y')

remainingBalance['Month'] = remainingBalance['Month'].dt.strftime('%b-%y')

# Aggregate table
savingAccount = savingAccount.groupby(['Name', 'Date'], as_index = False)['Amount'].sum()
savingAccount = savingAccount.rename(columns = {'Name': 'contractID',
                                                'Date': 'Month',
                                                'Amount': 'Outstanding'})

# Mapping with output table
outputBalance = []

for cusID in savingAccount['contractID'].unique():
    saving = savingAccount[savingAccount['contractID'] == cusID]
    balance = pd.merge(remainingBalance, saving[['contractID', 'Month', 'Outstanding']],
                       how = 'left',
                       left_on = ['Month'],
                       right_on = ['Month'])
    balance['contractID'] = balance['contractID'].fillna(cusID)
    balance['Outstanding'] = balance['Outstanding'].fillna(0)
    balance['Outstanding'] = balance['Outstanding'].cumsum()

    outputBalance.append(balance)
    
outputBalance = pd.concat(outputBalance, axis = 0)
