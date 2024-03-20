import os

def get_filepath_to_create(filepath: str) -> str:
    splits = filepath.split('/')
    path = '' if len(splits) <= 1 else ('/'.join(splits[:-1]) + '/')
    if path and not os.path.exists(path):
        raise OSError('File path to create is illegal: ' + filepath)

    splits = splits[-1].split('.')
    if len(splits) <= 1:
        raise OSError('File name to create is illegal: ' + filepath)
    name = '.'.join(splits[:-1])
    
    ext = '.' + splits[-1]

    i = 0
    while True:
        suffix = '' if i == 0 else ('(' + str(i) + ')')
        new_path = path + name + suffix + ext
        if not os.path.exists(new_path):
            return new_path
        else:
            i += 1

    
