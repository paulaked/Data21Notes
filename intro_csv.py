import csv
def extract_user_details(csv_file):
    with open(csv_file) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_list = list(csvreader)
    return csv_list

def transform_user_details(csv_list):
    iterable_csv = iter(csv_list)
    next(iterable_csv)
    user_list = []
    for row in iterable_csv:
        user_list.append([row[1], row[2], row[-1]])
    return user_list

def create_csv(old_user_details, new_file_name):
    old = extract_user_details(old_user_details)
    new_user_details = transform_user_details(old)
    with open(new_file_name, "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_details)

create_csv("user_details.csv", "new.csv")