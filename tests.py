import random
from blockchain import write_block, check_integrity


def test_create_blocks():
    for i in range(random.randrange(3, 10)):
        write_block(*[str(random.random())]*3)
    blocks = check_integrity()
    assert all([i['status'] == 'correct' for i in blocks]), print_blocks(blocks)


def print_blocks(blocks):
    for block in blocks:
        print(block['block'], block['status'])
