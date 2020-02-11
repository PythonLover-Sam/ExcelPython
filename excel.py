import xlrd

global id_values, sid_data

passwords = []
accounts = []
def read_file(filename):
    global id_values, sid_data
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_name("Sheet1")
    rows = sheet.nrows
    cols = sheet.ncols
    id_values = sheet.col_values(9)
    sid_data = sheet.col_values(3)


def to_string(list):
    for i in range(len(list)):
        list[i] = str(list[i])


def get_password(list, passwords_data):
    for i in range(len(list)):
        if i != 0:
            passwords_data.append(list[i][-7:-1])


def get_account(list, accounts_data):
    for i in range(len(list)):
        if i != 0:
            accounts_data.append(list[i][:-2])


if __name__ == "__main__":

    read_file("自动化学院中航候补名单.xlsx")

    to_string(sid_data)

    get_password(id_values, passwords)

    get_account(sid_data, accounts)

    file = open("data.txt", 'w+')
    for i in range(len(accounts)):
        file.write(accounts[i] + "   " + passwords[i] + "\n")