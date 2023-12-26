# To determine the absolute difference between a given number and
# 123 and if it is greater than 123 then print the triple of the given
# number.

a=eval(input("Enter a number :"))

absolute_dif=abs(a-123)

if absolute_dif> 123:
    result= absolute_dif * 3
    print("The triple of",a, "is", result)
else:
        print("The absolute difference (", absolute_dif, ") is not greater than 123.")