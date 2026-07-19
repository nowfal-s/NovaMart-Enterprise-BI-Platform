import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import zipfile
import os

np.random.seed(42)
random.seed(42)

outdir="/mnt/data/TechNova_Raw_Datasets"
os.makedirs(outdir, exist_ok=True)

# Region
regions=['North America','Europe','Asia Pacific','Latin America']
dirty_na=['North America','NorthAmerica','N America','North Am.','north america','  North America ']
region_data=[]
for i in range(1,21):
    base=random.choice(regions)
    if base=="North America":
        reg=random.choice(dirty_na)
    else:
        reg=base if random.random()>0.1 else ""
    region_data.append({"Region_ID":i,"Region_Name":reg,"Country":f"Country_{i}"})
df_region=pd.DataFrame(region_data)
df_region.to_csv(f"{outdir}/Raw_Dim_Region.csv",index=False)

# Product
cats=['Electronics','Furniture','Office Supplies','Invalid_Cat','  electronics']
product_data=[]
for i in range(1,501):
    cost=round(random.uniform(10,500),2)
    price=round(cost*random.uniform(1.2,2.5),2)
    product_data.append({
        "Product_ID":f"PROD-{i:04d}",
        "Product_Name":f"Product {i}"+(" "*random.randint(0,3)),
        "Category":random.choice(cats),
        "Standard_Cost":cost,
        "List_Price":price
    })
df_product=pd.DataFrame(product_data)
df_product.loc[10,"Product_ID"]=np.nan
df_product=pd.concat([df_product,df_product.iloc[[5]]],ignore_index=True)
df_product.to_csv(f"{outdir}/Raw_Dim_Product.csv",index=False)

# Customer
cust=[]
for i in range(1,5001):
    cust.append({
        "Customer_ID":f"CUST-{i:05d}" if random.random()>0.02 else np.nan,
        "Customer_Name":f"Customer {i}",
        "Region_ID":random.randint(1,20)
    })
df_customer=pd.DataFrame(cust)
df_customer.to_csv(f"{outdir}/Raw_Dim_Customer.csv",index=False)

# Fact
num=85000
start=datetime(2023,1,1)
sales=[]
for i in range(num):
    od=start+timedelta(days=random.randint(0,1000))
    qty=random.randint(-5,20)
    if qty==0: qty=1
    disc=round(random.uniform(0,0.3),2) if random.random()>0.05 else np.nan
    sales.append({
        "Invoice_ID":f"INV-{100000+i}",
        "Order_Date":od.strftime("%Y-%m-%d") if random.random()>0.01 else "",
        "Customer_ID":f"CUST-{random.randint(1,5000):05d}",
        "Product_ID":f"PROD-{random.randint(1,500):04d}",
        "Quantity":qty,
        "Discount_Percent":disc,
        "Payment_Method":random.choice(["Credit Card","PayPal","Wire","Cash","cc","paypal "])
    })
df_sales=pd.DataFrame(sales)
df_sales=pd.concat([df_sales,df_sales.sample(n=150,random_state=42)],ignore_index=True)
df_sales=df_sales.sample(frac=1,random_state=42).reset_index(drop=True)
df_sales.to_csv(f"{outdir}/Raw_Fact_Sales.csv",index=False)

zip_path="/mnt/data/TechNova_Raw_Datasets.zip"
with zipfile.ZipFile(zip_path,"w",zipfile.ZIP_DEFLATED) as z:
    for fn in os.listdir(outdir):
        z.write(os.path.join(outdir,fn),arcname=fn)

print(df_region.shape,df_product.shape,df_customer.shape,df_sales.shape)