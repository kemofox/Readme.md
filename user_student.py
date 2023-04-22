import random
import re
from unit import Unit
from user import User
from user_admin import UserAdmin

class UserStudent(User):

    def __init__(self, user_id=0, user_name="", user_password="", user_role="ST", user_status="enabled", enrolled_units=[]):
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        self.enrolled_units = enrolled_units

    def __str__(self):
        return f"{self.user_id},{self.user_name},{self.user_password},{self.user_role},{self.user_status},{self.enrolled_units}"

    def student_menu(self):
        print("1.list available units")
        print("2.list enrolled units")
        print("3.enroll unit")
        print("4.drop unit")
        print("check unit")
        print("6.generate score")
    
    def list_available_units(self):
        print("available units are :")
        with open("data/unit.txt", "r", encoding="utf-8") as file:
            for line in file:
                information = line.strip().split(",")
                if information[3] != "0":
                    print(information)

    def list_enrolled_units(self):
        
        if not self.enrolled_units:
            print("you do not enroll any units")
            return
        
        print("these are enrolled unit(s)")
        for unit_information in self.enrolled_units:
            print(unit_information)

    def enrol_unit(self,unit_code):
        unit_information = self.enrolled_units
        print(unit_information)
        print(type(unit_information))
        if len(unit_information) > 2:
            print("you have enrolled 3 units which reach maximun capacity")
            return

        if unit_code in (each_unit_information[0] for each_unit_information in unit_information):
            print("you have enrolled this unit ")
            return
        
        with open("data/unit.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        with open("data/unit.txt", "w", encoding="utf-8") as file:   
            for each_line in lines:
                information = each_line.strip().split(",")
                # print(type(information[3])) str
                if information[1] == unit_code and int(information[3]) > 0:
                    self.enrolled_units.append((unit_code,-1))
                    # unit_list = list(self.enrolled_units)
                    # unit_list.append((unit_code, -1))
                    # self.enrolled_units = tuple(unit_list)
                    print(self.enrolled_units)

                    information[3] = str(int(information[3])-1)
                    file.write(f"{information[0]},{information[1]},{information[2]},{information[3]}"+"\n")
                elif information[1] == unit_code and int(information[3]) == 0:
                    print("this unit is full")
                    file.write(each_line)
                else:
                    file.write(each_line)

        with open("data/user.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        with open("data/user.txt", "w", encoding="utf-8") as file:
            for each_line in lines:
                information = each_line.strip().split(",")
                if information[0] == str(self.user_id):
                    print(str(self))
                    file.write(str(self) + "\n")
                else:
                    file.write(each_line)
        
    def drop_unit(self,unit_code):
        unit_information = self.enrolled_units
        
        state = False
        for each_unit in unit_information:
            if each_unit[0]==unit_code:
                state = True
        
        if state:
            self.enrolled_units = [each_unit for each_unit in self.enrolled_units if each_unit[0] != unit_code]
            with open("data/user.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
            with open("data/user.txt", "w", encoding="utf-8") as file:
                for each_line in lines:
                    information = each_line.strip().split(",")
                    if information[0] == str(self.user_id):
                        file.write(str(self) + "\n")
                    else:
                        file.write(each_line)  

            with open("data/unit.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
            with open("data/unit.txt", "w", encoding="utf-8") as file:
                for each_line in lines:
                    information = each_line.strip().split(",") 
                    if information[1] == unit_code:
                        information[3] = str(int(information[3])+1)
                        file.write(f"{information[0]},{information[1]},{information[2]},{information[3]}"+"\n")
                    else:
                        file.write(each_line)
        else:
            print("you don enroll this unit")

    def check_score(self,unit_code = None):
        if not unit_code:
            print("here are scores for each unit ")
            for unit in self.enrolled_units:
                print(f"UNiT {unit[0]}'s score is {unit[1]}")
        else:
            for unit in self.enrolled_units:
                if unit[0] == unit_code:
                    print(f"UNiT {unit[0]}'s score is {unit[1]}")
                    return
                
            print(f"you do not have this unit {unit_code}")

    def generate_score(self,unit_code):
        unit_information = self.enrolled_units
        is_generate = False
        # print(unit_information)
        for index,each_unit_information in enumerate(unit_information):
            if each_unit_information[0] == unit_code:
                score = random.randint(0,100)
                unit_information[index] = (unit_code,score)
                is_generate = True
                print(f"the unit {each_unit_information[0]}'s score is {score}")
        if not is_generate:
            print("you type a worong unit code")
            return

        self.enrolled_units = unit_information


        with open("data/user.txt","r",encoding="utf-8") as file:
            lines = file.readlines()
        with open("data/user.txt","w",encoding="utf-8") as file:
            for each_line in lines:
                information = each_line.strip().split(",")
                # print(type(information[0]))
                if information[0] == str(self.user_id):
                    file.write(str(self) + "\n")
                else:
                    file.write(each_line)

    


#test
# ad1=UserAdmin(123,"dasda","1111")
# student1=UserStudent(1111,"std","asd","ST","enabled")
# # print(type(student1.enrolled_units))
# print(str(student1))
# student1.enrolled_units=[("FIT9136",50)]
# student1.list_available_units()
# student1.list_enrolled_units()
# # ad1.add_user(student1)
# # print(len(student1.enrolled_units))
# student1.enrol_unit("FIT9132") 
# student1.drop_unit("FIT9136")
# student1.check_score("")
# student1.generate_score("FIT9132")
# print(student1.enrolled_units)
# print(type(student1.enrolled_units))
# print(str(student1))




# with open("data/user.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
# # with open("data/user.txt", "w", encoding="utf-8") as file:
#     for each_line in lines:
#         information =each_line.strip().split(",")
#         if information[3] =="ST":
#             print(information[0:5])
#             match = re.search(r'\[.*\]', each_line)
#             if match:
#                 content_inside_brackets = match.group(0)
#                 print(content_inside_brackets)
#                 print(type(content_inside_brackets))
#                 unitsinfor=eval(content_inside_brackets)
#                 print(type(unitsinfor))
#                 print(type(unitsinfor[0]))

#             else:
#                 print("No brackets found.")
#             # enrolled_units=eval(enrolled_units_str)
#             # print(enrolled_units)
#             # print(type(enrolled_units))

