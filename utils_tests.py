import random

from utils import reversed, formatter

def tester(function: str, test_sequence:list):
    for item in test_sequence:
        print(f'Attempting: {item} of type {type(item)}')
        try:
            if function == 'reversed':
                if reversed(item) == int(str(item)[::-1]):
                    print(f'Pass: {reversed(item)}')
                else:
                    print('Failed')
            elif function == 'formatter':
                if formatter(item) == (bin(item), oct(item)):
                    print(f'Pass: {formatter(item)}')
                else:
                    print('Failed')
        except:
            print('Failed')

if __name__ == '__main__':
    print('Testing reversed...')
    tester('reversed', [1234567890, -1234567890, 0.123456789, '1234567890', random.randint(0,9999999999), random.random()])
    print('Testing formatter...')
    tester('formatter', [1234567890, -1234567890, 0.123456789, '1234567890', random.randint(0,9999999999), random.random()])