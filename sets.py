def remove_duplicate(some_list):
    # without_duplicates = []
    # for element in some_list:
    #     if element not in without_duplicates:
    #         without_duplicates.append(element)
    # return without_duplicates
    lista = set(some_list)
    return list(lista)

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicate(random_list))


if __name__=="__main__":
    run()