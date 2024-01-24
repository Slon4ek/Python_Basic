from Classes import *
elements_list = [Fire(), Water(), Earth(), Air()]

for i_index, i_val in enumerate(elements_list):
    for j_index, j_val in enumerate(elements_list[i_index + 1:]):
        print(i_val + j_val)
