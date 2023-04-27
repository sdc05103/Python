# 리스트(lists)

mbti = ['INFP', 'ENFP', 'ISTJ', 'ESTP']

print(mbti)
print(mbti[0])

mbti[0] = 'INFJ'

print(mbti)
print(mbti[0])

my_list = [123, 'apple']
print(my_list)

colors = ['red', 'blue', 'green']

# 수정
# colors[2] = 'black'
# print(colors)

# 추가 1
# colors.append('purple')
# print(colors)

# 추가 2
# colors.insert(1, 'yellow')
# print(colors)

# 제거 1
# del colors[0]
# print(colors)

# 제거 2
# color = colors.pop(0)
# print(colors)
# print(color)

# 제거 3
colors.remove('blue')
print(colors)

# 리스트 정렬

colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']

# 정렬 1
# colors.sort()
# print(colors)

# colors.sort(reverse=True)
# print(colors)

# 정렬 2
sorted(colors)
print(colors)
