import sublime
import sublime_plugin

import datetime

class SublimeTRFCommand(sublime_plugin.ViewEventListener):

	def on_load(self):
		# print(dir(sublime_plugin))
		# print(dir(self))
		# print(self.__dict__)
		pass

	def on_modified(self):
		n = self.view.file_name()
		if not n or not n.lower().endswith('.trf'):
			return
		# self.view.insert(edit, 0, "Hello, World!")
		now = datetime.datetime.now().strftime('%H:%M:%S')
		print(now, self.view.file_name())

		for s in self.view.sel():
			# TODO: As soon as a keyword scope is entered,
			#	trigger the relevant TextCommand to complete
			#	the line with the default text / layout.
			# TODO: Maybe make it so that the keyword is
			#	scoped as soon as a valid DIN is entered,
			#	not after a space was added. While this
			#	might flicker the syntax on and off in
			#	other cases, here it is safe, since all
			#	DINs start with the beginning of the line
			#	and are all 3 chars long.

			scope = self.view.scope_name(s.b) if s is not None else ''
			scopes = [s for s in scope.split(' ') if s] if scope else []
			# print(now, s, scopes)
			# print(now, 'keyword.trf' in scopes)

			# Something like this.
			linereg = self.view.line(s.b)
			line = self.view.substr(linereg)
			print(now, linereg, line)
			if line.startswith('012'):
				print('TOURNAMENT NAME')
