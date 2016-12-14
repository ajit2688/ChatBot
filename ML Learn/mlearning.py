import pandas as pd
import quandl

df = quandl.get("SI/TDC_SI")
print (df.head())
