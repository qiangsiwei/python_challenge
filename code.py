# -*- coding: utf-8 -*- 

def level00():
	print 2**38

def level01():
	from string import maketrans
	_from, _to = 'abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab'
	_trans = maketrans(_from, _to)
	string = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
	print string.translate(_trans)
	url = "map"
	print url.translate(_trans)

def level02():
	print ''.join([char for char in open('data/level_02.txt').read() if char.isalpha()])

def level03():
	import re
	_cont = ''.join([line.strip() for line in open('data/level_03.txt')])
	print ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', _cont))

def level04():
	import re
	import urllib
	_url, _num = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=', '12345'
	for i in range(400):
		_data = urllib.urlopen('{0}{1}'.format(_url, _num)).read()
		_num = ''.join([_char for _char in _data if _char.isdigit()])
		print '{0}{1}'.format(_url, _num)

def level05():
	import cPickle
	_cont = cPickle.load(file('data/level_05_banner.p'))
	for line in _cont:
		print ''.join([_tup[0]*_tup[1] for _tup in line])

def level06():
	import zipfile
	_num, _comments = '90052', []
	with zipfile.ZipFile('data/level_06_channel.zip', 'r') as _zip:
		while True:
			try:
				_data = _zip.open('{0}.txt'.format(_num),'r').read()
				_comments.append(_zip.getinfo('{0}.txt'.format(_num)).comment)
				_num = ''.join([_char for _char in _data if _char.isdigit()])
			except:
				print ''.join(_comments)
				break

def level07():
	import re
	from PIL import Image
	_im = Image.open('data/level_07_oxygen.png')
	_pixel = [_im.getpixel((x,_im.size[1]/2)) for x in range(0, _im.size[0], 7)]
	_mash = [r for r,g,b,a in _pixel if r==g==b]
	print ''.join(map(chr, map(int, re.findall(r'\d{3}', ''.join(map(chr, _mash))))))

def level08():
	import bz2
	_un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
	_pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
	print [bz2.decompress(x) for x in(_un, _pw)]

def level09():
	from PIL import Image
	from PIL import ImageDraw
	_first = [146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,
	310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,
	190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,
	389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
	215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,
	290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,
	279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,
	327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
	328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,
	259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,
	352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,
	120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
	214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,
	102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,
	113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,
	133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,
	111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,
	332,155,348,156,353,153,366,149,379,147,394,146,399]
	_second = [156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,
	157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,
	125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,
	77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
	158,121,157,128,156,134,157,136,156,136]
	_img = Image.new('RGB',(640,480))
	_draw = ImageDraw.Draw(_img)
	_draw.line(_first)
	_draw.line(_second)
	_img.show()

def level10():
	def getNext(seq):
		i, next_seq = 0, ""
		while i <= len(seq)-1:
			cnt = 1
			while i <= len(seq)-2 and seq[i] == seq[i+1]:
				cnt += 1
				i += 1
			next_seq += str(cnt)+seq[i]
			i += 1
		return next_seq
	seq = "1"
	for i in xrange(30):
		seq = getNext(seq)
		print len(seq)

def level11():
	from PIL import Image, ImageEnhance
	from cStringIO import StringIO
	_img = Image.open('data/level_11_cave.jpg')
	_img = ImageEnhance.Brightness(_img)
	_img.enhance(8).show()

def level12():
	_binary = open('data/level_12_evil2.gfx','rb').read()
	[open('data/evil%d.jpg' %i,'wb').write(_binary[i::5]) for i in range(5)]

def level13():
	import xmlrpclib
	_server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
	print _server.phone('Bert')

def level14():
	from PIL import Image
	_im = Image.open('data/level_14_wire.png')
	_new = Image.new(_im.mode,(100,100))
	_seq = [x/2 for x in range(200,0,-1)]
	for _edge in range(len(_seq)):
		for _pixel in range(_seq[_edge]):
			if (100-_seq[_edge])%2 == 0:
				x = _pixel+(100-_seq[_edge])/2
			else:
				x = _pixel+(100-_seq[_edge])/2+1
			y = _edge//4
			_new.putpixel((x,y),_im.getpixel((sum(_seq[:_edge])+_pixel,0)))
		_new = _new.rotate(90)
	_new.show()

def level15():
	from calendar import weekday, isleap
	print filter(lambda y: isleap(y) and 0==weekday(y, 1, 26), range(1006, 2000, 10))[-2]

def level16():
	from PIL import Image
	im = Image.open('data/level_16_mozart.gif')
	for height in range(im.size[1]):
		line=[im.getpixel((width,height)) for width in range(im.size[0])]
		pink=line.index(195)
		line=line[pink:]+line[:pink]
		[im.putpixel((width,height),pixel) for width,pixel in enumerate(line)]
	im.show()

