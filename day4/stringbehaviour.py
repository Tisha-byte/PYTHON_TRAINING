#isalpha(),isdigit(),islower(),isupper()
#isalpha()-only checks always alphabet
#isdigit()-checks if digit present in string or not
#title-starting letter will convert in capital
#swapcase-convert small in capital and capital into small
#casefold
#count
x="hello  "
print(x.isalpha())
y="3674"
print(y.isdigit())
print(x.title())
z="Tisha you are great"
print(z.swapcase())
t="HELLO"
y="hello"
print(x==y)
print(t.casefold()==y.casefold())
string="Hello Java and python and Java"
print(string.count("Java"))
print(string.count("Java",8)) #counting after 8th index
print(string.count("Java",8,12)) #range