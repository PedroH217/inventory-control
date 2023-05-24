import time

class DB:
    def __init__(self):
        self.bd = dict()


    def insert_bd(self, product=None, price=None, amount=None):
        
        # Checking if the data already exists, if it exists amount will be
        # incremented, otherwise new data will be created...
        if product:
            if product in self.bd:
                self.bd[product][1] += amount
            else:
                self.bd[product] = [price, amount, False]

        return f"Inserted Product {product} | {price} | {amount}"


    def withdraw_bd(self, item='', var=False):      
        
        for k in self.bd.keys():
            
            if k == item:
                print(f'\nThe item {k} WAS found !\n')
                time.sleep(1.5)
                self.bd.pop(k, None)
                print(f'\nThe item {k} has been successfully removed!\n')
                
                return None
        
        print(f'\nThe product {item} NOT found in stock')


    def search_bd(self, item):
        for k in self.bd.keys():

            if k == item:
                print(f'\nThe product {k} WAS found in the stock\n')
                time.sleep(1.5)
                
                return None
        
        print(f'\nThe product {item} NOT found in the stock !')


    def list_bd(self):
        for k, v in self.bd.items():
            print(f'Product : {k} | Price : {v}')

        print()
        

database_obj = DB()