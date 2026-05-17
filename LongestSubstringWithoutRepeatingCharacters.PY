

s = "pwwkew"


def remove_duplicate(s):
    seen = set()
    start = 0
    max_lenght = 0

    for end in range(len(s)):

        while s[end] in seen:
            # If we see a duplicate, shrink the window from the start
            # until the duplicate is gone
            seen.remove(s[start])
            # after removing first duplicate this will take next letter
            start += 1

        seen.add(s[end])
        max_lenght = max(max_lenght, end - start + 1)
    return max_lenght


print(remove_duplicate(s))
