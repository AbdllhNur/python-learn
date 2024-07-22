def det_bmi(weight, height):
    return weight / height ** 2


weight = float(input("weight in kg : "))
height = float(input("height in m : "))

bmi = det_bmi(weight, height)

print(bmi)