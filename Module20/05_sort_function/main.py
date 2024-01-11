def tpl_sort(tpl):
    tpl_list = list(tpl)
    float_flag = False
    for _, num in enumerate(tpl_list):
        if isinstance(num, float):
            float_flag = True
    if float_flag:
        return tuple(tpl)
    else:
        for index_1 in range(len(tpl_list)):
            for index_2 in range(index_1 + 1, len(tpl_list)):
                if tpl_list[index_1] >= tpl_list[index_2]:
                    tpl_list[index_1], tpl_list[index_2] = tpl_list[index_2], tpl_list[index_1]
        return tuple(tpl_list)
