from data import *
import random

MAX_LENGTH = 6
intab = 'abcdefghijklmnopqrstuvwxyz'
namelist = ['adjectives', 'animalnames', 'lastnames', 'midnames', 'placenames', 'surnames']

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
		# return jpname1,

	elif ablength == 3:
		jpname1 = gen_return_dict(['jsname1','jsname2','jgname2'],abbr)
		jpname2 = gen_return_dict(['jptname','jplname','jpename'],abbr)
		cnname1 = gen_return_dict(['csname','cgname1','cgname2'],abbr)
		aniname = gen_return_dict(['adjectives','jpsecpre','animalnames'],abbr)
		placenm = gen_return_dict(['adjectives','animalnames','placenames'],abbr,type = 'place')		
		return jpname1,jpname2,cnname1,aniname

	elif ablength == 4:
		jpname1 = gen_return_dict(['jsname1','jsname2','jgname1','jgname2'],abbr)
		jpname2 = gen_return_dict(['jgname1','jgname2','jsname1','jsname2'],abbr)
		cnname1 = gen_return_dict(['csname','csname','cgname1','cgname2'],abbr)
		return jpname1,jpname2,cnname1

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