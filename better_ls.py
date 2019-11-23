#!/usr/bin/env python

from subprocess import check_output

decode_file_type = {
    '-': 'Regular file',
    'd': 'Directory',
    'l': 'Symlink'
}

decode_file_perm = {
    'r': 'Read',
    'w': 'Write',
    'x': 'Execute'
}

readable_string = ""

def main():
    one_line = [x.split() for x in check_output(['ls', '-lh']).decode().split("\n")][1]

    print("the one line is")
    print(one_line)
    print()

    readable_file_name(one_line[-1])

    file_type = one_line[0][0]
    readable_file_type(file_type)

    owner_perms = one_line[0][1:4]
    readable_owner_perms(owner_perms)

    owner_group_perms = one_line[0][4:7]
    readable_owner_group_perms(owner_group_perms)

    other_users_perms = one_line[0][7:10]
    readable_other_users_perms(other_users_perms)

    readable_num_hard_links(one_line[1])

    readable_owner(one_line[2])

    readable_owner_group(one_line[3])

    readable_size(one_line[4])

    readable_last_modified(" ".join(one_line[5:8]))

    print(readable_string)


def readable_file_name(filename):
    global readable_string

    readable_string += "Filname: {} | ".format(filename)


def readable_file_type(file_type_code):
    global readable_string

    readable_string += decode_file_type[file_type_code]

def readable_owner_perms(owner_perms):
    global readable_string

    readable_string += ' | '
    readable_string += 'Owner can '

    readable_perms = ''
    for perm in owner_perms:
        if decode_file_perm.get(perm):
            readable_perms += decode_file_perm.get(perm, '')
            readable_perms += ', '

    readable_string += readable_perms


def readable_owner_group_perms(owner_group_perms):
    global readable_string

    readable_string += ' | '
    readable_string += 'Owner Group can '

    readable_perms = ''
    for perm in owner_group_perms:
        if decode_file_perm.get(perm):
            readable_perms += decode_file_perm.get(perm, '')
            readable_perms += ', '

    readable_string += readable_perms


def readable_other_users_perms(other_users_perms):
    global readable_string

    readable_string += ' | '
    readable_string += 'Other users can '

    readable_perms = ''
    for perm in other_users_perms:
        if decode_file_perm.get(perm):
            readable_perms += decode_file_perm.get(perm, '')
            readable_perms += ', '

    readable_string += readable_perms


def readable_num_hard_links(num_hard_links):
    global readable_string

    readable_string += ' | '
    readable_string += 'Num of hard links {}'.format(num_hard_links)


def readable_owner(owner):
    global readable_string

    readable_string += ' | '
    readable_string += 'Owner {}'.format(owner)


def readable_owner_group(owner_group):
    global readable_string

    readable_string += ' | '
    readable_string += 'Owner Group {}'.format(owner_group)


def readable_size(size):
    global readable_string

    readable_string += ' | '
    readable_string += 'Size {}'.format(size)

def readable_last_modified(last_modified):
    global readable_string

    readable_string += ' | '
    readable_string += 'Last Modified {}'.format(last_modified)


if __name__ == '__main__':
    main()
