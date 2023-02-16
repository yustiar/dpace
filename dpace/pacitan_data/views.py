from django.shortcuts import render
import requests as re 
from django.http import JsonResponse
import json
import ast
import time


def splash(request):
	context = {
		'Title' : 'Data Pacitan | Data Pacitan ',
		'Heading' : 'Dashboard Data',

	}

	return render(request, 'splash.html', context)

def index(request):
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'infographic',
		'lang': 'ind',
		'domain': '3501',
		'page':1,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}

	res = re.get(url, params=params)
	data = res.json()
	posts = data['data'][1]
	
	# #INDICATOR
	# tes = re.get('https://raw.githubusercontent.com/yustiar/data-pacitan/main/indicator.txt')
	# indicator=tes.text.split('\n')
	# indtitle = []
	# indcontent = []
	# for i in range(len(indicator)):
	# 	if (len(indicator[i])>1):
	# 		indtitle.append(indicator[i].split(';')[0])
	# 		indcontent.append(indicator[i].split(';')[1])
	# indall = zip(indtitle, indcontent)
	context = {
		'Title' : 'Data Pacitan | Data Pacitan ',
		'Heading' : 'Dashboard Data',
		'posts':posts,
		# 'indall':indall,
	}

	return render(request, 'index.html', context)
def load_init_berita(request):
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'news',
		'lang': 'ind',
		'domain': '3501',
		'page':1,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}

	res = re.get(url, params=params)
	data = res.json()
	posts = data['data'][1]
	totalitem = data['data'][0]
	return JsonResponse(data={
		'posts':posts,
		'totalitem':totalitem
	})
def load_more_berita(request):
	offset=int(request.POST['offset'])
	page=(offset/10)+1
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'news',
		'lang': 'ind',
		'domain': '3501',
		'page':page,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}
	posts=[]

	res = re.get(url, params=params)
	data = res.json()

	posts = data['data'][1]
	totalresult = data['data'][0]['total']
	return JsonResponse(data={
		'posts':posts,
		'totalResult':totalresult,
	})

def detail_berita(request):
	indeksberita=request.POST['offset']
	url = 'https://webapi.bps.go.id/v1/api/view'
	params = {
		'model': 'news',
		'lang': 'ind',
		'domain': '3501',
		'id':indeksberita,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}
	res = re.get(url, params=params)
	data = res.json()
	posts = data['data']
	return JsonResponse(data={
		'posts':posts,
	})
def cari_berita(request):
	keyword=request.POST['offset']
	posts=[]
	print(keyword)
	if len(keyword) > 2:
		for i in range(100):
			url = 'https://webapi.bps.go.id/v1/api/list'
			params = {
				'model': 'news',
				'lang': 'ind',
				'domain': '3501',
				'page':i+1,
				'key': '481cbe5f8403e091cb7abfd4d83829a3',
				'keyword': keyword
			}
			res = re.get(url, params=params)
			data = res.json()
			if data['data-availability'] != 'list-not-available':
				posts.extend(data['data'][1])
			else:
				break
	
	return JsonResponse(data={
		'posts':posts,
	})

def load_init_pub(request):
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'publication',
		'lang': 'ind',
		'domain': '3501',
		'page':1,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}

	res = re.get(url, params=params)
	data = res.json()
	posts = data['data'][1]
	totalitem = data['data'][0]
	return JsonResponse(data={
		'posts':posts,
		'totalitem':totalitem
	})
def load_more_pub(request):
	offset=int(request.POST['offset'])
	page=(offset/10)+1
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'publication',
		'lang': 'ind',
		'domain': '3501',
		'page':page,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}
	posts=[]

	res = re.get(url, params=params)
	data = res.json()

	posts = data['data'][1]
	totalresult = data['data'][0]['total']
	return JsonResponse(data={
		'posts':posts,
		'totalResult':totalresult,
	})

def detail_pub(request):
	indekspub=request.POST['offset']
	url = 'https://webapi.bps.go.id/v1/api/view'
	params = {
		'model': 'publication',
		'lang': 'ind',
		'domain': '3501',
		'id':indekspub,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}
	res = re.get(url, params=params)
	data = res.json()
	posts = data['data']
	return JsonResponse(data={
		'posts':posts,
	})
