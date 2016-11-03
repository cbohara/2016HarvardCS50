print("s: ", end="")
lower_case = input()
if lower_case == None:
    exit(1)

upper_case = lower_case.capitalize()

print("raw input: " + str(lower_case))
print("capitalize: " + str(upper_case))

exit(0)
