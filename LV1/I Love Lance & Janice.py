def solution(x):
    result=""
    for letter in x:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            result+=chr(ord('z')-(ord(letter)-ord('a')))
        else:
            result+=letter
    return result

solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")