
import pandas as pd

data = pd.read_csv('test1.csv')
data["Date"] = pd.to_datetime(data["Date"]).dt.strftime("%d-%m-%Y")
df = pd.DataFrame(data)
print (df)

now = pd.to_datetime('today').strftime("%d-%m-%Y")
print(now)
print(df[df['Date']==now])


"""
Output:

Date Lecture
0  16-07-2020       A
1  17-07-2020       B
2  19-07-2020       C
19-07-2020
         Date Lecture
2  19-07-2020       C
"""
