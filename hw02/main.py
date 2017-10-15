def search(list,target):
    begin = 0
    if list[0] == target:
        return 0

    end = len(list)-1
    while(begin < end):
        mid = begin + (end - begin)//2
        if list[mid]>target:
            end = mid - 1
        elif list[mid] <target:
            begin = mid + 1
        else:
            return mid

    if(begin == end):
        if(target == list[begin]):
            return begin
        else:
return -1
