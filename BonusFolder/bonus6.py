user_entries = ['10', '19.1', '20']
def sum_list(usernames):
    result = 0
    for str in user_entries:
        float_num = float(str)
        
        result += float_num
    return result

print(sum_list(user_entries))