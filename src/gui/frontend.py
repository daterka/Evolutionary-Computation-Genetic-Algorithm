# from tkinter import *
#
# window = Tk()
#
# row_0 = 0
# function_label = Label(window, text="~~~ Super-Hiper-Optimizer ~~~")
# function_label.grid(row=row_0, column=0, columnspan=8)
# function_label.config(font=("Courier", 14, "bold"))
#
# # function_text_input = StringVar()
# # function_entrance = Entry(window, textvariable = function_text_input)
# # function_entrance.grid(row=row_0+2, column=1)
#
# # args domains
# function_label = Label(window, text="FUNCTION AND ARGUMENTS")
# function_label.grid(row=row_0+2, column=0, columnspan=1)
# function_label.config(font=("Courier", 12, "bold"))
#
# # function
# function_label = Label(window, text="general form:")
# function_label.grid(row=row_0+3, column=0)
# function_label.config(font=("Courier", 12))
#
# function_form_label = Label(window, text="f(x)=sin(x1+x2)+(x1-x2)**2-1.5*x1+2.5*x2+1")
# function_form_label.grid(row=row_0+3, column=1, columnspan=2)
# function_form_label.config(font=("Courier", 12))
#
# # function_text_input = StringVar()
# # function_entrance = Entry(window, textvariable = function_text_input)
# # function_entrance.grid(row=1, column=1)
#
# # x1
# x1_domain_label = Label(window, text="x1 (touple: float, float):")
# x1_domain_label.grid(row=row_0+4, column=0)
# x1_domain_label.config(font=("Courier", 12))
#
# x1_domain_touple_input = StringVar()
# x1_domain_entrance = Entry(window, textvariable=x1_domain_touple_input)
# x1_domain_entrance.grid(row=row_0+4, column=1)
#
# # x2
# x2_domain_label = Label(window, text="x2 (touple: float, float):")
# x2_domain_label.grid(row=row_0+4, column=2)
# x2_domain_label.config(font=("Courier", 12))
#
# x2_domain_touple_input = StringVar()
# x2_domain_entrance = Entry(window, textvariable = x2_domain_touple_input)
# x2_domain_entrance.grid(row=row_0+4, column=3)
#
# # HIPERPARAMETERS
# hiperparams_header_label = Label(window, text="HIPER-PARAMETERS")
# hiperparams_header_label.grid(row=row_0+6, column=0, columnspan=1)
# hiperparams_header_label.config(font=("Courier", 12, "bold"))
#
# # epochs
# epochs_header_label = Label(window, text="EPOCHS:")
# epochs_header_label.grid(row=row_0+7, column=0, columnspan=1)
# epochs_header_label.config(font=("Courier", 12, "bold"))
#
# epochs_label = Label(window, text="epochs (int):")
# epochs_label.grid(row=row_0+8, column=0)
# epochs_label.config(font=("Courier", 12))
#
# epochs_number_input = StringVar()
# epochs_entrance = Entry(window, textvariable=epochs_number_input)
# epochs_entrance.grid(row=row_0+8, column=1)
#
# # population
# pop_header_label = Label(window, text="POPULATION SIZE:")
# pop_header_label.grid(row=row_0+9, column=0, columnspan=1)
# pop_header_label.config(font=("Courier", 12, "bold"))
#
# pop_size_label = Label(window, text="population size (int):")
# pop_size_label.grid(row=row_0+10, column=0)
# pop_size_label.config(font=("Courier", 12))
#
# pop_size_number_input = StringVar()
# pop_size_entrance = Entry(window, textvariable = pop_size_number_input)
# pop_size_entrance.grid(row=row_0+10, column=1)
#
# # survival rate
# sur_rate_header_label = Label(window, text="SURVIVAL RATE:")
# sur_rate_header_label.grid(row=row_0+11, column=0, columnspan=1)
# sur_rate_header_label.config(font=("Courier", 12, "bold"))
#
# survival_rate_label = Label(window, text="survival rate (float):")
# survival_rate_label.grid(row=row_0+12, column=0)
# survival_rate_label.config(font=("Courier", 12))
#
# survival_rate_number_input = StringVar()
# survival_rate_entrance = Entry(window, textvariable = survival_rate_number_input)
# survival_rate_entrance.grid(row=row_0+12, column=1)
#
# # precision
# precision_header_label = Label(window, text="PRECISION:")
# precision_header_label.grid(row=row_0+13, column=0, columnspan=1)
# precision_header_label.config(font=("Courier", 12, "bold"))
#
# precision_label = Label(window, text="precision (float):")
# precision_label.grid(row=row_0+14, column=0)
# precision_label.config(font=("Courier", 12))
#
# precision_number_input = StringVar()
# precision_entrance = Entry(window, textvariable = precision_number_input)
# precision_entrance.grid(row=row_0+14, column=1)
#
# # selection
# selection_header_label = Label(window, text="SELECTION:")
# selection_header_label.grid(row=row_0+15, column=0, columnspan=1)
# selection_header_label.config(font=("Courier", 12, "bold"))
#
# # type
# selection_label = Label(window, text="selection (integer):")
# selection_label.grid(row=row_0+16, column=0)
# selection_label.config(font=("Courier", 12))
#
# selection_type_number_input = StringVar()
# selection_entrance = Entry(window, textvariable = selection_type_number_input)
# selection_entrance.grid(row=row_0+16, column=1)
#
# # parameter trunc size / tournament group size
# selection_param_label = Label(window, text="selection parameter (float):")
# selection_param_label.grid(row=row_0+16, column=2)
# selection_param_label.config(font=("Courier", 12))
#
# selection_param_number_input = StringVar()
# selection_param_entrance = Entry(window, textvariable = selection_param_number_input)
# selection_param_entrance.grid(row=row_0+16, column=3)
#
# # crossover
# crossover_header_label = Label(window, text="CROSSOVER:")
# crossover_header_label.grid(row=row_0+17, column=0, columnspan=1)
# crossover_header_label.config(font=("Courier", 12, "bold"))
#
# # type
# crossover_label = Label(window, text="crossover type (int):")
# crossover_label.grid(row=row_0+18, column=0)
# crossover_label.config(font=("Courier", 12))
#
# crossover_type_number_input = StringVar()
# crossover_entrance = Entry(window, textvariable = crossover_type_number_input)
# crossover_entrance.grid(row=row_0+18, column=1)
#
# # parameter probability
# crossover_param_label = Label(window, text="crossover probability (float):")
# crossover_param_label.grid(row=row_0+18, column=2)
# crossover_param_label.config(font=("Courier", 12))
#
# crossover_param_number_input = StringVar()
# crossover_param_entrance = Entry(window, textvariable = crossover_param_number_input)
# crossover_param_entrance.grid(row=18, column=3)
#
# # mutation
# mutation_header_label = Label(window, text="MUTATION:")
# mutation_header_label.grid(row=19, column=0, columnspan=1)
# mutation_header_label.config(font=("Courier", 12, "bold"))
#
# # type
# mutation_label = Label(window, text="mutation type (int):")
# mutation_label.grid(row=20, column=0)
# mutation_label.config(font=("Courier", 12))
#
# mutation_number_input = StringVar()
# mutation_entrance = Entry(window, textvariable = mutation_number_input)
# mutation_entrance.grid(row=20, column=1)
#
# # parameters
# # probability
# mutation_param_label = Label(window, text="mutation probability (float):")
# mutation_param_label.grid(row=20, column=2)
# mutation_param_label.config(font=("Courier", 12))
#
# mutation_param_prob_number_input = StringVar()
# mutation_param_entrance = Entry(window, textvariable = mutation_param_prob_number_input)
# mutation_param_entrance.grid(row=20, column=3)
#
# # number of bits to mutate
# mutation_param_label = Label(window, text="bits to mutate (int):")
# mutation_param_label.grid(row=20, column=4)
# mutation_param_label.config(font=("Courier", 12))
#
# mutation_param_n_number_input = StringVar()
# mutation_param_entrance = Entry(window, textvariable = mutation_param_n_number_input)
# mutation_param_entrance.grid(row=20, column=5)
#
# padding_label = Label(window, text="")
# padding_label.grid(row=22, column=0)
# padding_label.config(font=("Courier", 12))
#
# optimize_button = Button(window, text='OPTIMIZE', width=15)
# optimize_button.grid(row=23, column=0)
# optimize_button.config(font=("Courier", 12, "bold"))
#
# padding_label = Label(window, text="")
# padding_label.grid(row=24, column=6)
# padding_label.config(font=("Courier", 12))
#
# result_label = Label(window, text="RESULT :")
# result_label.grid(row=25, column=0)
# result_label.config(font=("Courier", 12, "bold"))
#
# result_label = Label(window, text="123")
# result_label.grid(row=25, column=1)
# result_label.config(font=("Courier", 12))
#
#
#
# padding_label = Label(window, text="")
# padding_label.grid(row=26, column=6)
# padding_label.config(font=("Courier", 12))
#
#
# window.mainloop()
#
# Spinbox2 = tk.Spinbox(Frame6, from_=1.0, to=5)
# Spinbox2.place(relx=0.198, rely=0.219, relheight=0.155
#         , relwidth=0.297)
# Spinbox2.configure(activebackground="#f9f9f9")
# Spinbox2.configure(background="white")
# Spinbox2.configure(buttonbackground="#d9d9d9")
# Spinbox2.configure(disabledforeground="#a3a3a3")
# Spinbox2.configure(font="TkDefaultFont")
# Spinbox2.configure(foreground="black")
# Spinbox2.configure(highlightbackground="black")
# Spinbox2.configure(highlightcolor="black")
# Spinbox2.configure(insertbackground="black")
# Spinbox2.configure(selectbackground="#c4c4c4")
# Spinbox2.configure(selectforeground="black")
# Spinbox2.configure(textvariable=ga_gui_support.spinbox)
# value_list = ['cccccccccc ','bbbbbbbbbbbb','aaaaaaaaaaa',]
# Spinbox2.configure(values=value_list)
#
# Spinbox1_12 = tk.Spinbox(Frame6, from_=1.0, to=100.0)
# Spinbox1_12.place(relx=0.198, rely=0.4, relheight=0.155
#         , relwidth=0.297)
# Spinbox1_12.configure(activebackground="#f9f9f9")
# Spinbox1_12.configure(background="white")
# Spinbox1_12.configure(buttonbackground="#d9d9d9")
# Spinbox1_12.configure(disabledforeground="#a3a3a3")
# Spinbox1_12.configure(font="TkDefaultFont")
# Spinbox1_12.configure(foreground="black")
# Spinbox1_12.configure(highlightbackground="black")
# Spinbox1_12.configure(highlightcolor="black")
# Spinbox1_12.configure(insertbackground="black")
# Spinbox1_12.configure(selectbackground="#c4c4c4")
# Spinbox1_12.configure(selectforeground="black")
# Spinbox1_12.configure(textvariable=ga_gui_support.spinbox)
# value_list = ['dddddddddd ','eeeeeeeeeeeeee','ffffffff',]
# Spinbox1_12.configure(values=self.value_list)
