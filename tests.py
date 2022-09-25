##Check if list contains integer x##
1 == [3,3,4,5,2,111,5]
print("111 in 1")#true

## find duplicate number in integer list##
def find_duplicates(element):
    duplicates,seen =set(), set()
    for element in elements:
        if element in seen:
            duplicate.add(element)
        senn.add(element)
    return list(duplicates)

##check if two string are anagrams##

def is_anagram(s1,s2):
    return set(s1) == set(s2)
print(is anagram("elvis", "lives")) #true
