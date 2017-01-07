

import pandas as pd

df = pd.DataFrame([{'Name': 'Albert Einstein', 'Area': 'Relativity', 'Born':'Germany'}, 
		   {'Name': 'Lord Kelvin', 'Area': 'Thermodynamics', 'Born': 'Belfast'},
		   {'Name': 'Erwin Schroedinger', 'Area': 'Quantum Mechanics', 'Born': 'Vienna'}],)
 

df

df = pd.DataFrame([{'Name': 'Albert Einstein', 'Area': 'Relativity', 'Born':1879},
                   {'Name': 'Lord Kelvin', 'Area': 'Thermodynamics', 'Born': 1824},
                   {'Name': 'Erwin Schroedinger', 'Area': 'Quantum Mechanics', 'Born': 1887}],
                  index=['Germany', 'Belfast', 'Vienna'])
df

df['Gender']='Male'
 

df

df['Height'] = pd.Series({0: 1.69, 1:1.70, 2:1.75})
 

df


df.drop('Born', axis = 1, inplace = False)

df


import pandas as pd
df = pd.read_csv('census.csv')
df


