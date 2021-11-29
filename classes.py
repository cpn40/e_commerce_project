class User:
    def __init__(self, userid, username, pswd, email, phone, shipping, credit_num, billing):
        self.userid = userid
        self.username = username
        self.pswd = pswd
        self.email = email
        self.phone = phone
        self.shipping = shipping
        self.credit_num = credit_num
        self.billing = billing

    def get_userid(self):
        return self.userid

    def get_username(self):
        return self.username


class Books:
    def __init__(self, itemID, name, price, inventory):
        self.itemID = itemID
        self.name = name
        self.price = price
        self.inventory = inventory


class Shirts:
    
    #constructor
    def __init__(self, shirtID, color, price, inventory):
        self.itemID = shirtID
        self.color = color
        self.price = price
        self.inventory = inventory
        
    #destructor
    def __del__(self):
    print("Destroying the Shirts object")
    
    #getters
    def getId(self):
        return self.shirtID
    def getColor(self):
        return self.color
    def getPrice(self):
        return self.price
    def getInventory(self):
        return self.inventory
    
    #setters
    def setId(self, shirtID):
        self.shirtID = shirtID
    def setColor(self, color):
        self.color = color
    def setPrice(self, price):
        self.price = price
    def setInventory(self, inventory):
        self.inventory = inventory
    
    
        
