# nesteed disctionary

marks= {}

x = int(input("Enter the marks of physics :"))
marks.update ({"physics" : x})

x = int(input("Enter the marks of Chemistry :"))
marks.update({"chemistry": x} )

x= int(input("Enter the marks of Math :"))
marks.update({"math": x })

print(marks)