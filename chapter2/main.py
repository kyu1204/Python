# if (a == 10) {
#
# }

a = None

if a is None:
    print("a is None")


if a is None:
    print("second a is None")
elif a is not None:
    print("a is None")
else:
    print("a is not None")

while True:
    print("Infinity loop")
    break

# for (int i = 0; i < 10; i++) {
#
# }

for i in range(10):
    print(i)

a = [1, 2, 3, 4, 5]

arr = [1, 2, "3", "4", 5.5, "Hello World", True, False, None]

a.append(6)

a.insert(1, 1.5)


print(f"a is {a}")
print(f"arr is {arr}")

print(a[0])

# for (int i=0; i < 5; i++) {
#     print(a[i])
# }

for aaaaaaaaaaaaaaa in arr:
    print(aaaaaaaaaaaaaaa)

a = [[1, 2, 3], [4, 5, 6]]
