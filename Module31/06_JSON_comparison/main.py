import json


def find_diff(old_dict, new_dict, diff_lst, diff_dict=None):
    if diff_dict is None:
        diff_dict = dict()
        for i_key in new_dict.keys():
            if new_dict[i_key] != old_dict[i_key]:
                if i_key in diff_lst:
                    diff_dict[i_key] = new_dict[i_key]
                else:
                    if isinstance(new_dict[i_key], dict):
                        return find_diff(old_dict[i_key], new_dict[i_key], diff_lst)
                    elif isinstance(new_dict[i_key], list):
                        for i in new_dict[i_key]:
                            return find_diff(old_dict[i_key][i], new_dict[i_key][i], diff_lst)
    return diff_dict


with open('json_old.json', 'r', encoding='utf-8') as old_file:
    with open('json_new.json', 'r', encoding='utf-8') as new_file:
        diff_list = ['services', 'staff', 'datetime']
        old = json.loads(old_file.read())
        new = json.loads(new_file.read())
        result = find_diff(old, new, diff_list)
        print(json.dumps(result, ensure_ascii=False, indent=4))
        with open('result.json', 'w', encoding='utf-8') as file:
            json.dump(result, file, ensure_ascii=False, indent=4)
