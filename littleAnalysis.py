"""
OPTIONS TO PICK FROM
1 - Firstname
2 - Surname
3 - Gender
4 - Age
5 - English
6 - Mathematics
7 - Sciences
8 - Database Management
"""
import matplotlib.pyplot as plt
import time
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats as st
sns.set()


def selected_column_view(x):
    s_data = info[x]
    print(s_data.to_markdown(index=False))


def mean_of_selected(arg):
    try:
        selected = info[arg]
        x = np.mean(selected)
        return f"Mean of {arg} is {x}"
    except KeyError:
        print("Wrong Input")
    except NameError:
        print('Variable does not exist')
    except KeyboardInterrupt:
        print("Program Stopped!!")


def mode_of_selected(arg):
    mode = info[arg]
    mode_age = np.array(mode)
    return f"The most occurring figure in {arg} is '{st.mode(mode_age, keepdims=True)[0][0]}' " \
           f"with the frequency of '{st.mode(mode_age, keepdims=True)[1][0]}'"


def plot_columns(arg):
    return sns.countplot(x=arg, data=info, edgecolor='black')


def mean_condition(mean_input):
    if mean_input == 1:
        return mean_of_selected('Age')
    elif mean_input == 2:
        return mean_of_selected('English')
    elif mean_input == 3:
        return mean_of_selected('Mathematics')
    elif mean_input == 4:
        return mean_of_selected('Sciences')
    elif mean_input == 5:
        return mean_of_selected('Database_Management')
    else:
        return "Wrong Input!!!"


def mode_condition(mode_input):
    if mode_input == 1:
        return mode_of_selected('Age')
    elif mode_input == 2:
        return mode_of_selected('English')
    elif mode_input == 3:
        return mode_of_selected('Mathematics')
    elif mode_input == 4:
        return mode_of_selected('Sciences')
    elif mode_input == 5:
        return mode_of_selected('Database_Management')
    else:
        return "Wrong Input!!!"


def view_complete_dataset():
    return info.to_markdown(index=False)


def selection_filter():
    for i in range(len(columns[1:])):
        print(f"{lst_short[i]} -- {columns[1:][i]}")
    f_con = int(input("\nPick a number that represents a column?\n-> "))
    if f_con == 1:
        f_con = "Firstname"
    elif f_con == 2:
        f_con = "Surname"
    elif f_con == 3:
        f_con = "Gender"
    elif f_con == 4:
        f_con = "Age"
    elif f_con == 5:
        f_con = "English"
    elif f_con == 6:
        f_con = "Mathematics"
    elif f_con == 7:
        f_con = "Sciences"
    elif f_con == 8:
        f_con = "Database_Management"
    print(f_con)

    ask_ = int(input("What do you want to do?\n1 -- Greater than ('>')\n"
                     "2 -- Less than ('<')\n3 -- Less than equal to ('<=')\n"
                     "4 -- Greater than equal to ('>=')\n5 -- Equal to ('==')\n-> ").lower())
    if ask_ == 1:
        ask_ = '>'
    elif ask_ == 2:
        ask_ = '<'
    elif ask_ == 3:
        ask_ = '<='
    elif ask_ == 4:
        ask_ = '>='
    elif ask_ == 5:
        ask_ = '=='
    print(ask_)

    first_elemen = input("Enter element query\n-> : ").title()
    return f_con, ask_, first_elemen


"""
SUBJECTS: MATHS, ENGLISH, SCIENCES, DATABASE
"""
d_f_nam = ['Emmanuel', 'Micheal', 'Miracle', 'Rachel', 'Esther', 'Adele', 'David']
d_s_nam = ['Bush', 'Gates', 'Bill', 'Jonathan', 'Daniel', 'DeeJay', 'Love']
d_age = [i for i in range(25, 70)]
d_sex = ['Female', 'Male']
d_score = [i for i in range(20, 99)]
lst_short = [i for i in range(1, 11)]
# CREATING THE RANDOM DATA
first_name = np.random.choice(d_f_nam, size=100)
surname = np.random.choice(d_s_nam, size=100)
age = np.random.choice(d_age, size=100)
sex = np.random.choice(d_sex, size=100)
eng = np.random.choice(d_score, size=100)
math = np.random.choice(d_score, size=100)
sci = np.random.choice(d_score, size=100)
dbms = np.random.choice(d_score, size=100)
num = [i for i in range(1, 101)]
# ASSIGNING THE RANDOM DATA TO THE DATAFRAME
data = {
    'S/N': num,
    'Firstname': first_name,
    'Surname': surname,
    'Gender': sex,
    'Age': age,
    'English': eng,
    'Mathematics': math,
    'Sciences': sci,
    'Database_Management': dbms
}
info = pd.DataFrame(data)
columns = list(info.columns)

