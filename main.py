# -*- coding: utf-8 -*-
from wox import Wox
import random
MAX_LENGTH = 6
intab = 'abcdefghijklmnopqrstuvwxyz'
namelist = ['adjectives', 'animalnames', 'lastnames', 'midnames', 'placenames', 'surnames']
abbstrmap={
    'adjectives': 	'黯白橙黛二风高黑一金宽蓝墨南圆平青瑞三天乌威万新玉紫',
    'animalnames': 	'鹌豹虫雕鳄蜂龟虎蚁鲸蝌狼马牛猿鹏雀人鲨兔鱿猬蛙虾雁竹',
    'lastnames': 	'敖彬才丹娥凤刚华益军坤亮明楠琳朋强荣生涛佑伟旺新勇忠',
    'midnames': 	'安博从德恩福国海爱家克兰美宁凌培庆睿世铁友维文晓玉志',
    'placenames': 	'庵堡城岛邑府沟会隘街口楼庙南院坡桥入寺堂坞卫湾溪营庄',
    'surnames': 	'阿白陈窦易冯郭黄艾蒋孔李毛倪袁潘钱任孙唐吴韦王徐杨张',
	'jpfname': 		'奥白川大義福高火愛吉堀柳木南元平淺日山藤武尾丸小岩中',
	'jpsname': 		'安本長稻耳豐古河伊金口栗米內原浦千若上田友隈外新野竹',
	'jptname': 		'阿阪赤東刈富谷黑一井康瀨梅鳥猿片清入森土五惟万西永佐',
	'jplname': 		'岸北池島額飯宮戶已江開瀧門楠林坪秋仁石天物位文下羽字',
	'jpename':	 	'庵八村德恩峰國橫乙久空郎末乃欧棚橋染松湯屋為文細燕真',
	'jpuname':	 	'鹌豹虫雕鳄蜂龟虎蚁鲸蝌狼马牛猿鹏雀人鲨兔鱿猬蛙虾燕竹',
	'jpprefix': 	'安本川东義丰高黑伊吉柯濑木南元平崎若松藤友武丸小野佐',
	'jpsecpre': 	'岸部村岛刈方冈河衣井口里门内原浦泉入山田屋尾外西岩泽',
	'jpthirdn': 	'奥北仓大二福贵辉乙江康鹿名能源片前仁石庭有五王新永中',
	'jpsuffix': 	'庵阪成都翼富谷户爱君堀郎美男凌旁清人生太佑吾文翔云子',
	#################################################################
	'jsname1':		'奥北長大尔福谷黑伊吉昆柳名南元平前若三藤柚武宛小羽中',
	'jsname2':		'岸本川岛耳方冈河乙江口里木鸟林浦桥仁山田屋尾湾溪野泽',
	'jgname1':		'阿百池德恩枫高惠爱久康隆麻能全朋崎瑞石庭佑维文信英真',
	'jgname2':		'安博成東邑夫光弘一家堀郎美奈欧旁清戎松堂优隈丸香洋子',
	#################################################################
	'csname':		'阿白陈窦易冯郭黄艾蒋孔李毛倪袁潘钱任孙唐吴韦王徐杨张',
	'cgname1':		'安博从德恩福国海爱家克兰美宁凌培庆睿世铁友维文晓雨志',
	'cgname2':		'敖彬才丹娥凤刚华益军坤亮明楠琳朋强荣生涛佑伟旺新越忠',
}
occupation_dct={
	'辅助':'有爱',
	'法师':'沉稳',
	'射手':'冷血',
	'刺客':'敏锐',
	'坦克':'坚韧',
	'战士':'勇敢',
}

def get_jpstory(name):
	ablength = len(name)
	occupaindex = hash(name) % 6
	occupation = list(occupation_dct.keys())[occupaindex]
	return f'{name}是东瀛大陆一名{occupation_dct[occupation]}的{occupation}。'

def get_story(name):
	ablength = len(name)
	occupaindex = hash(name)%6
	occupation = list(occupation_dct.keys())[occupaindex]
	if ablength == 2:
		return f'{name}是王者大陆一名{occupation_dct[occupation]}的{occupation}。'
	elif ablength == 3:
		return f'{name}是王者大陆一名{occupation_dct[occupation]}的{occupation}。'
	elif ablength == 4:
		return f'{name[:2]}是王者大陆一个盛产{occupation}地方,{name[2:]}是{name[:2]}国一名{occupation_dct[occupation]}的{occupation}.'
	elif ablength == 5:
		return f'{name[:2]}是王者大陆一个盛产{occupation}地方,{name[2:]}是{name[:2]}国一名{occupation_dct[occupation]}的{occupation}.'
	elif ablength == 6:
		return f'{name[:3]}是王者大陆一个盛产{occupation}地方,{name[3:]}是{name[:3]}国一名{occupation_dct[occupation]}的{occupation}.'
	else:
		return "This is my story."

