
weight = int(input("Weight in kilograms: "))
height = float(input("Height in meters: "))
x = weight/float(height*height)
if x < 18.5:
    print('Underweight,  with a BMI of', x)
if x>=18.5 and x<25:
    print("Average, with a BMI of", x)
if x >= 25 and x < 30:
   print('Overweight, with a BMI of', x)
if x >= 30:
   print('Obese, with a BMI of', x )