#Name: Nafisa Chowdhury
#PSID: 1591144

integers = [int(i) for i in input().split()]

sorted_int = sorted(integers)

for num in sorted_int:
    if num >= 0:
        print(num, end=" ")
