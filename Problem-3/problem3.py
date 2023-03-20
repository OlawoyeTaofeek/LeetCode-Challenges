from codecs import lookup_error


lookup = {}

target = 9
nums = [2, 7, 9, 11]
for cnt, num in enumerate(nums):
    print(cnt, num)
    if target - num in lookup:
        print(lookup)