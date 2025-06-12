import os
import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    database = 'pos'
)
curs = conn.cursor()

more = True
while more:
    os.system('cls')

    print('POS System')
    print('----------')
    date = input('Transaction Date: ')
    type = input('Type [O/P/S]:     ')
    prod = input('Product id:       ')
    qty  = input('Quantity:         ')
    free = input('Free quantity:    ')
    rate = input('Rate:             ')
    tax  = input('Tax %:            ')
    disc = input('Discount %:       ')

    price = float(rate) * int(qty)
    taxamt = price * float(tax)/100
    discamt = price * float(disc)/100
    amount = price + taxamt - discamt

    buf = "INSERT INTO trn(trn_date,trn_type,prod_id,qty,free,rate,tax,discount,amount) VALUES('"+str(date)+"','S',"+str(prod)+","+str(qty)+","+str(free)+","+str(rate)+","+str(taxamt)+","+str(discamt)+","+str(amount)+")\r\n"
    curs.execute(buf)

    more = input('More [y/n]: ').upper().startswith('Y')