def level17():
	import cookielib,urllib,urllib2, re,bz2,xmlrpclib
	from urllib2 import Request
	from urllib import quote_plus
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	res = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php')
	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
	seed = '12345'
	info = ''
	while 1:
		req = urllib.urlopen(url+seed)
		content = req.read()
		seed = ''.join(re.findall(r"busynothing is (\d+)", content))
		cookies = req.info().getheaders('Set-Cookie')[0]
		byte = cookies.split(';')[0].split('=')[1]
		info += byte
		try:
			int(seed)
			print "Info:",byte,"	Next:",seed
		except:
			print "Info:",byte,"	Last:",content
			break
	print "info:",bz2.decompress(urllib.unquote_plus(info))
	server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
	print server.phone('Leopold')
	inform = 'the flowers are on their way'
	url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
	req = Request(url,headers={'Cookie':'info='+quote_plus(inform)})
	print urllib2.urlopen(req).read()

def level18():
	import gzip
	import difflib
	deltas = gzip.GzipFile('data/level_18_deltas.gz','rb').read()
	deltas = deltas.splitlines()
	left, right, png = [], [], ['','','']
	for row in deltas:
		left.append(row[:53])
		right.append(row[56:])
	diff = list(difflib.ndiff(left, right))
	for row in diff:
		bytes = [chr(int(byte,16)) for byte in row[2:].split()]
		if row[0]=='-': png[0]+=''.join(bytes)
		elif row[0]=='+': png[1]+=''.join(bytes)
		elif row[0]==' ': png[2]+=''.join(bytes)
	for i in range(3):
		open('data/level_18_%d.png' % i ,'wb').write(png[i])

def level19():
	import base64,wave,array
	_file = open('data/level_19')
	a = array.array('c',base64.b64decode(_file.read()))
	a.byteswap()
	_file.close()
	wav = wave.open('data/level_19_indian.wav','wb')
	wav.setnchannels(1)
	wav.setsampwidth(1)
	wav.setframerate(22050)
	wav.writeframes(a.tostring())
	wav.close()

def level20():
	import urllib
	url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg'
	for i in [(30237,30337), (30284,30384), (30295,30395), (30313,30413),\
				(2123456744,2123456788), (2123456712,2123456743)]:
		opener = urllib.FancyURLopener({})
		opener.addheader('range','bytes=%d-%d' % i)
		f = opener.open(url)
	opener = urllib.FancyURLopener({})
	opener.addheader('range','bytes=1152983631-1152983671')
	f = opener.open(url)
	open('data/level_20.zip','wb').write(f.read())

def level21():
	import zlib, bz2
	reverse = lambda x:x[::-1]
	reverse.__module__='reverse'
	decompressors = [zlib.decompress,bz2.decompress, reverse]
	step = True
	last = None
	logs = []
	data = open("data/level_20/package.pack",'rb').read()
	while step:
		step = False
		for decompress in decompressors:
			try:
				if last == decompress.__module__ in ('reverse',): raise Exception()
				data = decompress(data)
				step = True
				last = decompress.__module__
				logs.append((len(data),last))
				break
			except:
				pass
	mark = dict(zlib='.',bz2='*',reverse='\r\n')
	print "".join([mark[log[1]] for log in logs])

def level22():
	from PIL import Image, ImageSequence
	import turtle, time
	im = Image.open("data/level_22_white.gif")
	locations = []
	for frame in ImageSequence.Iterator(im):
		data = list(frame.getdata())
		index = data.index(8)
		y,x = divmod(index,200)
		locations.append((x,y))
	EXP = 2
	x = y = 0 
	for pilx,pily in locations:
		dx = (pilx-100)//2
		dy = (100-pily)//2
		x += dx*EXP
		y += dy*EXP
		turtle.goto(x,y)
		if dx == dy == 0:
			time.sleep(1)
			turtle.reset()
			x = y = 0

def level23():
	import this

def level24():
	from PIL import Image
	def BFS(maze, path):
		dirs = [(0,1),(0,-1),(1,0),(-1,0)]
		wall = (255,)*4
		w,h = maze.size
		maze.putpixel((1,h-1),wall)
		maze.putpixel((w-2,0),wall)
		queue = [(1,h-2)] #enter
		path[queue[0]] = 'exit'
		while queue:
			pos = queue.pop(0)
			for d in dirs:
				new_pos = (pos[0]+d[0], pos[1]+d[1])
				if not path.has_key(new_pos) and maze.getpixel(new_pos) != wall:
					path[new_pos] = pos
					queue.append(new_pos)
	maze = Image.open('data/level_24_maze.png')
	path = {}
	BFS(maze,path)
	maze.show()
	w = maze.size[0]
	pos = (w-2,1)
	while pos != 'exit':
		maze.putpixel(pos,(0,0,255,255))
		pos = path[pos]
	maze.show()

def level25():
	import urllib, wave
	from PIL import Image
	from cStringIO import StringIO
	url = "http://butter:fly@www.pythonchallenge.com/pc/hex/lake%i.wav"
	canvas = Image.new('RGB',(300,300))
	for i in range(25):
		wav = wave.open(StringIO(urllib.urlopen(url % (i+1)).read()))
		piece = Image.frombytes('RGB',(60,60),wav.readframes(10800))
		canvas.paste(piece,((i%5)*60,(i/5)*60))
	canvas.show()

if __name__ == '__main__':
	level25()

