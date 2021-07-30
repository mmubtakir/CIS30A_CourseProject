# Name: Musamim Mubtakir
# CIS 30A
# Professor Kasey Nguyen
# CIS 30A Course Project Option A
# receipt_module

fout = open('receipt.txt','a')

tax = 0.0775
def total(customer_list):

    subtotal = 0

    for i in customer_list:
        subtotal += (i[1])

    print(customer_list)
    print('Subtotal: $ {:.2f}' .format(subtotal))

    t_amount = tax*subtotal
    print('Tax: \t $ {:.2f}' .format(t_amount))

    total = subtotal + t_amount
    print('Total: \t $ {:.2f}' .format(total))

    receipt(customer_list,subtotal,total)

def receipt(customer_list,subtotal,total):
    
    fout.write('...You will find your receipt below...\n')
    fout.write('********        RECEIPT       ********\n')
    fout.write('Service                          Price\n')
    fout.write('--------------------------------------\n')

    for i in customer_list:
        fout.write('{}  $ {}\n' .format(i[0],i[1]))

    fout.write('''
-------------------------------------
Subtotal:       $ {}
Tax:            $ {}
Total:          $ {:.2f}
-------------------------------------
Thank you for trusting us with your auto care...
''' .format(subtotal,tax*100,total))

    fout.close()
    print('\n\nYour receipt has been printed in the receipt.txt file')
