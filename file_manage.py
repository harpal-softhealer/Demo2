import pandas as pd
from Mobiles import Mobile


mobile = Mobile()

info = mobile.add_mobile_item()

df = pd.read_csv("example.csv")

df = df.append(info, ignore_index=True)