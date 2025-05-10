### Loops: for, while

nums = [1, 2, 3, 4, 5]
print(3 in nums) # True

for num in nums:
    print(num)


fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits):
    print(idx, fruit)


for i in range(5):
    print(i)


# while loop
print("While loop:")
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1