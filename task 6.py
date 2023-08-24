from test3 import load_data , update_data
products = load_data()
while True :
    selection = int(input( '1. Add New Product\n2. Print Product Details\n3. Buy Product\n4. Delete\n5. Exit '))

    if selection == 1 :
        product_num = int(input('Enter Product Number : '))
        product_name = input("Enter Product Name : ")
        product_price = int(input("Enter Product Price : "))
        product_qty = int(input("Enter Product Quantity : "))
        product = {
                "id" : product_num,
                "name" : product_name ,
                "price" : product_price,
                "qty" : product_qty
                   }
        products.append(product)
        update_data(product)
        print("Product Added Successfully")
    elif selection == 2 :
        product_num = int(input('Enter Product Number : '))
        for i in products :
            if i ['id'] == product_num :
                print(i)
                break
        else :
            print('products Not Exist')
    elif selection == 3 :
        product_num = int(input('Enter Product Number : '))
        for i in products :
            if i ['id'] == product_num :
                while True :
                    qty = int(input('Enter product qty : '))
                    if qty > i ['qty'] or qty <=0:
                        print('Invalid Qty ')
                    else:
                        break
                i['qty'] = i ['qty'] - qty
                break



        # product_qtyaf = int(input("Enter Product Quantity : "))
        # product_qty = product_qty - product_qtyaf
        # print("Quntity After = " , product_qty)
    elif selection == 4 :
        product_num = int(input('Enter Product Number : '))
        for i in products[:] :
            if i ['id'] == product_num :
                products.remove(i)
        # for i in products :
        #     if i.get("id") == product_num :
        #         products.remove(i)
        #         print("Product Deleted ")
        #         break

    elif selection == 5 :
        exit()
    else :
        print("Invalid Input ")
