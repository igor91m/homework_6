#### РєР»Р°СЃСЃ РѕР±СЉРµРєС‚ Р°С‚СЂРёР±СѓС‚ ########
'''
Р°С‚СЂРёР±СѓС‚С‹ РєР»Р°СЃСЃР°
Р°С‚СЂРёР±СѓС‚С‹ РѕР±СЉРµРєС‚Р° (СЌРєР·РµРјРїР»СЏСЂР°) РєР»Р°СЃСЃР°
list.append(x)
'''
'''
class Car:
    """
    ###### РїСѓР±Р»РёС‡РЅС‹Р№, Р·Р°С‰РёС‰РµРЅРЅС‹Р№, РїСЂРёРІР°С‚РЅС‹Р№ (РёРЅРєР°РїСЃСѓР»СЏС†РёСЏ)######
    x - Public
    _x - Protected
    __x - Private
    """
    color = 'red'
    model = 'camry'
    _count = 0

    def print_info(self):
        pass
        # print(self.__form_description())

    # def __form_description(self):
    #     return f"{self.color, self.model}"
    # РЅРёР¶Рµ С‡РµСЂРµР· РјР°РіРёС‡РµСЃРєРёР№ РјРµС‚РѕРґ __str__
    def __str__(self):
        return f"{self.color, self.model}"

    ###### РёРЅРёС†РёР°Р»РёР·Р°С†РёСЏ Рё РјРµС‚РѕРґС‹ #######
    def __init__(self, color, model = None):
        """
        "РјР°РіРёС‡РµСЃРєРёР№ РјРµС‚РѕРґ"
        РєРѕРЅСЃС‚СЂСѓРєС‚РѕСЂ РєР»Р°СЃСЃР° (С‚РѕС‡РЅРѕ С‚Р°РєРѕР№ Р¶Рµ РјРµС‚РѕРґ, СЃРѕР·РґР°РµС‚ РѕР±СЉРµРєС‚С‹ РєР»Р°СЃСЃР°)
        """
        print("Hello, It's me!")
        Car._count += 1
        if model == None:
            self.model = Car.model
        else:
            self.model = model
        self.color = color

    def car_returned(self):
        Car._count -= 1

test1_car = Car('orange', 'audi') #РІС‹Р·РѕРІ __init__
test2_car = Car('black', 'bmw') #red
test3_car = Car('yellow') #red

print(test1_car.color)
# test1_car.color = 'pink'

print(Car.color)
Car.color = 'blue'
test1_car.print_info()
# print(test1_car.__form_description())
test2_car.print_info()
test3_car.print_info()
print("Car:", test2_car)
str_test2_car = str(test2_car)
print("str_test2_car", str_test2_car)
print(Car._count)
test3_car.car_returned()
print(Car._count)
'''
##### РЅР°СЃР»РµРґРѕРІР°РЅРёРµ #######
class Shape:
    def __init__(self, color, param_1, param_2, rectangle_h = None):
        print("I am new shape!")
        self.color = color
        self.param_1 = param_1
        self.param_2 = param_2
        self.rectangle_h = rectangle_h

    def square(self):
        return self.param_1 * self.param_2

class Toy:
    def __init__(self, *args):
        print("I am toy")

    def play_sound(self):
        print("You win!")

class Rectangle(Shape):
    pass

class Triangle(Shape, Toy):
    """
    s = 1/2*h*a
    """
    def square(self):
        return 1/2 * self.param_1 * self.rectangle_h

test_rectangle = Rectangle("white", 10, 20)
print(test_rectangle.square())

test_triangle = Triangle("orange", 30, 2, 7)
print(test_triangle.square())
test_triangle.play_sound()


# class Triangle(Shape):
#     def __init__(self, color, param_1, param_2, triangle_p):
#         super().__init__(color, param_1, param_2)
#         self.triangle_p = triangle_p
#
#     def get_t_p(self):
#         return self.triangle_p
#
# r = Rectangle("white", 10, 20, True)
# print(r.color)
# print(r.square())
# print(r.get_r_p())
# t = Triangle("red", 30, 40, False)
# print(t.color)
# print(t.square())
# print(t.get_t_p())


###### РїРѕР»РёРјРѕСЂС„РёР·Рј Рё РїРµСЂРµРіСЂСѓР·РєР° РјРµС‚РѕРґРѕРІ########

######## РїСЂРёРјРµСЂ РєР»Р°СЃСЃ #########
"""
id РєР°РјРµСЂС‹ (РёР»Рё РїСѓС‚СЊ РґРѕ РІРёРґРµРѕ) 
РєР°Р»РёР±СЂРѕРІРєР° - СѓР±СЂР°С‚СЊ РёСЃРєР°Р¶РµРЅРёРµ Р»РёРЅР·С‹
РѕР±СЂРµР·Р°С‚СЊ РІРёРґРµРѕ 
"""
# from cv2 import imread

class Video:
    def __init__(self, path):
        self.path = path
        # self.video = cv2.imread(path) #РґР»СЏ РєР°СЂС‚РёРЅРєРё

    def calibration(self):
        """
        РїСЂРёРјРЅСЏРµРј РєСѓС‡Сѓ С„РЅРєС†РёР№ Рє self.video
        :return:
        """
        return new_video #РѕР±СЉРµРєС‚ РєР»Р°СЃСЃР°

    def cut_frame(self):
        return new_video #РЅРµ РѕР±СЏР·Р°С‚РµР»СЊРЅРѕ РѕР±СЉРµРєС‚ РєР»Р°СЃСЃР°
        """
        РѕР±СЂРµР·Р°РµРј РєР°РґСЂ
        :return:
        """
    def show_video(self):
        """
        РїРѕРєР°Р·С‹РІР°РµС‚ РІРёРґРµРѕ
        :return:
        """
main_video1 = Video('folder_1')
main_video2 = Video('folder_2')
main_video3 = Video('folder_3')

clean_video = main_video1.calibration()
clean_video = clean_video.cut_frame()

###РїСЂРёРјРµСЂ РЅРµСЃРєРѕР»СЊРєРёС… РјРµС‚РѕРґРѕРІ РїРѕРґСЂСЏРґ
# print(np.array(test_list).add(7).sum())