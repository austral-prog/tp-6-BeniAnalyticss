


def remove_elements(list_to_remove elements):
    if len(list_to_remove elements) >= 6:
        list_to_remove elements.pop(5)
        list_to_remove elements.pop(4)
        list_to_remove elements.pop(0)
        return list
    elif len(list) >= 5:
        list_to_remove elements.pop(4)
        list_to_remove elements.pop(0)
        return list_to_remove elements
    elif len(list_to_remove elements) > 0:
        list_to_remove elements.pop(0)
        return list_to_remove elements
    else:
        return list_to_remove elements


def add_element(list_to_add_elements):
    list_to_add_elements.insert(0,"Pink")
    list_to_add_elements.append("Yellow")
    return list2



def is_empty(list_to_check):
    if len(list_to_check)<=0:
        return True
    else: 
        return False


def check_list(list_to_compare1, list_to_compare2):
    if list_to_compare1[2] == list_to_compare2[2]:
        return True
    elif list_to_compare1[2] != list_to_compare2[2]:
        return False
    elif len(list_to_compare1)<3 or len(list_to_compare2)<3:
        return False
    else:
        return False


def list_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify[0])>1:
        row1= list_of_lists_to_modify[0]
        row1= row1[:2] 
    elif len(list_of_lists_to_modify[0])==1:
        row1= list_of_lists_to_modify[0]
        row1= row1[0]
    else:
        row1= []

    if len(list_of_lists_to_modify[1])>=4:
        row2= list_of_lists_to_modify[1]
        row2= row2[1:4]
    elif len(list_of_lists_to_modify[1])==3:
        row2= list_of_lists_to_modify[1]
        row2= row2[1:3]
    elif len(list_of_lists_to_modify[1])==2:
        row2= list_of_lists_to_modify[1]
        row2= row2[2]
    else:
        row2= []

    if len(list_of_lists_to_modify[2])>=2:
        row3= list_of_lists_to_modify[2]
        row3= [row3[-2],row3[-1]]
    elif len(list_of_lists_to_modify[2])==1:
        row3= list_of_lists_to_modify[2]
        row3= [row3[-1]]
    else:
        row3=[]

    final_table= [row1,row2,row3]
    return final_table
