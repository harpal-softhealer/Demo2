class Mobile:
    def __init__(self):
        self.information = {
            "Brand name": ["Vivo"],
            "RAM": [8],
            "ROM": [128],
            "Display Size": [6.5],
            "Camera Quality": [12],
            "Price": [100000],
            "Discount": [10]
        }

    def reduce_discount_price(self,price,discount):
        return int(price) - (int(price) * int(discount) / 100)
        
    def add_mobile_item(self):
        self.information["Brand name"] = list(input('Brand Name :'))
        self.information["RAM"] = list(input('RAM :'))
        self.information["ROM"] = list(input('ROM :'))
        self.information["Display Size"] = list(input('Display Size :'))
        self.information["Camera Quality"] = list(input('Camera Quality :'))
        self.information["Price"] = list(input('Price :'))
        self.information["Discount"] = list(input('Discount :'))

        return self.information

mobile_1 = Mobile()

print(type(mobile_1.information["Brand name"]))

print(mobile_1.add_mobile_item())

li = []

li.append(mobile_1.information)

print(li)