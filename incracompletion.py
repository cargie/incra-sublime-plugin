import sublime_plugin
import sublime
import os, fnmatch,re
from . import replacers
result = []

def get_scope_attribute():
	return replacers.replacer_list
# limits to prevent bogging down the system
class IncraComplete(sublime_plugin.EventListener):

	def on_query_completions(self, view, prefix, locations):
		start= locations[0]
		end = locations[0]
		open_bracket_colon = view.substr(sublime.Region(locations[0],locations[0]-2))
		open_bracket = view.substr(sublime.Region(locations[0],locations[0]-1))
		close_bracket = view.substr(sublime.Region(locations[0],locations[0]+1))
		trigger = view.substr(sublime.Region(locations[0],locations[0]-1))
		extension = os.path.splitext(view.file_name())[1]
		if (open_bracket_colon == "[:" and extension == ".html"):
			print(locations[0])
			try:
				regex = re.compile(prefix, re.IGNORECASE)
				result.sort()
				matches = [string for string in result if re.search(regex, string)]
				match = [(w+'\t Block', (w.replace('.html', '',))+ ({True:'',False:']'}[close_bracket==']']) )  for w in matches]
				
				return (match,sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
				
			except ValueError:
				print(e)
		elif(open_bracket== "[" and extension == ".html" or trigger == '?'):
			return ([(w+'\t Scope', (w.replace('.html', '',))+ ({True:'',False:'$0]'}[close_bracket==']']) )  for w in sorted(get_scope_attribute().keys())],sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)

		elif(trigger == '.' and (close_bracket=="]" or close_bracket != ']')):

			vw = ''
			x = 1
			# while(vw != '['):
			# 	vw = view.substr(sublime.Region(start-1-x, end-x))
			# 	x=x+1
			# 	if (x> 15):
			# 		break
			while True:
				vw = view.substr(sublime.Region(start-1-x, end-x))
				if (vw == '[' or vw =='?'):
					vw = view.substr(sublime.Region(start-1-x, end-x))
					print(vw)
					break
				else:
					x+=1
			print(x)
			vw = view.substr(sublime.Region(start-x, end-1))
			print (vw)
			return ([(w+'\tAttribute',(w)+ ({True:'',False:'$0]'}[close_bracket==']'])) for w in (get_scope_attribute().get(vw))],sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)

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
						matches = [(w, w.replace('.html', '',)) for w in files]
					# print (matches)
						for m in files:
							if m not in  result:
								result.append(m)
								print (result)
