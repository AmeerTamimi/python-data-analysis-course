# Assignment #3: Python Problem-Solving

# Task 1: Set Operations Without Built-in Methods
# Given the following two lists, implement the union, intersection, difference, and symmetric difference operations without using built-in set methods.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Union: combine both lists without duplicates
res = []
for i in list1:
    if i not in res:
        res.append(i)

for i in list2:
    if i not in res:
        res.append(i)

# Intersection: find common elements between both lists
res = []
for i in list1:
    if i in list2 and i not in res:
        res.append(i)

# Symmetric difference: elements in either list but not in both
res = []
for i in list1:
    if i not in list2:
        res.append(i)

for i in list2:
    if i not in list1:
        res.append(i)


# Task 2: Paragraph Analysis and Cleaning
paragraph = """Manchester United, often referred to simply as United, is one of the most successful football clubs in the world.
               Established in 1878 as Newton Heath LYR Football Club, the team changed its name to Manchester United in 1902.
               The club has won a record 20 English League titles, 12 FA Cups, five League Cups, and three European Champions Cups.
               Manchester United has a large fan base and has been home to many legendary players, including George Best, Bobby Charlton, and Cristiano Ronaldo.
               The club's home ground is Old Trafford, which has a capacity of 74,140. In recent years, Manchester United has been striving to reclaim its former glory under various managers.
               As of the 2022-2023 season, the team continues to compete at the highest levels of English and European football."""

# Count the total number of words in the paragraph
total = len(paragraph.split())

# Find and print the most frequent word in the paragraph
dic = {}
max = 0
mostFrequent = ""
for word in paragraph.split():
    word = word.lower()
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1
        if max < dic[word]:
            max = dic[word]
            mostFrequent = word

# Find and print the longest word in the paragraph along with its length
dic = {}
max = 0
mostFrequent = ""
for word in paragraph.split():
    word = word.lower()
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1
    if max < dic[word]:
        max = dic[word]
        mostFrequent = word

print(mostFrequent)
print(max)

# Remove/clean all numbers from the paragraph
res = []
for word in paragraph.split():
    if not word.isdigit():
        res.append(word)


# Task 3: Remove Redundant Numbers from List
nums = [1, 2, 4, 5, 5, 5, 7, 5, 7, 4, 2, 4]

# Remove duplicates without using set() - create new list
dic = {}
res = []
for num in nums:
    if num not in dic:
        dic[num] = 1
        res.append(num)

# Remove duplicates in-place (modify original nums list) without using set()
dic = {}
i = 0
while i < len(nums):
    if nums[i] not in dic:
        dic[nums[i]] = 1
        i += 1
    else:
        nums.remove(nums[i])