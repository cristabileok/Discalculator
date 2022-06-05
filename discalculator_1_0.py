import kivy
from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder

ux = Builder.load_file("discalculator.kv")

dumb_detail = []
dumb_show = []
disc_list = []
dumb_discs = {}

button_list = []

only_discs_1 = 0
only_discs_2 = 0
only_discs_5 = 0
only_discs_10 = 0

total_discs_1 = 0
total_discs_2 = 0
total_discs_5 = 0
total_discs_10 = 0

class Label_Weights(Label):
    pass

class Button_Weights(Button):
    pass

class Label_Results(Label):
    pass

class Label_Add(Label):
    pass

class Main_Window(Widget):
    pass

    def addDumbbell(self):

        excluded = [0,1,2,5,10,15,20,25,30]

        if self.ids.textinput.text != "" and not(int(self.ids.textinput.text) in excluded) :
            discs_dumb_1 = 0
            discs_dumb_2 = 0
            discs_dumb_5 = 0
            discs_dumb_10 = 0

            weight = int(self.ids.textinput.text)
            
            perfect = range(7,42,5)
            step = range(3,42,5)
            jump = range(4,42,5)
            weird = range(6,42,5)

            if weight in perfect:
                weight_adjusted = weight -2
            elif weight in step:
                weight_adjusted = weight - 2 + .25
            elif weight in jump:
                weight_adjusted = weight -2 +.5
            elif weight in weird:
                weight_adjusted = weight -2 - .25
            discs_dumb_1 += weight_adjusted /1.25
            discs_dumb_1 = int(discs_dumb_1)
            
            while (discs_dumb_1 + discs_dumb_2 + discs_dumb_5 + discs_dumb_10) > 8:
                if discs_dumb_1 >= 2:
                    discs_dumb_1 -= 2
                    discs_dumb_2 += 1
                elif discs_dumb_2 >= 2:
                    discs_dumb_2 -= 2
                    discs_dumb_5 += 1
                
            while discs_dumb_1 > 8:
                discs_dumb_1 -= 4
                discs_dumb_2 += 2
            while discs_dumb_2 > 6:
                discs_dumb_2 -= 4
                discs_dumb_5 += 2
            while discs_dumb_5 > 6:
                discs_dumb_5 -= 2
                discs_dumb_10 += 1

            dumb_detail.append([weight,discs_dumb_1,discs_dumb_2,discs_dumb_5,discs_dumb_10])
  
            block = BoxLayout(orientation="horizontal")
            dumb_show.append(block)
            self.ids.dumb_pile.add_widget(block)

            dumbbell = Button_Weights()
            dumbbell.text ="Dumbbell \n{}K".format(weight)
            
            block.add_widget(dumbbell)
            button_list.append(dumbbell)
            #dumbbell.bind(on_release = self.ids.dumb_pile.remove_widget(block))
                     
            detail_1 = Label_Weights()
            detail_1.text ="{}\nx 1,25K".format(discs_dumb_1)
            detail_2 = Label_Weights()
            detail_2.text ="{}\nx 2,5K".format(discs_dumb_2)
            detail_5 = Label_Weights()
            detail_5.text ="{}\nx 5K".format(discs_dumb_5)
            detail_10 = Label_Weights()
            detail_10.text ="{}\nx 10K".format(discs_dumb_10)
            
            block.add_widget(detail_1)
            block.add_widget(detail_2)
            block.add_widget(detail_5)
            block.add_widget(detail_10)
    
            
    def addDisc(self):
        
        global only_discs_1
        global only_discs_2
        global only_discs_5
        global only_discs_10

        discs = [1,2,5,10,15,20]

        #these_discs_1 = 0
        #these_discs_2 = 0
        #these_discs_5 = 0
        #these_discs_10 = 0
        
        if self.ids.textinput.text != "" and int(self.ids.textinput.text) in discs:
            weight = int(self.ids.textinput.text)

            if weight == 1:
                only_discs_1 += 1
            if weight == 2:
               only_discs_2 += 1
            if weight == 5:
                only_discs_5 += 1
            if weight == 10:
                only_discs_5 += 2
            if weight == 15:
                only_discs_5 += 3
            if weight == 20:
                only_discs_10 += 1
                only_discs_5 += 2

            self.ids.disc_1.text="{}\nx 1,25K".format(only_discs_1)
            self.ids.disc_2.text="{}\nx 2,5K".format(only_discs_2)
            self.ids.disc_5.text="{}\nx 5K".format(only_discs_5)
            self.ids.disc_10.text="{}\nx 10K".format(only_discs_10)

    def addEverything(self):
        global total_discs_1
        global total_discs_2 
        global total_discs_5
        global total_discs_10

        total_discs_1 = 0
        total_discs_2 = 0
        total_discs_5 = 0
        total_discs_10 = 0

        for dumbbell in dumb_detail:
            total_discs_1 += dumbbell[1]
            total_discs_2 += dumbbell[2]
            total_discs_5 += dumbbell[3]
            total_discs_10 += dumbbell[4]

        total_discs_1 += only_discs_1
        total_discs_2 += only_discs_2
        total_discs_5 += only_discs_5
        total_discs_10 += only_discs_10

        
      
    def Adjust(self):
        global total_discs_1
        global total_discs_2
        global total_discs_5
        global total_discs_10
        while total_discs_1 > 12:
            total_discs_1 -= 2
            total_discs_2 += 1

            '''dumb_weights = []
            for dumb in dumb_detail:
                dumb_weights.append(dumb[0])
                heaviest_weight = dumb_weights.sorted(reverse=True)[0]
            counter = 0
            while counter == 0:
                for dumb in dumb_detail:
                    if dumb[0] == heaviest_weight:
                        if dumb[1] >= 2:
                            dumb[1] -= 2
                            dumb[2] += 1

                            counter += 1'''
            


        while total_discs_2 > 10:
            total_discs_2 -= 2
            total_discs_5 += 1
        while total_discs_5 > 6:
            total_discs_5 -= 2
            total_discs_10 += 1

    def Remove(self,button):
        self.ids.dumb_pile.clear_widgets(dumb_show[button_list.index(button)])          
      
    def Show(self):
        self.ids.num_1.text= "[size=40]{}[/size]\nx 1,25K".format(int(total_discs_1))
        if total_discs_1 > 8:
            self.ids.add_1.text= "[b][size=40]{}[/size][/b]\nx 1,25K".format(int(total_discs_1)-8)
        else: 
            self.ids.add_1.text= "[b][size=40]0[/size][/b]\nx 1,25K"

        self.ids.num_2.text= "[size=40]{}[/size]\nx 2,5K".format(int(total_discs_2))
        if total_discs_2 > 4:
            self.ids.add_2.text= "[b][size=40]{}[/size][/b]\nx 2,5K".format(int(total_discs_2)-4)
        else: 
            self.ids.add_2.text= "[b][size=40]0[/size]\nx 2,5K[/b]"

        self.ids.num_5.text= "[size=40]{}[/size]\nx 5K".format(int(total_discs_5))        
        self.ids.add_5.text= "[b][size=40]{}[/size][/b]\nx 5K".format(int(total_discs_5))
        self.ids.num_10.text="[size=40]{}[/size]\nx 10K".format(int(total_discs_10))
        self.ids.add_10.text="[b][size=40]{}[/size][/b]\nx 10K".format(int(total_discs_10))

    def Calculate(self):
        self.addDumbbell()
        self.addDisc()
        self.addEverything()
        self.Adjust()
        self.Show()
        self.textReset()
        self.ids.textinput.text=""

    def textReset(self):
        if self.ids.textinput.text == "0":
            self.Reset()

    def Reset(self):
        global total_discs_1
        global total_discs_2
        global total_discs_5
        global total_discs_10
        
        total_discs_1 = 0
        total_discs_2 = 0
        total_discs_5 = 0
        total_discs_10 = 0

        global only_discs_1
        global only_discs_2
        global only_discs_5
        global only_discs_10

        only_discs_1 = 0
        only_discs_2 = 0
        only_discs_5 = 0
        only_discs_10 = 0

        global dumb_detail
        
        dumb_detail = []

        self.ids.num_1.text= ""
        self.ids.num_2.text= ""
        self.ids.num_5.text= ""
        self.ids.num_10.text=""

        self.ids.disc_1.text= ""
        self.ids.disc_2.text= ""
        self.ids.disc_5.text= ""
        self.ids.disc_10.text=""

        self.ids.add_1.text= ""
        self.ids.add_2.text= ""
        self.ids.add_5.text= ""
        self.ids.add_10.text=""
                
        self.ids.dumb_pile.clear_widgets()
        
        self.ids.textinput.focus=True

    def keep_records(self):
        pass

    def remove_item(self):
        self.ids.parent.remove_widget(self)


class DiscalculatorApp(App):
    def build(self):
        return Main_Window()
        


if __name__ == "__main__":
    DiscalculatorApp().run()

