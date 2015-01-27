import sublime_plugin
import sublime
import os

# limits to prevent bogging down the system


class AllAutocomplete(sublime_plugin.EventListener):

	def on_new(self,view):
		print("carl")

	def on_query_completions(self, view, prefix, locations):
		for root, dirs, files in os.walk('/data/ShopData/Test/designs/Sample6/'):
			for file in files:
				if file.startswith(prefix):
					matches = [(w, w.replace('.html', '')) for w in files]
					print (words)
						

if sublime.version() >= '3000':
  	def is_empty_match(match):
    	return match.empty()
else:
  	def is_empty_match(match):
    	return match is None