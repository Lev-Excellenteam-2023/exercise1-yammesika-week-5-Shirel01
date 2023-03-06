def join(*param, sep="-"):
    if not param:
        return None

    newlist = param[0]
    rest_of_list = param[1:]
    for list in rest_of_list:
        newlist += sep
        newlist += list

    print(newlist)




