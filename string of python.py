# string is defen
str1 = "hassan is good student."
print(str1)
len1 = len(str1)  # first string langht
print(len1)
str2 = "abbattabat univ"
len2 = len(str2)  # first string langht
print(len2)
str3 = "khan"
len3 = len(str3)  # first string langht
print(len3)
final = str3+str2 + " " + str1  # final string

print(len(final))
str4 = "hassan"  # sting using indix for the string
str0 = str4[0:-5]
s = str1[6:-6]  # sting 1 using indix for the string
st = str3[0:-1]  # sting 3 using indix for the string
print(s)
str2[0:-1]  # sting 2 using indix for the string
print(str2)
# slicing
str5 = "my name is hassan I from kohat"
str01 = str5[3:12]
print(str01)

# or
str6 = "apna collage "
print(str6[5:len(str6)])
str7 = "my name is hassan I from kohat"
print(str7[:len(str7)])

str6 = "apna collage "
print(str6[-4:-1])

str1 = "hassan"
print(str1.upper())
s = "TOUFFEQ"
print(s.lower())
print(s[0:-6])
print(s[-1:])

str10 = "my name is hassan toufeeq"  # endwith function
print(str10.endswith("eeq"))
str10 = str10.capitalize()
print(str10)

print(str10.capitalize())  # capitalize function

# replace function than the coplite word will be change
print(str10.replace("a", "o"))

# find the word and letteter of stance and also find the indix of str
print(str10.find("o"))

#count the word or latter how many time use in string
print(str10.count("e"))
# prictase qustion in srting
str11 = input("enter your string")
print(len(str11))
# 2nd qustion
str12 = "the $ of the $ is $"
print(str12.count("$"))


def to_check():
    str14 = "madam"
    print(str14)
    return str14


to_check()


def remove_duplicate():
    duplicate = "hhhasssan"
    print(duplicate[0:])
    return duplicate


remove_duplicate()
