import re
from unit import Unit
from user import User
from user_admin import UserAdmin




class UserTeacher(User):
    def __init__(self, user_id=0, user_name="", user_password="", user_status="enabled",teach_unit=[]):
        super().__init__(user_id, user_name, user_password, "TA", user_status)
        self.teach_unit=teach_unit

    def __str__(self):
        str_teach_unit = ','.join(self.teach_unit)
        return super().__str__() + f",{str_teach_unit}"

    def teacher_menu(self):
        print("Teacher Menu:")
        print("1. List Teach Units")
        print("2. Add Teach Unit")
        print("3. Delete Teach Unit")
        print("4. List Enrolled Students")
        print("5. Show Unit Average/Max/Min Score")

    # def list_teach_units(self):
    #     with open("data/user.txt","r",encoding="utf-8") as file:
    #         regex_teach_unit = f"{self.user_id},[^,]+,[^,]+,[^,]+,ebabled,[^,]*{self.user_id}[^,]*$"
    #         regex_teach_unit = f"{self.user_id},*,*,"TA",{[(*,2)]}"
    #         teacher_unit_lines = re.search(regex_teach_unit,file.read(), re.MULTILINE)
    #         print(teacher_unit_lines)
    #         if teacher_unit_lines is None:
    #             print("No unit taught by the teacher is found in database")
    #             return
    #         unit_code = re.findall(r"\d{7}",regex_teach_unit.group(0))
    #         with open ("data/unit.txt","r",encoding="utf-8") as file:
    #             for line in file:
    #                 information = line.strip().split(",")
    #                 if information[0] in unit_code:
    #                     print(information)

    def list_teach_units(self):
        if not self.teach_unit:
            print("No units taught by this teacher are found in the system.")
            return

        print("units taught by this teacher")
        with open("data/unit.txt", "r", encoding="utf-8") as file:
            for line in file:
                information = line.strip().split(",")
                # print(type(information[1]))
                if information[1] in self.teach_unit:
                    print(information)

    def add_teach_unit(self,unit_obj):
        state = True
        with open("data/unit.txt","r",encoding="utf-8") as file:
            lines = file.readlines()
            for each_line in lines:
                information = each_line.strip().split(",")
                if information[1] == unit_obj.unit_code:
                    state = False

        if state:
            with open("data/unit.txt","a",encoding="utf-8") as file:
                file.write(str(unit_obj)+"\n")

        self.teach_unit.append(unit_obj.unit_code)
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


    def delete_teach_unit(self,unit_code):
        if unit_code not in self.teach_unit:
            print("Unit not found in the teach_units list.")
            return

        self.teach_unit.remove(unit_code)
        with open("data/unit.txt","r",encoding="utf-8") as file:
             lines = file.readlines()
        with open("data/unit.txt","w",encoding="utf-8") as file:
            is_deleted = False
            for each_line in lines:
                information = each_line.strip().split(",")
                if information[1] != unit_code:
                    file.write(each_line)
            #     else:
            #         is_deleted = True
            # if is_deleted:
            #     print(f"{unit_code} has been deleted")
            # else:
            #     print(f"{unit_code} not found")
        
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
        
        with open("data/user.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        with open("data/user.txt", "w", encoding="utf-8") as file:
            for each_line in lines:
                information =each_line.strip().split(",")
                if information[3] =="ST":
                    regex_match = re.search(r'\[.*\]', each_line)
                    if regex_match:
                        stu_unit_information = regex_match.group(0)
                        # print(stu_unit_information)
                        # print(type(stu_unit_information))
                        list_stu_unit=eval(stu_unit_information)
                        for unit in list_stu_unit:
                            if unit[0] == unit_code:
                                list_stu_unit.remove(unit)
                        print(list_stu_unit)
                    file.write(f"{information[0]},{information[1]},{information[2]},{information[3]},{information[4]},{list_stu_unit}"+"\n")
                    # else:
                    #     print("No brackets found.")
                else:
                    file.write(each_line)
        # with open("data/user.txt","r",encoding="utf-8") as file:
        #     lines = file.readlines()
        # with open("data/user.txt","w",encoding="utf-8") as file:
        #     for each_line in lines:
        #         information = each_line.strip().split(",")
        #         print(information)
                # if  information[3]=="ST":
                #     print("1")
                #     stu_enrolled_units = information[5]
                #     for index,stu_enrolled_unit in enumerate(stu_enrolled_units):
                #         if stu_enrolled_unit[0] == unit_code:
                #             stu_enrolled_units.remove(stu_enrolled_units[index])
                #             information[5] = stu_enrolled_units
                #             file.write(f"{information[0]},{information[1]},{information[2]},{information[3]},{information[4]},{information[5]}"+"\n")
                #         else:
                #             file.write(each_line)

    def list_enrol_students(self,unit_code):
        state = False
        with open("data/user.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            for each_line in lines:
                information =each_line.strip().split(",")
                if information[3] =="ST":
                    regex_match = re.search(r'\[.*\]', each_line)
                    if regex_match:
                        stu_unit_information = regex_match.group(0)
                        list_stu_unit=eval(stu_unit_information)
                        for unit in list_stu_unit:
                            if unit[0] == unit_code:
                                print(f"student {information[1]} enroll this unit{unit_code}")
                                state = True
        
        if not state:
            print("no one enroll this unit")

    def show_show_unit_avg_max_min_score(self,unit_code):
        unit_score = []
        with open("data/user.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            for each_line in lines:
                information =each_line.strip().split(",")
                if information[3] =="ST":
                    regex_match = re.search(r'\[.*\]', each_line)
                    if regex_match:
                        stu_unit_information = regex_match.group(0)
                        list_stu_unit=eval(stu_unit_information)
                        for unit in list_stu_unit:
                            if unit[0] == unit_code:
                                unit_score.append(unit[1])
        
        print(unit_score)
        if unit_score != []:
            max_value = max(unit_score)
            print("max score is :", max_value)

            # 最小值
            min_value = min(unit_score)
            print("min score is:", min_value)

            # 平均值
            avg_value = sum(unit_score) / len(unit_score)
            print("avger score is:", avg_value)
        else:
            print("no one enroll this unit")
#test
admin1=UserAdmin(123,"dasda","1111")
unit1=Unit(1000005,"FIT9000","something",50)
teacher1 = UserTeacher()
teacher1.user_id = 123455
teacher1.teach_unit = ["FIT9136","FIT9132"]
# print(str(teacher1))


teacher1.add_teach_unit(unit1)
teacher1.list_teach_units()
# teacher1.delete_teach_unit("FIT9136")
# teacher1.delete_teach_unit("FIT9132")
# admin1.add_user(teacher1)
# teacher1.list_teach_units()
# admin1.list_all_unit()
teacher1.list_enrol_students("FIT9136")
teacher1.show_show_unit_avg_max_min_score("FIT9132")

