import time
import json

#로그 클래스
class LogE:
	
	tim = time.localtime(time.time())
	time_format = "%Y-%m-%d %H:%M:%S"
	Log_time = str(time.strftime(time_format, tim))
	
	#일반 로그
	def d(Log_name, Log_text):
		tim = time.localtime(time.time())
		time_format = "%Y-%m-%d %H:%M:%S"
		Log_time = str(time.strftime(time_format, tim))
		print(f"{Log_time} | {Log_name} : {Log_text}")
	
	# 문자 red (에러 로그)
	def e(Log_name, Log_text):
		tim = time.localtime(time.time())
		time_format = "%Y-%m-%d %H:%M:%S"
		Log_time = str(time.strftime(time_format, tim))
		text_red = "\033[31m"
		print(text_red + f"{Log_time} | [Error] {Log_name} : {Log_text}" + "\033[0m")
	
	#문자 green	
	def g(Log_name, Log_text):
		tim = time.localtime(time.time())
		time_format = "%Y-%m-%d %H:%M:%S"
		Log_time = str(time.strftime(time_format, tim))
		text_green = "\033[32m"
		print(text_green + f"{Log_time} | {Log_name} : {Log_text}" + "\033[0m")
		
	#배경 red (에러 로그)
	def E(Log_name, Log_text):
		tim = time.localtime(time.time())
		time_format = "%Y-%m-%d %H:%M:%S"
		Log_time = str(time.strftime(time_format, tim))
		bg_red = "\033[41m"
		print(bg_red + f"{Log_time} | [Error] {Log_name} : {Log_text}" + "\033[0m")
		
#json 클래스
class jsonE:
	
	#json dumps
	def dumps(file_name: str, content):
		name_len = len(file_name)
		json_ext = file_name[name_len-5 : name_len]
		
		if json_ext == ".json":
			pass
		else:
			file_name = file_name + ".json"
			
		with open(file_name, "w", encoding="utf-8") as json_file:
			json.dump(content, json_file, ensure_ascii = False, indent=4)
		LogE.g("dumps json", f"'{file_name}' is dumped")
	
	#json load
	def load(file_name):
		name_len = len(file_name)
		json_ext = file_name[name_len-5 : name_len]
		
		if json_ext == ".json":
			pass
		else:
			file_name = file_name + ".json"
			
		LogE.g("load json", f"'{file_name}' is loaded")
		with open(file_name, "r") as json_file:
			content = json.load(json_file)
			return content
			
class timeE:
	
	# 시간 문자열 반환 함수
	def geta():
		tim = time.localtime(time.time())
		time_format = "%Y-%m-%d %H:%M:%S"
		str_time = str(time.strftime(time_format, tim))

		return str_time
	
	# 커스텀 된 시간 문자열 반환 함수
	# getc함수 입력 예: 연, 월, 일, 시 데이터  >>  timeE.getc("Y-M-D-H")  /  timeE.getc("Year-Month-Day-Hour")
	def getc(time_type):
			tim = time.localtime(time.time())
			time_type.split("-")
			# TODO time_type 입력에 맞춰 time_format 설정(if, 반복문 활용)