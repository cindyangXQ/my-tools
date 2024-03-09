import PyPDF2

def get_name_from_path(path: str):
    return path.split('/')[-1][:-4]

def merge():
    files = []
    i = 1
    while True:
        file = input('File ' + str(i) + ' (press Enter to end): ')
        if not file:
            print(str(i - 1) + ' file' + ('s' if i > 1 else '') + ' to merge. ')
            break
        files.append(file)
        i += 1
    if len(files) <= 1:
        print('At least two files to do merge. ')
        return

    output = input('Output file name (without extension): \n' + \
                   '0 for default. \n' + \
                   '1 for <first file name>_merged. \n' + \
                   '2 for file names concatenated. \n' + \
                   'Enter output file name: ')
    if output == '0':
        output = 'merged'
    if output == '1':
        output = get_name_from_path(files[0]) + '_merged'
    if output == '2':
        output = '_'.join(map(get_name_from_path, files))

    merger = PyPDF2.PdfMerger()
    for file in files:
        merger.append(file)
    try: 
        with open(output + '.pdf', 'xb') as f:
            merger.write(f)
    except OSError:
        output += ' - copy'
        with open(output + '.pdf', 'xb') as f:
            merger.write(f)

merge()
