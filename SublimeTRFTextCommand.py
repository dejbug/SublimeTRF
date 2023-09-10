import sublime
import sublime_plugin

# import re

def getCursorPos(view):
	sel = view.sel()
	if sel: return sel[0]

def getLineRegionAtPoint(view, point):
	return view.line(point)

def getLineAtPoint(view, point):
	region = getLineRegionAtPoint(view, point)
	return view.substr(region)

def getCurrentLineRegion(view):
	point = getCursorPos(view)
	return getLineRegionAtPoint(view, point)

def getCurrentLine(view):
	point = getCursorPos(view)
	return getLineAtPoint(view, point)

def replaceLineWithText(view, edit, text):
	region = getCurrentLineRegion(view)
	view.replace(edit, region, text)

def addPhantomToCurrentLine(view, html, key = 'trf-phantastic!', single = False):
	if single: view.erase_phantoms(key)
	region = getCurrentLineRegion(view)
	region = sublime.Region(region.a, region.b)
	print(region)
	return view.add_phantom(key, region, html, sublime.PhantomLayout.BLOCK)

def removePhantoms(view, key = 'trf-phantastic!'):
	view.erase_phantoms(key)

def removePhantom(view, pid):
	view.erase_phantom_by_id(pid)

def compareRegions(a, b):
	return a.a == b.a and a.b == b.b

def isPhantomAtCurrentLine(view, pid):
	if pid is None: return False
	cregion = getCurrentLineRegion(view)
	pregion = view.query_phantom(pid)[0]
	return compareRegions(cregion, pregion)

def findPhantomAtCurrentLine(view, pids):
	for pid in pids:
		if isPhantomAtCurrentLine(view, pid):
			return pid

def togglePhantomAtCurrentLine(view, pids, html, *aa, **kk):
	pid = findPhantomAtCurrentLine(view, pids)
	if pid:
		removePhantom(view, pid)
	else:
		pid = addPhantomToCurrentLine(view, html, *aa, **kk)
		pids.append(pid)


HTML = '''
	<body id="trf-hint">
		<style>
			div.hint {
				background-color: #333;
				color: hotpink;
				padding: 0;
			}
		</style>
		<div class="hint">%s</div>
	</body>
'''

def html(text, padded = True):
	return HTML % text.replace(' ', '&nbsp;')

TOURNAMENT_START_DATE = '    DD/MM/YYYY'
PLAYER_LINE = '001    1 m  g Mirzoev Azer                      2527 AZE    13400304 1978        4.0    1    26 w 1    13 b 1     8 w 1     4 b 1'

class Phantoms:

	def __init__(self, view):
		self.pids = []

	# removeAll / clear / reset

	# setAtCurrentLine / set
	# removeFromCurrentLine / remove
	# isSetAtCurrentLine / IsSet

	# setAtLine / setAt
	# removeFromLine / removeAt
	# isSetAtLine / isSetAt

	# toggleAtLine / toggleAt
	# toggleAtCurrentLine / toggle

# self.view.add_regions('annotastic!',
# 	[sublime.Region(0, 100)],
# 	scope='invalid',
# 	annotations=[minihtml],
# 	flags=(sublime.DRAW_NO_FILL),
# 	on_close=self.hide_annotations)
#
#	view.erase_regions('annotastic!')
#	view.hide_popup()

class SublimeTrfTextCommand(sublime_plugin.TextCommand):

	def __init__(self, *aa, **kk):
		super().__init__(*aa, **kk)
		self.pid = None
		self.pids = []

	def run(self, edit, action = ''):
		self.edit = edit

		# <div class="error">&nbsp;&nbsp;&nbsp;&nbsp;DD/MM/YYYY</div>

		if action == '042':
			# This is highly problematic
			# replaceLineWithText(self.view, edit, '042 DD/MM/YYYY')
			pass

		elif action == 'hint': # <F1>
			line = getCurrentLine(self.view)

			if line.startswith('042') or line.startswith('052'):
				togglePhantomAtCurrentLine(self.view, self.pids, html(TOURNAMENT_START_DATE))
			elif line.startswith('001'):
				togglePhantomAtCurrentLine(self.view, self.pids, html(PLAYER_LINE))

			elif self.pid:
				if isPhantomAtCurrentLine(self.view, self.pid):
					# removePhantoms(self.view)
					removePhantom(self.view, self.pid)
					self.pid = None
				else:
					self.pid = addPhantomToCurrentLine(self.view, html('Hello again!'))
			else:
				removePhantoms(self.view)
				self.pid = addPhantomToCurrentLine(self.view, html('Hello!'))

		elif action == 'unhint': # <S-F1>
			removePhantoms(self.view)
			self.pid = None

	def onPhantomLinkClicked(self, href):
		print(href)
