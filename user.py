
import random



class User:
	
    def __init__(self, user_id=0, user_name="", user_password="", user_role="" , user_status=""):
        self.user_id = user_id
        self.user_name = user_name
        # self.user_password = user_password
        self.user_password = self.encrypt(user_password)
        self.user_role = user_role
        self.user_status = user_status

    def __str__(self):
        return f"{self.user_id},{self.user_name},{self.user_password},{self.user_role},{self.user_status}"

    def generate_user_id(self):
        return random.randint(10000, 99999)

    def check_username_exist(self, user_name):
        with open("data/user.txt","r",encoding="utf-8") as file:
            for line in file:
                field = line.strip().split(",")
                if field[1] == user_name:
                    return True
        return False

    def encrypt(self, user_password):
        str_1 ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        str_2 = "!#$%&()*+-./:;<=>?@\^_`{|}~"
        encrypted_password = "^^^"
        i=0
        for char in user_password:
            char_acsII = ord(char)
            charAcsII_mod_str1 = char_acsII % len(str_1)
            char_mod_str2 = i % len(str_2)
            encrypted_char = str_1[charAcsII_mod_str1] + str_2[char_mod_str2]
            encrypted_password += encrypted_char
            i +=1
        encrypted_password += "$$$"
        return encrypted_password
    

    def login(self, user_name, user_password):
        with open("data/user.txt","r",encoding="utf-8") as file:
            for line in file:
                field = line.strip().split(",")#在这个里面 是删除末尾的空格 中间的不删除
                if field[1] == user_name and field[2] == self.encrypt(user_password) and field[4] == "enabled":
                    # return self.__str__
                    return line.strip()
        return None


# test
# with open("data/user.txt","r",encoding="utf-8") as file:
#     for line in file:
#         field = line.strip().split(",")
#         print(field,type(field[1]),field[1])
#         print(line)

user1=User(12,"jack")
# a = user1.check_username_exist("jack")
# print(str(user1),a)

b=user1.encrypt("asdfsgdhag")
print(b)

# b1=user1.encrypt("abcd1234")
# print(b1)
# user1.user_password = b1
# print(str(user1))

# c=user1.login("jack","password")
# print(c)
