def solution(my_string, overwrite_string, s):
    answer = ''
    # my_string[s:s+len(overwrite_string)+1]
    # overwrite_string
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]