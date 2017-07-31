infoArr = []

# 添加新名片
def add_info():
	name = str(input('请输入您的姓名: '))
	age  = int(input('请输入您的年龄: '))
	qq   = int(input('请输入您的QQ号: '))
	infoDic = {"name":name,"age":age,"qq":qq}
	global infoArr
	print(infoArr)
	infoArr.append(infoDic)
	print(infoArr)
	print('='*10)

# 删除一个名片
def del_info():
	name = input('请输入您要删除的人员的名字: ')
	f = open('info.data','r')
	info = eval(f.read())
	info_temp = info
	find_flag = 0
	for p in info:
		if name == p["name"]:
			find_flag = 1
			info_temp.remove(p)
			f.close()

			f = open('info.data','w')
			f.write(str(info_temp))
			f.close()
	if find_flag == 0:
		print('不存在删除的人员,请重新查找')
	else:
		print('删除成功')

# 查询一个名片
def search_info():
	name = input("请输入您要查找的人的姓名: ")
	f = open('info.data','r')
	info = eval(f.read())
	search_flag = 0
	for p in info:
		if name == p["name"]:
			search_flag = 1;
			print('此人信息为:\n')
			print('姓名:%s\n'%p["name"])
			print('年龄:%s\n'%p["age"])
			print('QQ号:%s\n'%p["qq"])
	if search_flag == 0:
		print('查无此人')
	f.close()

# 更改一个名片
def modify_info():
	name = input('请输入您要更改信息的人员的名字: ')
	f = open('info.data','r')
	info = eval(f.read())
	info_temp = info
	find_flag = 0
	for p in info:
		if name == p["name"]:
			find_flag = 1
			f.close()

			age = str(input('请输入%s要更改的年龄'%name))
			qq = str(input('请输入%s要更改的qq号码'%name))
			p["age"] = age
			p["qq"] = qq

			f = open('info.data','w')
			f.write(str(info))
			f.close()

	if find_flag == 0:
		print('当前需要修改信息的人员不存在,请确认后重新输入')
	else:
		print('更改成功')
		
# 展示全部名片
def show_info():
	f = open('info.data','r')
	info = eval(f.read())
	for p in info:
		print('------\t')
		print('姓名:%s\n'%p["name"])
		print('年龄:%s\n'%p["age"])
		print('QQ号:%s\n'%p["qq"])
	f.close()

# 保存名片
def save_info():
	try:
		f = open('info.data','w')
		f.write(str(infoArr))
	except Exception as e:
		print('保存失败')
		raise e
	else:
		print('保存成功')
	finally:
		f.close()

def load_info():
	f = open('info.data','r')
	global infoArr
	infoArr = eval(f.read())

# 定义打印格式
def printMsg():
	print("===" * 10)
	print("   名片管理系统 V0.01")
	print(" 1. 添加一个新的名片")
	print(" 2. 删除一个名片")
	print(" 3. 修改一个名片")
	print(" 4. 查询一个名片")
	print(" 5. 显示所有的名片")
	print(" 6. 保存信息")
	print(" 7. 退出系统")
	print("===" * 10)

def main():
	printMsg()
	load_info()
	while True:
		num = int(input("请输入您的操作: "))
		if num == 1:
			add_info()
		elif num == 2:
			del_info()
		elif num == 3:
			modify_info()
		elif num == 4:
			search_info()
		elif num == 5:
			show_info()
		elif num == 6:
			save_info()
		elif num == 7:
			break
		else:
			print('输入有误,请重新输入: ')

if __name__ == '__main__':
	main()