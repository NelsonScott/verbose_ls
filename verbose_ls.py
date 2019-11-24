#!/usr/bin/env python

from subprocess import check_output


class LSFormatter:
    """Formats ls command into verbose, human readable output."""

    code_to_file_permission = {
        'r': 'Read',
        'w': 'Write',
        'x': 'Execute'
    }
    code_to_file_type = {
        '-': 'Regular file',
        'd': 'Directory',
        'l': 'Symlink'
    }

    def __init__(self):
        self.verbose_ls_output = []
        self.get_ls_output()

    def get_ls_output(self):
        ls_output = check_output(['ls', '-lh']).decode().split("\n")
        self.one_line = [x.split() for x in ls_output][1]

    def format_and_print(self):
        self.get_ls_output()

        self._set_readable_file_name()
        self._set_readable_file_type()
        self._set_all_readable_perms()
        self._set_readable_meta_data()

        print(" \n ".join(self.verbose_ls_output))

    def _set_readable_file_name(self):
        filename = self.one_line[-1]
        self._update_verbose_ls_output("Filename", filename)

    def _set_readable_file_type(self):
        file_type_code = self.one_line[0][0]
        file_type = self.code_to_file_type[file_type_code]
        self._update_verbose_ls_output("File Type", file_type)

    def _set_all_readable_perms(self):
        perm_info = self.one_line[0]

        perm_codes_and_types = [
            [perm_info[1:4], 'Owner'],
            [perm_info[4:7], 'Group'],
            [perm_info[7:10], 'Other Users']
        ]
        for perm_code_and_type in perm_codes_and_types:
            self._set_readable_perms(perm_code_and_type[0], perm_code_and_type[1])

    def _set_readable_perms(self, perm_codes, owner_type):
        readable_perms = []
        for perm_code in perm_codes:
            permission = self.code_to_file_permission.get(perm_code)
            if permission:
                readable_perms.append(permission)

        readable_perms = ', '.join(readable_perms)
        self._update_verbose_ls_output('{} Permissions'.format(owner_type), readable_perms)

    def _set_readable_meta_data(self):
        self._update_verbose_ls_output('Hard Links', self.one_line[1])
        self._update_verbose_ls_output('Owner', self.one_line[2])
        self._update_verbose_ls_output('Owner Group', self.one_line[3])
        self._update_verbose_ls_output('Size', self.one_line[4])
        last_modified = " ".join(self.one_line[5:8])
        self._update_verbose_ls_output('Last Modified', last_modified)

    def _update_verbose_ls_output(self, title, desc):
        self.verbose_ls_output.append("{}: {}".format(title, desc))


if __name__ == '__main__':
    LSFormatter().format_and_print()
