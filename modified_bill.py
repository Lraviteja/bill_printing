str= ('BILL') #Bill_title

#center_is_used_for_keep_the_titile_in_cnter
print(str.center(30),'\n','GONGURA') #gongura_shop_name

#adress_of_shop
adress = ('3rd floor,GVK One Mall Sri Venkateshwarw Associates,HYD,TELANAGAN.')

#Shop_gst_num
gst = "36ACRFS3362E1ZV"
print('GSTIN :',gst)

billno = "40511"
date = "02-03-2019"
time = "03:45"
print(f'BIILNo :{billno}\nDATE :{date}    Time :{time}','\n','_____________________________________')

mrp = 209.5253555 #iten_prce
qty = 1 #item_quantity
amnt = float(mrp*qty)
print('ITEM NAME\tQTY\tRATE\tAmount','\n','_____________________________________') #printing_label_names
print('''Goungura spl
non-veg thaali''','\t',qty,'  ','{:05.2f}'.format(mrp),'  ','{:05.2f}'.format(amnt),'\n''_______________________________________') #'''  '''_forms_new_line,\t_defines_tab_spaces
print('TOTAL    :\t\t\t','{:05.2f}'.format(amnt)) #'{:05.2f}'.format()_is_used_to_control_float_value
gst = float(2.50)
GST =((gst/100)*amnt) #calculating_gst_by_using_/_*
Gst = float(format(GST,'.2f'))
net = format(Gst+amnt+Gst,'.2f') #format(value,'.2f')_is_used_print_only_2_digits_after_point
print(f'CGST(2.50%) : \t\t\t{Gst}\nSGST(2.50%) : \t\t\t{Gst}\t\t\t\t\nNET AMOUNT :\t{net}')


