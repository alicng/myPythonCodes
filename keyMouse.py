def KM(table):
    x=round((float(table['Total'][:-1]) / 2) - (float(table['Difference'][:-1])/2),2)
    return {"Total": table['Total'], "Difference": table['Difference'], "Mouse": str(x)+'$'}
    
a=KM({"Total": "1.90$", "Difference": "0.90$", "Mouse": "?"})
print(a)