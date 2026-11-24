#m1
# class Student:
#     def __init__(self,first_name,last_name,age,id,course):
#         self._first_name=first_name
#         self._last_name=last_name
#         self._age=age
#         self._id=id
#         self._course=course
#     def get_full_name(self):
#         return self.first_name,self.last_name
#     def get_age(self):
#         return self.age
#     def get_id(self):
#         return self.age
#     def __str__(self):
#         return f"""Name: {self._first_name}
# Surname: {self._last_name}
# Age: {self._age}
# ID: {self._id}
# Course: {self._course}"""
    
#     def set_age(self,age):
#         if 18<age<30:
#             self._age=age
#         else:
#             print("Nmadur xato")

#     def set_full_name(self,first_name,last_name):
#         if first_name:
#             self._first_name=first_name
#         if last_name:
#             self._last_name=last_name
#     def set_course(self,course):
#         if course<4:
#             self._course+=1
#     def set_id(self,id):
#         if id:
#             self._id=id
# s1=Student("Abbos","Xalimov",18,101,1)
# s1.set_age(22)
# s1.set_full_name("Anvar","Gofurov")
# s1.set_id(101)
# print(s1)








#Masalalar
# class Pharmacy:
#     def __init__(self, pharmacy_name: str, pharmacy_address: str) -> None:
#         self.medicines  = {
#             "trimol": {
#                 "price": 30000,
#                 "quantity": 50
#             }
#         }
#         self.__pharmacy_name = pharmacy_name
#         self.__pharmacy_address = pharmacy_address
#         self.__cash_balance  = 500000
        
        
#     def get_medicines_info(self) -> str:
#         print(f"--- {self.__pharmacy_name} ---")
#         for i in self.medicines:
#             print(f"Drag name: {i} : ${self.medicines[i]['price']} | Quantity: {self.medicines[i]['quantity']}")
            
            
#     def add_medicine(self, medicine: str, price: float, quantity: int) -> None:
#         self.medicines[medicine] = {
#             "price": price,
#             "quantity": quantity
#         }
          
#         print("Dori omborgha muvaffaqiyatli qo'shildi! :)")
        
        
#     def remove_medicine(self, medicine: str) -> None:
        
#         try:
#             self.medicines.pop(medicine)
#             print("Dori muvaffaqiyatli o'chirildi!")
            
#         except:
#             print("Dorini nomini qayta tekshiring")
            
            
#     def sell_medicine(self, medicine: str, quantity: int) -> None:
#             if medicine in self.medicines.keys():
#                 if self.medicines[medicine]["quantity"] > quantity:
#                     print(f"Marhamat sizdan {self.medicines[medicine]["price"]}")
                    
#                 else:
#                     print("Dori yetmas ekan")
#             else:
#                 print("Uzr bizda bunaqa dori yo'q")
            
        
        
        
    
    
# ArzonApteka = Pharmacy("ArzonApteka", "Chilonzor Qatortol MFY")

# ArzonApteka.add_medicine("Bolnol", 12000, 6)
# ArzonApteka.add_medicine("Sitramon", 22000, 16)
# ArzonApteka.get_medicines_info()


# ArzonApteka.remove_medicine("Bolnol")

# ArzonApteka.get_medicines_info()