def get_intro(place):
	ablength = len(place)
	occupaindex = hash(place)%6
	occupation = list(occupation_dct.keys())[occupaindex]
	if ablength == 3 or ablength == 2:
		return f'{place}是王者大陆一个盛产{occupation_dct[occupation]}{occupation}地方。'
	else:
		return "This is my story."

def gen_return_dict(names,abbr,type='person'):
	tablelist = [str.maketrans(intab, abbstrmap[name]) for name in names]
	place = ''.join([c.translate(tablelist[i]) for i, c in enumerate(abbr)])
	ablength = len(place)
	occupaindex = hash(place)%6
	occupation = list(occupation_dct.keys())[occupaindex]
	if type == 'place':
		ret = {
			'name':place,
			'story': f'{get_intro(place)}',
		}
	else:
		ret = {
			'name':place,
			'story': f'{get_story(place)}',
		}
	return ret

def get_harmonic(abbr):
	abbr = abbr.lower()
	ablength = len(abbr)
	if ablength ==2:
		jpname1 = gen_return_dict(['jsname1','jsname2'],abbr)
		jpname2 = gen_return_dict(['jgname1','jgname2'],abbr)
		cnname1 = gen_return_dict(['csname','cgname2'],abbr)
		aniname = gen_return_dict(['adjectives','animalnames'],abbr)
		placenm = gen_return_dict(['animalnames','placenames'],abbr,type = 'place')
		return jpname1,jpname2,cnname1,aniname,placenm

	elif ablength == 3:
		jpname1 = gen_return_dict(['jsname1','jsname2','jgname2'],abbr)
		jpname2 = gen_return_dict(['jptname','jplname','jpename'],abbr)
		cnname1 = gen_return_dict(['csname','cgname1','cgname2'],abbr)
		aniname = gen_return_dict(['adjectives','jpsecpre','animalnames'],abbr)
		placenm = gen_return_dict(['adjectives','animalnames','placenames'],abbr,type = 'place')		
		return jpname1,jpname2,cnname1,aniname

	elif ablength == 4:
		jpname1 = gen_return_dict(['jsname1','jsname2','jgname1','jgname2'],abbr)
		return jpname1,

	elif ablength == 5:
		jpname1 = gen_return_dict(['jsname1','jsname2','jsname1','jsname2','jgname2'],abbr)
		jpname2 = gen_return_dict(['jpfname','jpsname','jptname','midnames','jpsuffix'],abbr)
		cnname1 = gen_return_dict(['adjectives','placenames','csname','cgname1','cgname2'],abbr)
		return jpname1,jpname2,cnname1

	elif ablength == 6:
		jpname1 = gen_return_dict(['adjectives','animalnames','placenames','jsname1','jsname2','jgname2'],abbr)
		jpname2 = gen_return_dict(['jsname1','jpsecpre','animalnames','csname','cgname1','cgname2'],abbr)
		return jpname1,jpname2

	else:
		reminder = {
			'name':f"Please type 2-{MAX_LENGTH} bit English characters.",
			'story':f'You can divide long words into small pieces of 2-{MAX_LENGTH} words.'
		}
		return reminder,

reminder = [{
    'name': f"Please type 2-{MAX_LENGTH} bit English characters.",
    'story':"This can help you remember English words by making up a story."
}]
class MagicMnemonics(Wox):
    # query is default function to receive realtime keystrokes from wox launcher
    def query(self, query):
        results = []
        rets = get_harmonic(query) if len(query)>=2 else reminder
        for ret in rets:
            results.append({
                # "Title": "Type 2-6 alphabets, you will get a Chinese name.",
                "Title": "谐音记忆法: {}".format(ret['name']),
                "SubTitle": "Story: {}".format(ret['story']),
                "IcoPath":"Images/app.png",
                "ContextData": "ctxData",
                "JsonRPCAction": {
                    'method': 'take_action',
                    'parameters': ["{}".format("SomeData")],
                    'dontHideAfterAction': False
                }
            })
        return results
    # context_menu is default function called for ContextData where `data = ctxData`

    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath":"Images/app.png"
        })
        return results

    def take_action(self, SomeArgument):
        # Choose what to trigger on pressing enter on the result.
        # use SomeArgument to do something with data sent by parameters.
        return None

if __name__ == "__main__":
    MagicMnemonics()
