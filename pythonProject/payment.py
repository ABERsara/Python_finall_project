from datetime import datetime
import random

class Payment:
    """Initializes the credit card data"""

    def __init__(self,creditNumber,threeDigits,validity,IDofCardHolder,secretCod):
        self.creditNumber=creditNumber
        self.treeDigits=threeDigits
        self.validity=validity
        self.IDofCardHolder=IDofCardHolder
        self.secretCod=secretCod

    def payCard(self,cost):
        """Checking the correctness of the credit information received"""
        # check if the credit number length is 16 and it has only numbers
        if len(self.creditNumber) != 16:
            return False
        else:
            for digit in self.creditNumber:
                try:
                    int(digit)
                except ValueError:
                    print("The credit number is not valid")
                    return False
        if len(self.secretCod) != 4:
            return False
        # if self.validity<datetime.today():
        #    return False
        return self.pay(cost)

    def pay(self,cost):
        """Credit transfer: If the credit did not go through (drawn 0) we will return false"""
        num=random.randint(0,10)
        print(num)
        return num>0
