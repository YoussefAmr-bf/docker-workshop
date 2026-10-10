import sys
import pandas as pd

print('arguments:', sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2, 3], "passenger": [4, 5, 6]})
df['month'] = month

df.to_parquet(f"data_{month}.parquet", index=False)
print('Hello from pipeline.py!')
print(f'Month: {month}')
print(df)