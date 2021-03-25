#build holding property file
#3_25_21
class Maneymanager:
	def __init__(self):
		self.belongings = []
		self.holding_belongings()
		if self.did_loan():
			self.loan()
		self.filename = self.file_name()
		self.write_file()

	def holding_belongings(self):
		while True:
			self.belongings.append(input('please input your holding belongings: '))
			print('your holdingbelongings is', self.belongings)
			break
	def loan(belongings):
		self.belongings.append(input('please input your loan: '))
		
	def write_file(self):
		with open(self.filename+ '.csv', 'w', encoding='utf-8') as f:
			f.write('Property,\n')
			for b in self.belongings:
				f.write(b + '\n')
		print('Now Ledger file is completed.')

	def file_name(self):
		return 'moneymanager'

	def did_loan(self):
		user_loan = input('Did you have loan?(y/n)')
		if user_loan == 'y' or user_loan == 'Y':
			return True
		elif user_loan == 'n' or user_loan == 'N':
			return False
		
MG = Maneymanager()