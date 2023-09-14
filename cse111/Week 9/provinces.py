def main():
    test = read_txt("C:\\Users\\Danie\\OneDrive\\Área de Trabalho\\BYUI\\cse111\\Week 9\\provinces.txt")
    print(test)


def read_txt(filename):
    txt = []
    count = 0

    with open(filename, "rt") as provinces:
        for province in provinces:
            clean_line = province.strip()
            replace_line = clean_line.replace("AB", "Alberta")
            if replace_line == "Alberta":
                count += 1

            txt.append(replace_line)

    print(f"Alberta appears: {count} times")
    return txt

main()