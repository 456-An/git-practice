from collections import Counter

def reverse_string(s: str) -> str:
    res_s = s[::-1]
    return(res_s)

def count_vowels(s: str) -> int:
    s_temp = s.lower()
    counts = Counter(s_temp)
    return sum(counts[vowel] for vowel in "aeiou")

def is_palindrome(s: str) -> bool:
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def count_occurrences(text: str, substring: str) -> int:
    """計算一個字串中，某個子字串出現的次數。

    Args:
        text: 原始字串
        substring: 要搜尋的子字串

    Returns:
        子字串出現的次數

    Raises:
        TypeError: 當 text 或 substring 不是字串時
        ValueError: 當 substring 為空字串時
    """
    if not isinstance(text, str) or not isinstance(substring, str):
        raise TypeError("Both text and substring must be strings")
    if not substring:
        raise ValueError("Substring cannot be empty")
    return text.count(substring)

if __name__ == "__main__":
    print(reverse_string("apple"))
    print(count_vowels("I like apple"))
    print(is_palindrome("A man, a plan, a canal: Panama"))