from re import *
import csv
with open("phonebook_raw.csv", 'r', encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

num_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
              r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
              r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'

num_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\20'
contacts_list_new = []
for page in contacts_list:
    page_string = ','.join(page)
    format_page = sub(num_pattern, num_pattern_new, page_string)
    page_list = format_page.split(',')
    contacts_list_new.append(page_list)

name_pattern = r'^(\w+)(\s*)(\,?)(\w+)' \
               r'(\s*)(\,?)(\w*)(\,?)(\,?)(\,?)'
name_pattern_new = r'\1\3\10\4\6\9\7\8'
contacts_list = []
for page in contacts_list_new:
    page_string = ','.join(page)
    format_page = sub(name_pattern, name_pattern_new, page_string)
    page_list = format_page.split(',')
    contacts_list.append(page_list)

for i in contacts_list:
    if len(i) != len(contacts_list[0]) and i[-1] == '':
        i.remove(i[-1])

for i in contacts_list:
    for j in contacts_list:
        if i[0] == j[0] and i[1] == j[1]:
            if i[2] == '':
                i[2] = j[2]
            if i[3] == '':
                i[3] = j[3]
            if i[4] == '':
                i[4] = j[4]
            if i[5] == '':
                i[5] = j[5]
            if i[6] == '':
                i[6] = j[6]
        contact_list = []
        for page in contacts_list:
            if page not in contact_list:
                contact_list.append(page)


with open("phonebook.csv", "w", encoding='UTF-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contact_list)