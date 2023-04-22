from user import User
# from unit import Unit

class UserAdmin(User):
    def __init__(self, user_id=0, user_name="", user_password="", user_status="enabled"):
        super().__init__(user_id, user_name, user_password, "AD", user_status)


    def admin_menu(self):
        print("Admin Menu:")
        print("1. Search User")
        print("2. List All Users")
        print("3. List All Units")
        print("4. Enable/Disable User")
        print("5. Add User")
        print("6. Delete User")

    def search_user(self, user_name):
        with open("data/user.txt","r",encoding="utf-8") as file:
            for line in file:
                information = line.strip().split(",")
                if information[1] == user_name:
                    print(information)
                    # break
                    return
            print(f"{user_name} not found")

    def list_all_user(self):
        with open("data/user.txt","r",encoding="utf-8") as file:
            for line in file:
                information = line.strip().split(",")
                print(information)

    def list_all_unit(self):
        with open("data/unit.txt","r",encoding="utf-8") as file:
            for line in file:
                information = line.strip().split(",")
                print(information)

    def enable_disable_user(self,user_name):
        with open("data/user.txt","r",encoding="utf-8") as file:
            datas = file.readlines()
        with open("data/user.txt","w",encoding="utf-8") as file:
            for each_line in datas:
                information = each_line.strip().split(",")
                if information[1] == user_name:
                    if information[4] == "enabled":
                        information[4] = "disabled"
                        print(f"change user {user_name} status to disabled")
                    else:
                        information[4] = "enabled"
                        print(f"change user {user_name} status to enabled")
                file.write(",".join(information) + "\n")

    def add_user(self,user_obj):
        with open("data/user.txt","a",encoding="utf-8") as file:
            file.write(str(user_obj) + "\n")

    def delete_user(self, user_name):
        with open("data/user.txt","r",encoding="utf-8") as file:
            datas = file.readlines()
        with open("data/user.txt","w",encoding="utf-8") as file:
            is_deleted = False
            for each_line in datas:
                information = each_line.strip().split(",")
                print(information)
                if information[1] != user_name:
                    file.write(each_line)
                else:
                    is_deleted = True
            if is_deleted:
                print(f"{user_name} has been deleted")
            else:
                print(f"{user_name} not found")


#test
# admin1=UserAdmin(123,"dasda","1111")
# admin1.add_user(admin1)
# print(str(admin1))
# admin1.search_user("jack")
# admin1.list_all_unit()
# admin1.enable_disable_user("jack")

# admin1.list_all_user()
# admin1.delete_user("dasda")
# admin1.list_all_user()