sequence_a =[7,10,12,14,16,20,29,37]
def binary_search(seqence,item):
    begin_index =0
    end_index = len(sequence)-1
    while begin_index <= end_index:
     midpoint = begin_index + (end_index - begin_index) //2
     midpoint_value = sequence [mid]
    if midpoint_value == item:
        return midpoint
    elif item < midpoint_value:
        end_index = midpoint - 1
    else:
        begin_index = midpoint + 1
 return None
 item_a = 14,29
