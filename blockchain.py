import hashlib
import os
import json


def get_dir_block():
    return os.curdir + '/blocks/'


def get_sorted_list_blocks():
    return sorted([int(i) for i in os.listdir(get_dir_block())])


def get_path_to_block(number):
    return f'{get_dir_block()}{number}'


def get_hash(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def write_block(name, surname, replica):
    last_number = get_sorted_list_blocks()[-1]
    current_number = last_number + 1
    data = {'name': name,
            'surname': surname,
            'replica': replica,
            'hash': get_hash(get_path_to_block(last_number))}

    with open(get_path_to_block(current_number), 'wt') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def check_integrity():
    blocks = get_sorted_list_blocks()
    result = []
    for i in blocks[1:]:
        hash_last = get_hash(get_path_to_block(i-1))
        with open(get_path_to_block(i)) as f:
            hash_current = json.load(f)['hash']
        result.append({"block": i-1, 'status': ['wrong', 'correct'][hash_current == hash_last]})
    return result


def main():
    for i in range(4):
        write_block('1', '2', 'text')


if __name__ == '__main__':
    main()

