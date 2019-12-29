
def is_name_has_space(ap_name):
    return " " in ap_name

def filter_example():
    aps = ["Abdur Rahim", "Mofajjul", "Shovon", "Rakibul Anam"]

    # big_names = list(filter(is_name_has_space, aps))
    big_names = list(filter(lambda x:" " in x, aps))
    print(big_names)


if __name__ == "__main__":
    filter_example()