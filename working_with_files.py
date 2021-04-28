def open_and_print_file(file="order.txt"):
    try:
        with open(file, "r") as opened_file:
            for line in opened_file.readlines():
                print(line.rstrip("\n"))
    except FileNotFoundError as errmsg:
        print("There has been an error opening your file!")
        print(errmsg)
    finally:
        print("Execution complete")


def write_to_file(order_item,file="order.txt"):
    try:
        with open(file, "x") as opened_file:
            opened_file.write(order_item + "\n")
    except FileNotFoundError:
        print("file cannot be found")
    except FileExistsError:
        print("file already exists")

write_to_file("Chocolate")
open_and_print_file()
