import PyPDF2
import my_file
from my_file import\
    check_filepath, \
    get_filepath_to_create, \
    get_path_name_ext_from_full_path, \
    get_name_from_full_path

def merge_pdf():
    files = []
    i = 1
    while True:
        file = input('File ' + str(i) + ' (press Enter to end): ')
        if not file:
            print(str(i - 1) + ' file' + ('s' if i > 1 else '') + ' to merge. ')
            break
        if not check_filepath(file, ext='.pdf'):
            print('Please enter a valid pdf file path. ')
        else:
            files.append(file)
            i += 1
    if len(files) <= 1:
        print('At least two files to do merge. ')
        return

    # output to directory of the first file
    path0, name0, _ = get_path_name_ext_from_full_path(files[0])
    output_name = input('Enter output file name (without extension)\n' + \
                   '  <shortcut> 0 for default \n' + \
                   '  <shortcut> 1 for <first file name>_merged \n' + \
                   '  <shortcut> 2 for file names concatenated \n' + \
                   ': ')
    if output_name == '0':
        output_name = 'merged'
    if output_name == '1':
        output_name = name0 + '_merged'
    if output_name == '2':
        output_name = '_'.join(map(get_name_from_full_path, files))
    output_path = get_filepath_to_create(path0 + output_name + '.pdf')

    merger = PyPDF2.PdfMerger()
    for file in files:
        merger.append(file)
    with open(output_path, 'xb') as f:
        merger.write(f)

merge_pdf()
