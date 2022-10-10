rom = "MMMCD"
subt = ["CD", "CM", "IX", "IV", "XL", "XC"]

n = [subt if True for subt in rom]
print(n)
mm = [x for x in rom if x != "C" and x != "D"]
print(mm)

