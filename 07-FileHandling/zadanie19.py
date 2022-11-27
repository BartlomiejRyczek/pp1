nums=range(1,51)

with open('zadanie19.txt', 'w') as f:
    for i in range(0, len(nums)):
        f.write(str(nums[i])+"\n")