selection = ""

""""""
while selection != 000:
    selection = int(input(("""
Welcome to the data analysis corner!!!
 - Press '000' to quit!!!
 - To view the complete DataFrame : Press 1
 - To View all the columns of the Data Set : Press 2
 - To view selected columns in the DataFrame: Press 3
 - To filter the table based on specific data in columns : Press 4
 - To View the mean of a selected Data Set : Press 5
 - To View the mode of a selected Data Set : Press 6
 - To plot a barchart of a selected column against its frequency : Press 7
    -> """)))
    if selection == 1:
        print(f"\nComplete Dataset!!!!\n{view_complete_dataset()}")
        time.sleep(5)
    elif selection == 2:
        df = info.columns
        print("Complete Columns in Dataset")
        for i in range(len(df)):
            print(f"{i+1} --- {df[i]}")
            time.sleep(1)
        print('\nComplete columns shown')
    elif selection == 3:
        e_lst = []
        c = ""
        co = info.columns
        print(co[1:])
        while c == "":
            col = input("Enter a column\n-> ").title()
            e_lst.append(col)
            c = input("Hit 'Enter' to enter another value")

        selected_column_view(e_lst)
    elif selection == 4:
        condi = int(input("How many conditions are in your filtering?\n-> "))
        if condi == 1:
            select_a = selection_filter()
            print(f'{select_a[0]} {select_a[1]} {select_a[2]}')
            if select_a[2].isdigit():
                fil_selct = info.query("{0} {1} {2}"
                                       .format(select_a[0], select_a[1], select_a[2])).to_string(index=False)
            else:
                fil_selct = info.query("{0} {1} '{2}'"
                                       .format(select_a[0], select_a[1], select_a[2])).to_string(index=False)
            print(fil_selct)
            time.sleep(5)
        elif condi == 2:
            select_1 = selection_filter()
            print(f'{select_1[0]}, {select_1[1]}, {select_1[2]}')
            select_2 = selection_filter()
            print(f'{select_2[0]}, {select_2[1]}, {select_2[2]}')

            if select_1[2].isdigit() and select_2[2].isalpha():
                fil_selct = info.query("{0} {1} {2} and {3} {4} '{5}'".format(select_1[0], select_1[1], select_1[2],
                                                                              select_2[0], select_2[1],
                                                                              select_2[2])).to_string(index=False)
            elif select_2[2].isdigit() and select_1[2].isalpha():
                fil_selct = info.query("{0} {1} '{2}' and {3} {4} {5}".format(select_1[0], select_1[1], select_1[2],
                                                                              select_2[0], select_2[1],
                                                                              select_2[2])).to_string(index=False)
            elif select_1[2].isdigit() and select_2[2].isdigit():
                fil_selct = info.query("{0} {1} {2} and {3} {4} {5}".format(select_1[0], select_1[1], select_1[2],
                                                                            select_2[0], select_2[1],
                                                                            select_2[2])).to_string(index=False)
            else:
                fil_selct = info.query("{0} {1} '{2}' and {3} {4} '{5}'".format(select_1[0], select_1[1], select_1[2],
                                                                                select_2[0], select_2[1],
                                                                                select_2[2])).to_string(index=False)
            print(fil_selct)
            time.sleep(5)
    elif selection == 5:
        for i in range(len(columns[4:])):
            print(f"{i+1} ---- {columns[4:][i]}")
        meanInput = int(input('Mean of which of the above data-set\n-> '))
        meanCondition = mean_condition(meanInput)
        print(meanCondition)
        time.sleep(5)
    elif selection == 6:
        for i in range(len(columns[4:])):
            print(f"{i+1} ---- {columns[4:][i]}")
        modeInput = int(input('Mode of which of the above data-set\n-> '))
        modeCondition = mode_condition(modeInput)
        print(modeCondition)
        time.sleep(5)
    elif selection == 7:
        for i in range(len(columns[1:])):
            print(f"{i + 1} -- {columns[1:][i]}")
        pick = 0
        while pick != 9:
            pick = int(input("Please select a column to plot\nPress 9 to quit\n-> "))
            if pick == 1:
                plot_columns("Firstname")
                plt.show()
            elif pick == 2:
                plot_columns("Surname")
                plt.show()
            elif pick == 3:
                plot_columns("Gender")
                plt.show()
            elif pick == 4:
                plot_columns("Age")
                plt.show()
            elif pick == 5:
                plot_columns("English")
                plt.show()
            elif pick == 6:
                plot_columns("Mathematics")
                plt.show()
            elif pick == 7:
                plot_columns("Sciences")
                plt.show()
            elif pick == 8:
                plot_columns("Database_Management")
                plt.show()
            else:
                print('Selection not noted.')
                break
else:
    print('Thank you for visiting my little analysis portal')
