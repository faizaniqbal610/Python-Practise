letter = "Hey my name is {1} and i am from {0}"

name = "Faizan"
country = "Pakistan"

print(letter.format(country, name))

print(f"Hey my name is {name} and i am from {country}")

print(f"we use f-string like this:- Hey my name is {{name}} and i am from {{country}}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.09999))

