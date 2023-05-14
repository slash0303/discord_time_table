import discord
from discord.ext import commands
import json
from collections import OrderedDict

# 커스텀 확장 모듈
from easy_module_extension import LogE
from easy_module_extension import jsonE
from dict_sort_extension import usrdat

# 봇 토큰 파싱
privacy = jsonE.load("privacy.json")
token = privacy["token"]

# 봇 커맨드 감지 문자
bot = commands.Bot(command_prefix = "/") 

#json으로 데이터 전달 시 매개체
file_data = OrderedDict() 

@bot.event
async def on_ready():
	LogE.g("Login bot", bot.user)
	
# 커맨드 - 봇 지연시간 출력
@bot.command(name="핑")
async def ping(ctx):
	await ctx.send(f"핑: {round(round(bot.latency, 4)*1000)}ms")
	
# 커맨드 - 유저 별 학교 데이터 등록
@bot.command(name="학교등록")
async def schoolRegister(ctx):
	school_name = ctx.message.content.replace("/학교등록 ", "")
	user_info_class_mem = ctx.message.author
	user_info = str(user_info_class_mem)
	user_data = usrdat.school(user_info, school_name, False)
	
	load_data = jsonE.load("data.json")
	
	load_data["user"][user_info]["school"] = school_name
	# TODO 데이터 덮어쓰기가 아닌 수정하기로 로직 변경
	jsonE.dumps("data.json", user_data)
	LogE.g("학교 설정", f"{user_info} - {school_name}")
	await ctx.send(f"'{user_info}'의 학교가 '{school_name}'으로 설정되었습니다. ")
	
@bot.command(name="test")
async def test(ctx):
	# ctx 함수 테스트
	print(ctx.message.content)
	print(type(ctx.message.content))
	print(ctx.message.author)
	print(type(ctx.message.author))
	print(type(str(ctx.message.author)))
	print(str(ctx.message.author))
	# Log_extension으로 로깅 테스트
	LogE.d("log","message")
	LogE.e("error", "message")
	LogE.E("log", "message")
	LogE.g("log", "message")
	#메시지 전송 테스트
	await ctx.send(ctx.message.content)

bot.run(token)