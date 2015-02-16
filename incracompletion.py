import sublime_plugin
import sublime
import os, fnmatch,re

# limits to prevent bogging down the system
result = []
class IncraComplete(sublime_plugin.EventListener):

	def on_query_completions(self, view, prefix, locations):
		#print(view.word())
		open_bracket = view.substr(sublime.Region(locations[0],locations[0]-2))
		close_bracket = view.substr(sublime.Region(locations[0],locations[0]+1))
		trigger = view.substr(sublime.Region(locations[0],locations[0]-1))
		extension = os.path.splitext(view.file_name())[1]
		print(open_bracket,close_bracket)
		if (open_bracket == "[:" and extension == ".html" and close_bracket == "]") or (trigger == '?' and close_bracket == "]"):
			print(trigger,extension)
			try:
				regex = re.compile(prefix, re.IGNORECASE)
				result.sort()
				matches = [string for string in result if re.search(regex, string)]
				# print (matches)
				match = [(w, w.replace('.html', '',)) for w in matches]
				# print (match,prefix)
				print(match)
				return match
			except ValueError:
				print(e)

		return []

	def without_duplicates(words):
		result = []
		for w in words:
			if w not in result:
				result.append(w)
				return result

	def on_new(self,view):
		dirs = sublime.active_window().folders()
		if len(dirs) == 1:
			for d in dirs:
				for root, dirs, files in os.walk(d):
					for file in files:
					# without_duplicates(files)
					# print (files)
						matches = [(w, w.replace('.html', '',)) for w in files]
					# print (matches)
						for m in files:
							if m not in  result:
								result.append(m)
								print (result)


	def on_post_save(self,view):
		dirs = sublime.active_window().folders()
		if len(dirs) == 1:
			for d in dirs:
				for root, dirs, files in os.walk(d):
					for file in files:
					# without_duplicates(files)
					# print (files)
						matches = [(w, w.replace('.html', '',)) for w in files]
					# print (matches)
						for m in files:
							if m not in  result:
								result.append(m)
								print (result)


	def __init__(self):
		dirs = sublime.active_window().folders()
		if len(dirs) == 1:
			for d in dirs:
				for root, dirs, files in os.walk(d):
					for file in files:
					# without_duplicates(files)
					# print (files)
						matches = [(w, w.replace('.html', '',)) for w in files]
					# print (matches)
						for m in files:
							if m not in  result:
								result.append(m)
								# print (result)
