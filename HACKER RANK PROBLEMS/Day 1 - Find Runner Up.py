arr = "10 25 45 69 52 52"
list2 = map(int, arr.split())
final_list = list(list2)
final_list.sort(reverse = True)

def get_runnerup(final_list):
    n = 0
    while final_list[n] <= final_list[n+1]:
        n += 1
    else:
        return final_list[n+1] 


print(get_runnerup(final_list))