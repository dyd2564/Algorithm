def solution(my_string, is_suffix):
    
    
    if is_suffix == my_string[len(my_string)-len(is_suffix):]:
        return 1
    return 0