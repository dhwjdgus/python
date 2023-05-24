from pathlib import Path

def shopping(shop_file):
    file_path = Path("data") / shop_file
    with open(file_path, 'r') as file:
        result = {}
        for line in file:
            item, price = line.strip().split(',')
            result[item] = int(price)
        return result
