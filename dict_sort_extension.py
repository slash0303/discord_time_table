from easy_module_extension import LogE

class usrdat:
	
	#유저 학교 정보 dict로 정렬
	def school(user_data, school_data, only_user_data: bool):
		if only_user_data == False:
			dict = {"user": {user_data: {"school": school_data} } }
			return dict
		elif only_user_data == True:
			dict = {user_data: {"school": school_data} }
			return dict
		else:
			LogE.e("dict_sort_extension - usedat.school 오류", "only_user_data의 if문에서 else가 반환 됨")