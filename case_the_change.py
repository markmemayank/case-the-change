import tkinter as tk
from tkinter import *


def select_all(event):
    event.widget.tag_add('sel', '1.0', 'end')


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Case the Change')
        self.geometry('1500x1000')
        self.configure(bg='white')
        self.bind_all("<Control-a>", select_all)

        # setting the rows and columns
        self.grid_rowconfigure(0, weight=int(0.5))
        self.grid_rowconfigure(1, weight=int(1.5))
        self.grid_rowconfigure(2, weight=int(1.5))
        self.grid_columnconfigure(0, weight=1)

        # title frame and title
        self.title_frame = tk.Frame(self, border=20, background='#dce7fc')
        self.title_frame.configure(width=1400)
        self.title_frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=20, pady=(20, 10))
        self.title = tk.Label(self.title_frame,
                              text='Write Your Entry Or Paste In The Input Area And Select The Operation That You Want To Perform.')
        self.title.configure(background='#dce7fc', font=('Sofia Pro Medium Az.otf', 19, 'bold'), fg='#011993')
        self.title.grid(pady=20, padx=20, sticky=tk.N + tk.S + tk.E + tk.W)

        # data frame
        self.data_frame = tk.Frame(self, background='white')
        self.data_frame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=20, pady=10)
        self.data_frame.rowconfigure(0, weight=1)
        self.data_frame.columnconfigure(0, weight=1)
        self.data_frame.columnconfigure(1, weight=1)

        # input frame and input area
        self.input_frame = tk.Frame(self.data_frame, background='#dce7fc')
        self.input_frame.grid(padx=20, pady=20, sticky=tk.N + tk.S + tk.E + tk.W, row=0, column=0)
        self.input_frame.rowconfigure(0, weight=int(0.5))
        self.input_frame.rowconfigure(1, weight=int(2))
        self.input_frame.columnconfigure(0, weight=int(1))

        self.input_label = tk.Label(self.input_frame, text='INPUT')
        self.input_label.configure(background='#dce7fc', fg='#011993', font=('Sofia Pro Regular Az.otf', 19, "bold"))
        self.input_label.grid(padx=20, pady=10, row=0, column=0)
        self.input_area = tk.Text(self.input_frame, font=('arial', 16))
        self.input_area.grid(padx=20, pady=(10, 20), row=1, column=0)

        # output frame and output area
        self.output_frame = tk.Frame(self.data_frame, background='#dce7fc')
        self.output_frame.grid(padx=20, pady=20, sticky=tk.N + tk.S + tk.E + tk.W, row=0, column=1)
        self.output_frame.rowconfigure(0, weight=int(0.5))
        self.output_frame.rowconfigure(1, weight=int(2))
        self.output_frame.columnconfigure(0, weight=int(1))

        self.output_label = tk.Label(self.output_frame, text='OUTPUT')
        self.output_label.configure(background='#dce7fc', font=('Sofia Pro Regular Az.otf', 19, "bold"), fg='#011993')
        self.output_label.grid(padx=20, pady=10, row=0, column=0)
        self.output_area = tk.Text(self.output_frame, font=('arial', 16))
        self.output_area.grid(padx=20, pady=(10, 20), row=1, column=0)

        # button frame
        self.button_frame = tk.Frame(self, background='white')
        self.button_frame.grid(padx=20, pady=(10, 20), row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.button_frame.rowconfigure(0, weight=1)
        self.button_frame.rowconfigure(1, weight=1)
        self.button_frame.rowconfigure(2, weight=1)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.columnconfigure(2, weight=1)

        # buttons
        self.alternative_case_button = tk.Button(self.button_frame, text="aLtErNaTiVe CaSe", height=3, width=35,
                                                 font=('Sofia Pro Regular Az.otf', 19), background='darkblue',
                                                 command=self.alternativecase)
        self.alternative_case_button.configure(fg='white')
        self.alternative_case_button.grid(row=0, column=0, pady=10, padx=20)

        self.camel_case_button = tk.Button(self.button_frame, text="camelCase", height=3, width=35,
                                           font=('Sofia Pro Regular Az.otf', 19), background='darkblue',
                                           command=self.camelcase)
        self.camel_case_button.configure(fg='white')
        self.camel_case_button.grid(row=0, column=1, pady=10, padx=20)

        self.title_case_button = tk.Button(self.button_frame, text="Title Case", height=3, width=35,
                                           font=('Sofia Pro Regular Az.otf', 19), background='darkblue',
                                           command=self.titlecase)
        self.title_case_button.configure(fg='white')
        self.title_case_button.grid(row=0, column=2, pady=10, padx=20)

        self.kebab_case_button = tk.Button(self.button_frame, text="kebab-case", height=3, width=35,
                                           font=('Sofia Pro Regular Az.otf', 19), background='darkblue',
                                           command=self.kebabCase)
        self.kebab_case_button.configure(fg='white')
        self.kebab_case_button.grid(row=1, column=0, pady=10, padx=20)

        self.lower_case_button = tk.Button(self.button_frame, text="lowercase", height=3, width=35,
                                           font=('Sofia Pro Regular Az.otf', 19), background='darkblue',
                                           command=self.lowercase)
        self.lower_case_button.configure(fg='white')
        self.lower_case_button.grid(row=1, column=1, pady=10, padx=20)

        self.pascal_case_button = tk.Button(self.button_frame, text="PascalCase", height=3, width=35,
                                            font=('Sofia Pro Regular Az.otf', 19), background='darkblue',
                                            command=self.pascalcase)
        self.pascal_case_button.configure(fg='white')
        self.pascal_case_button.grid(row=1, column=2, pady=10, padx=20)

        self.sentence_case_button = tk.Button(self.button_frame, text="Sentence case", height=3, width=35,
                                              font=('Sofia Pro Regular Az.otf', 19), background='darkblue',
                                              command=self.sentencecase)
        self.sentence_case_button.configure(fg='white')
        self.sentence_case_button.grid(row=2, column=0, pady=10, padx=20)

        self.snake_case_button = tk.Button(self.button_frame, text="snake_case", height=3, width=35,
                                           font=('Sofia Pro Regular Az.otf', 19), background='darkblue',
                                           command=self.snakecase)
        self.snake_case_button.configure(fg='white')
        self.snake_case_button.grid(row=2, column=1, pady=10, padx=20)

        self.upper_case_button = tk.Button(self.button_frame, text="UPPER CASE", height=3, width=35,
                                           font=('Sofia Pro Regular Az.otf', 19), background='darkblue',
                                           command=self.uppercase)
        self.upper_case_button.configure(fg='white')
        self.upper_case_button.grid(row=2, column=2, pady=10, padx=20)

    def camelcase(self):
        initial_string = str(self.input_area.get("1.0", END))
        initial_list = [word for word in initial_string]
        for items in initial_list:
            ind = initial_list.index(items)
            if items == ' ' and ind == int(len(initial_list) - 1):
                break
            elif items == ' ':
                initial_list[ind] = ''
                initial_list[int(ind + 1)] = initial_list[int(ind + 1)].upper()
        output = ''.join(initial_list)
        self.output_area.delete(1.0, END)
        self.output_area.insert(1.0, output)

    def pascalcase(self):
        initial_string = str(self.input_area.get("1.0", END))
        initial_list = [word for word in initial_string]
        initial_list[0] = initial_list[0].upper()
        for items in initial_list:
            ind = initial_list.index(items)
            if items == ' ' and ind == int(len(initial_list) - 1):
                break
            elif items == ' ':
                initial_list[ind] = ''
                initial_list[int(ind + 1)] = initial_list[int(ind + 1)].upper()
        output = ''.join(initial_list)
        self.output_area.delete(1.0, END)
        self.output_area.insert(1.0, output)

    def titlecase(self):
        initial_string = str(self.input_area.get("1.0", END))
        initial_list = [word for word in initial_string]
        initial_list[0] = initial_list[0].upper()
        final_list = []
        for i in initial_list:
            final_list.append(i)

        final_list[0] = initial_list[0].upper()
        for items in initial_list:
            ind = initial_list.index(items)
            if items == "*":
                continue
            elif items == ' ' and ind == int(len(initial_list) - 1):
                break
            elif items == ' ':
                final_list[int(ind) + 1] = initial_list[int(ind) + 1].upper()
                # final_list = final_list.append(items)
                initial_list[ind] = '*'
        output = ''.join(final_list)
        self.output_area.delete(1.0, END)
        self.output_area.insert(1.0, output)

    def kebabCase(self):
        initial_string = str(self.input_area.get("1.0", END))
        initial_list = [word for word in initial_string]
        for items in initial_list:
            ind = initial_list.index(items)
            if items == ' ' and ind == int(len(initial_list) - 1):
                break
            elif items == ' ':
                initial_list[ind] = '-'
        output = ''.join(initial_list)
        self.output_area.delete(1.0, END)
        self.output_area.insert(1.0, output)

    def lowercase(self):
        initial_string = str(self.input_area.get("1.0", END))
        initial_list = [word for word in initial_string]
        for items in initial_list:
            ind = initial_list.index(items)
            initial_list[ind] = initial_list[ind].lower()
        output = ''.join(initial_list)
        self.output_area.delete(1.0, END)
        self.output_area.insert(1.0, output)

    def snakecase(self):
        initial_string = str(self.input_area.get("1.0", END))
        initial_list = [word for word in initial_string]
        for items in initial_list:
            ind = initial_list.index(items)
            if items == ' ' and ind == int(len(initial_list) - 1):
                break
            elif items == ' ':
                initial_list[ind] = '_'
        output = ''.join(initial_list)
        self.output_area.delete(1.0, END)
        self.output_area.insert(1.0, output)

    def uppercase(self):
        initial_string = str(self.input_area.get("1.0", END))
        initial_list = [word for word in initial_string]
        for word in initial_list:
            ind = initial_list.index(word)
            initial_list[ind] = initial_list[ind].capitalize()
        output = ''.join(initial_list)
        self.output_area.delete(1.0, END)
        self.output_area.insert(1.0, output)

    def sentencecase(self):
        initial_string = str(self.input_area.get("1.0", END))
        initial_list = [word for word in initial_string]
        final_list = []
        for i in initial_list:
            final_list.append(i)

        final_list[0] = initial_list[0].upper()
        for item in initial_list:
            test_ind = initial_list.index(item)
            if item == '*':
                continue
            elif test_ind <= len(initial_list) - int(1):
                if item == '.':
                    ind = int(initial_list.index(item) + 1)
                    if not initial_list[ind].isalpha():
                        ind += 1
                    final_list[ind] = final_list[ind].upper()
                initial_list[test_ind] = '*'
        output = (''.join(final_list))
        self.output_area.delete(1.0, END)
        self.output_area.insert(1.0, output)

    def alternativecase(self):
        initial_string = str(self.input_area.get("1.0", END))
        initial_list = [word for word in initial_string]
        final_list = []
        for i in initial_list:
            final_list.append(i)

        for items in initial_list:
            ind = initial_list.index(items)
            if items == '*':
                break
            elif ind % 2 == 0:
                final_list[ind] = initial_list[ind].upper()
                # initial_list[ind] = '*'
            elif ind % 2 != 0:
                final_list[ind] = initial_list[ind].lower()
            initial_list[ind] = '*'
        output = ''.join(final_list)
        self.output_area.delete(1.0, END)
        self.output_area.insert(1.0, output)


# main loop
if __name__ == '__main__':
    root = App()
    root.mainloop()
