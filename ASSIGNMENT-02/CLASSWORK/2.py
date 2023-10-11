def BURGER(name, location = "Mohakhali"):
    burger_dic = {"BBQ Chicken Cheese Burger":250, "Beef Burger":170, "Naga Drums":200}
    if name in burger_dic:
        if location == "Mohakhali":
            print(burger_dic[name]+40+(burger_dic[name]*0.08))
        else:
            print(burger_dic[name]+60+(burger_dic[name]*0.08))
BURGER(input(), "Dhanmondi")


