#str = company_details

str = ('lifestyla International P Ltd.' "\n" 'Max Retail division' "\n" '1st floor, City Centre Mall' "\n"'Banjara Hills, Hyd - 500034' "\n" 'TELANAGANA')

#str1 = customer_details

str1 = ('Name: Raviteja R' "\n" 'Mobile: 7675025059')
print(str, "\n" '--------------------------',"\n", str1)

print('ITEM/HSN/Desc  100007248393')
MRP = int(299.00) 
QTY = int(1)
print('MRP     ',MRP)
print('QTY     ',QTY,"\n")
Total = MRP*QTY
print('Total AMt        ',format(Total, '.2f'))
print('Total Rounded    ',format(Total, '.2f'))
print('Rounded of amt    0.00')

cash = int(500)
Total_tender = int(500)
change_due = cash-MRP
print('Cash = ',cash)
print('Total Tender     ',Total_tender)
print('Change Due       ',change_due,"\n" '------------------------')

a="Tax Details"
print(a.center(20))

gst = float(2.5) 
cgst = ((gst/100)*MRP)
sgst = ((gst/100)*MRP)
print('A CGST _           ',format(cgst, '.2f'))
print('B SGST _           ',format(cgst, '.2f'))
total = cgst+sgst
print('                  --------',"\n" 'Total Tax Value   ',format(total, '.2f'))
print('Total svaings       0.00')










 
