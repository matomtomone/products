import os

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
	return products

def user_input(list_1):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		list_1.append([name, price]) #清單中加入另一個清單[name, price]
	print(list_1)

def print_now(list_1):
	for p in list_1:
		print(p[0], '的價格是', p[1])

def write_now(filename, list_1):
	with open(filename, 'w', encoding='utf-8') as f :
		f.write('商品,價格\n') #寫入標題列
		for p in list_1:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	if os.path.isfile('products.csv'):
		print('找到檔案!')
		products = read_file('products.csv')
		user_input(products)
		print_now(products)
		write_now('products.csv', products)
	else:
		print('沒有讀到檔案')

main()