def cari_pub(request):
	keyword=request.POST['offset']
	posts=[]
	if len(keyword) > 2:
		for i in range(100):
			url = 'https://webapi.bps.go.id/v1/api/list'
			params = {
				'model': 'publication',
				'lang': 'ind',
				'domain': '3501',
				'page':i+1,
				'key': '481cbe5f8403e091cb7abfd4d83829a3',
				'keyword': keyword
			}
			res = re.get(url, params=params)
			data = res.json()
			if data['data-availability'] != 'list-not-available':
				posts.extend(data['data'][1])
			else:
				break

	return JsonResponse(data={
		'posts':posts,
	})
def load_init_brs(request):
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'pressrelease',
		'lang': 'ind',
		'domain': '3501',
		'page':1,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}

	res = re.get(url, params=params)
	data = res.json()
	posts = data['data'][1]
	totalitem = data['data'][0]
	return JsonResponse(data={
		'posts':posts,
		'totalitem':totalitem
	})
def load_more_brs(request):
	offset=int(request.POST['offset'])
	page=(offset/10)+1
	url = 'https://webapi.bps.go.id/v1/api/list'
	params = {
		'model': 'pressrelease',
		'lang': 'ind',
		'domain': '3501',
		'page':page,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}
	posts=[]

	res = re.get(url, params=params)
	data = res.json()

	posts = data['data'][1]
	totalresult = data['data'][0]['total']
	return JsonResponse(data={
		'posts':posts,
		'totalResult':totalresult,
	})
def detail_brs(request):
	indeksbrs=request.POST['offset']
	url = 'https://webapi.bps.go.id/v1/api/view'
	params = {
		'model': 'pressrelease',
		'lang': 'ind',
		'domain': '3501',
		'id':indeksbrs,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}
	res = re.get(url, params=params)
	data = res.json()
	posts = data['data']
	return JsonResponse(data={
		'posts':posts,
	})

def cari_brs(request):
	keyword=request.POST['offset']
	posts=[]
	if len(keyword) > 2:
		for i in range(100):
			url = 'https://webapi.bps.go.id/v1/api/list'
			params = {
				'model': 'pressrelease',
				'lang': 'ind',
				'domain': '3501',
				'page':i+1,
				'key': '481cbe5f8403e091cb7abfd4d83829a3',
				'keyword': keyword
			}
			res = re.get(url, params=params)
			data = res.json()
			if data['data-availability'] != 'list-not-available':
				posts.extend(data['data'][1])
			else:
				break
	
	return JsonResponse(data={
		'posts':posts,
	})

def load_init_data(request):
	sosial = []
	ekonomi = []
	pertanian = []
	
	with open(r"static/json/sosial.json") as f:
	    data1 = f.read()
	with open(r"static/json/ekonomi.json") as f:
	    data2 = f.read()
	with open(r"static/json/pertanian.json") as f:
	    data3 = f.read()
	sosial = list(ast.literal_eval(data1))
	ekonomi = list(ast.literal_eval(data2))
	pertanian = list(ast.literal_eval(data3))

	return JsonResponse(data={
		'sosial':sosial,
		'ekonomi':ekonomi,
		'pertanian':pertanian,
	})

def load_more_data(request):
	posts=[]
	offset=str(request.POST['offset'])
	# print(offset)
	#STATICTABLE
	for i in range(100):
		url = 'https://webapi.bps.go.id/v1/api/list'
		params = {
			'model': 'statictable',
			'lang': 'ind',
			'domain': '3501',
			'subject':int(offset.split("_")[1]),
			'page':i+1,
			'key': '481cbe5f8403e091cb7abfd4d83829a3'
		}
		res = re.get(url, params=params)
		data = res.json()
		if data['data-availability'] != 'list-not-available':
			posts.extend(data['data'][1])
		else:
			break
	  
	
	return JsonResponse(data={
		'posts':posts,
	})
def detail_data(request):
	posts=[]
	offset=str(request.POST['offset'])
	url = 'https://webapi.bps.go.id/v1/api/view'
	params = {
		'model': 'statictable',
		'lang': 'ind',
		'domain': '3501',
		'id':offset,
		'key': '481cbe5f8403e091cb7abfd4d83829a3'
	}
	res = re.get(url, params=params)
	data = res.json()
	posts = data['data']
	return JsonResponse(data={
		'posts':posts,
	})