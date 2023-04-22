# import os
import random

class Unit:
    def __init__(self, unit_id=0, unit_code="", unit_name="", unit_capacity=0):
        self.unit_id = unit_id
        self.unit_code = unit_code
        self.unit_name = unit_name
        self.unit_capacity = unit_capacity

    def __str__(self):
        return f"{self.unit_id},{self.unit_code},{self.unit_name},{self.unit_capacity}"

    def generate_unit_id(self):
        return random.randint(1000000, 9999999)
		#事实上我想给它改成从1000001开始 往后顺延


# test
#unit1= Unit("",unit_code="FIT9136")
#unit1.unit_id = Unit.generate_unit_id(unit1)
#unit2 = Unit(12,"asdasd","asd",4)
#print(unit1.unit_id)
#print(str(unit1))
#print(str(unit2))
# import os
# import random


