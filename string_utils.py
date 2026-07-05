from collections import Counter

def reverse_string(s):
    res_s = s[::-1]
    return(res_s)

def count_vowels(s):
    s_temp = s.lower()
    counts = Counter(s_temp)
    return sum(counts[vowel] for vowel in "aeiou")

def is_palindrome(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    print(reverse_string("apple"))
    print(count_vowels("I like apple"))
    print(is_palindrome("A man, a plan, a canal: Panama"))