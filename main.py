from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
import time

Window.softinput_mode = 'below_target'
#Window.clearcolor = (1, 0, 0.4, 1)

Builder.load_file("widgetsModification.kv")
Builder.load_file("screen.kv")


class LoginScreen(Screen):
	def animateTextfieldOpen(self, textField):
		cnt = .01
		if textField == 'txt1':
			for x in range(15):
				self.text1.size_hint = (.4+cnt, .25)
				cnt += 0.02
				#time.sleep(0.2)
			
		elif textField == 'txt2':
			for i in range(15):
				self.text2.size_hint = (.4+cnt, .25)
				cnt += 0.02
				#time.sleep(0.2)
			
		else:
			pass

	def show_pane(self, textField):
		if textField == "txt1":
			if self.text1.text == "Username":
				self.text1.text = ""
			else:
				pass
		
		elif textField == "txt2":
			if self.text2.text == "Password":
				self.text2.text = ""
			else:
				pass
		else:
			pass

class SearchScreen(Screen):
    #py_rst_text = ThirdWindow.py_rst_text
    def do_search(self):
        self.rst_text.text = '\n'.join(("LeoRon Books.io", "----------------","``Here are your search queries third tab.``", ''))
        self.rst_text.text += str("\n\nYour search: " +"**" + self.search_text.text + "**\n")
        #user_search = str(input('Enter your search word: '))
        OxfordUrl = "https://en.oxforddictionaries.com/definition/" + self.search_text.text
        #GoogleUrl = "https://www.google.com/search?=" + self.search_text.text

        webpage = ul(OxfordUrl).read()
        soupObj = sp(webpage, "lxml")

        if soupObj.find('span', {'class':'ind'}).text == None:
            self.rst_text.text += "\n\n**No results found!** "
        else:
            NounDef = soupObj.find('span', {'class':'ind'}).text
            self.rst_text.text += "\n\n**[color=#FF0000][b][i]Definition:[/i][/b][/color][/u]** "+NounDef + '\n\n'

        exampleTag = soupObj.find('div', {'class':'exg'})
        listExample = exampleTag.find_all('li', {'class':'ex'})

        if listExample == None or listExample == []:
            self.rst_text.text += "**No examples found** \n\n" 
        else:
            self.rst_text.text += "Examples:\n\n"
            cnt = 1
            for i in listExample:
                self.rst_text.text += ("\t[b][i]{0}[/i][/b]".format(cnt) + str(i.text) + '\n\n')
                cnt += 1
                print(i)
            

        try:
            synonymTag = soupObj.find('div', {'class':'synonyms'})
            synonym = synonymTag.find('div', {'class':'exs'}).text
            self.rst_text.text += "\n\n**[color=#FFFF00][b][i]Synonyms:[/i][/b][/color][/u]** "
            self.rst_text.text += synonym + '\n'

        except Exception:
            self.rst_text.text += "\n\nNo synonym\n"
            pass
class ResultsScreen(Screen):
	pass

class WindowManager(ScreenManager):
    pass

class KlenamMasterApp(App):
    def build(self):
        return WindowManager()

if __name__ == '__main__':
    KlenamMasterApp().run()
