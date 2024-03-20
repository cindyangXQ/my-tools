import os

def get_path_name_ext_from_full_path(full_path: str) -> str:
    splits = full_path.split('/')
    path = '' if len(splits) <= 1 else ('/'.join(splits[:-1]) + '/')

    splits = splits[-1].split('.')
    if len(splits) <= 1:
        raise ValueError('Path does not include name or extention: ' + filepath)
    name = '.'.join(splits[:-1])

    ext = '.' + splits[-1]

    return path, name, ext

def get_path_from_full_path(full_path: str) -> str:
    splits = full_path.split('/')
    path = '' if len(splits) <= 1 else ('/'.join(splits[:-1]) + '/')
    return path

def get_name_from_full_path(full_path: str) -> str:
    splits = full_path.split('/')[-1].split('.')
    if len(splits) <= 1:
        raise ValueError('Path does not include name or extention: ' + filepath)
    name = '.'.join(splits[:-1])
    return name

def get_ext_from_full_path(full_path: str) -> str:
    splits = full_path.split('/')[-1].split('.')
    if len(splits) <= 1:
        raise ValueError('Path does not include name or extention: ' + filepath)
    ext = '.' + splits[-1]
    return ext

def check_filepath(filepath: str, ext: str = '') -> bool:
    if ext:
        if (ext[0] != '.'):
            raise ValueError('ext to check illegal. Re-enter with \'.\'')
        ext_len = len(ext)
        if filepath[-ext_len:] != ext:
            return False
    if not os.path.exists(filepath):
        return False
    return True

def get_filepath_to_create(filepath: str) -> str:
    path, name, ext = get_path_name_ext_from_full_path(filepath)    
    if path and not os.path.exists(path):
        raise ValueError('Path of file to create does not exist: ' + filepath)

    i = 0
    while True:
        suffix = '' if i == 0 else ('(' + str(i) + ')')
        new_path = path + name + suffix + ext
        if not os.path.exists(new_path):
            return new_path
        else:
            i += 1
