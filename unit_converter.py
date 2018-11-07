#unit_converter.py
unit_to_meter_dict = {'mm': 1000, 'cm': 100, 'm': 1, 'km': .001, 'in':39.37, 'ft': 3.28, 'yd': 1.09}
while True:
    in_unit = input("What unit will you convert from? >")
    in_num = input("How many? >")
    in_num = int(in_num)
    out_unit = input("What will you convert to? >")
    try:
        out_num = (in_num / unit_to_meter_dict[in_unit]) * unit_to_meter_dict[out_unit]
        print(out_num, out_unit)
        break
    except KeyError:
        print("Bad units!")
