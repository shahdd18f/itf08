def load_data ():
    products = []
    with open('itf08 ', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace('\n', '')
            line = line.split('|')
            product = {
                "id": line[0],
                'name': line[1],
                'price ': line[2],
                'qty': line[3]
            }
            products.append(product)
        print('Data Loaded successfully')
        return products

def update_data(data:list):
    data_str = []
    for item in data :
        item = f"{item.get('id')|item.get('name')|item.get('price')|item.get('qty')}"
        data_str.append(item)

        with open('itf08','w') as file:
            file.writelines(data_str)
            file.close()


