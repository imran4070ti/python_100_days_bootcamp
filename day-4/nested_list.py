row1 = ['😞', '😞', '😞']
row2 = ['😞', '😞', '😞']
row3 = ['😞', '😞', '😞']
lists = [row1, row2, row3]
print(f'{lists[0]}\n{lists[1]}\n{lists[2]}')

index = input('Enter the position: ')
row = int(index[0]) - 1
col = int(index[1]) - 1

lists[row][col] = '😂'
print(f'{lists[0]}\n{lists[1]}\n{lists[2]}')
