#build holding property file
#4_1_21
#新增輸入貸款與持有項目
#補齊loan()
#3_25_21
class Maneymanger:
	#4_6改寫項目清單轉為字典，project轉為清單收納
	def __init__(self):
		self.project = []
		self.belongings = {}
		self.loan = {}
		self.holding_belongings()
		if self.did_loan():
			self.holding_loan()
		self.filename = self.file_name()
		self.write_file()

	def holding_belongings(self):
		while True:
			hd_item = input('please input your holding belonging item: ')
			if hd_item == 'n':
				break
			hd = input('please input your holding belonging: ')
			print('your holdingbelongings item: ', hd_item, ' = ', hd)
			self.belongings[hd_item] = hd
			
	#loan功能完成4/6
	def holding_loan(self):
		self.loan_is_true = True
		while True:
			loan_item = input('please input your loan item: ')
			if loan_item == 'n':
				break
			loan_money = input('please input your loan: ')
			print('your loan item: ', loan_item, ' = ',loan_money )
			self.loan[loan_item] = loan_money

		
	def write_file(self):
		with open(self.filename+ '.csv', 'w', encoding='utf-8') as f:
			f.write('Property,\n')
			for key in self.belongings:
				f.write(key + ',' + self.belongings[key] + '\n')
			if self.loan_is_true:
				f.write('Loan,\n')
				for key in self.loan:
					f.write(key + ',' + self.loan[key] + '\n')

		print('Now Ledger file is completed.')

	def file_name(self):
		return 'moneymanager'

	def did_loan(self):
		user_loan = input('Did you have loan?(y/n)')
		if user_loan == 'y' or user_loan == 'Y':
			return True
		elif user_loan == 'n' or user_loan == 'N':
			return False

		
MG = Maneymanger()