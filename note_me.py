import tkinter as tk
from tkinter import Frame, Grid, Image, PhotoImage, Scrollbar, Text, ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
from tkinter.constants import BOTTOM, FALSE, NONE, TOP, TRUE


main_swasher=tk.Tk()
main_swasher.geometry('1200x900')
main_swasher.title("NOTE_ME")

#"note_me\\atomwriter icon\\new .png"
#**************part1*********
main_menu=tk.Menu()
#**************part1*********
#images taken for file menu
'''
new_img_data=b'iVBORw0KGgoAAAANSUhEUgAAACEAAAAhCAYAAABX5MJvAAAEkElEQVRYR72XWYiNYRjHfx9jJGS5sJOxZ99Sliwh2YbIGNuFC7kQWYoImYkQspQbkqUISXaKCVku7MzYIhmmIYzGLoxP//Ocb84548yZ75wxnjp1vnPe9//+32f5P8/nuK7r4tfev4fp06FlS5g9G1JSQjufPYMtWyA3F3buhNq1/aLi+Cbx+zeMGQMnThh4lSqQlgYTJ8LBg3DgAPz8af+NHg1HjkClSr6I+Cexbh0sXOgLNLBo1SpYssTX+ugk8vLg/Hn4+hU+f4a3b2HjRvjxwxdosafmzIEGDaB6dahRAwYNgiZN/sKITkKLL1zwf6Dflf37w8WLPkgUFUHduvDxo19o/+tq1gQld1JSxJ6/PaHsbt7cP3C8K1VF4VUFUarjzBkYPjxeaP/rT56EESNK8YTkQgQWLICHD/2DxruyXTvYsMEu6jiB3RaO589BmSwNiEO74j2/eL0OHznSxC0lBcctKnJp3Bhev04YM+GN9epBfn7QE126wL17CWMlvLFjR8jODpLIyIAVKwxL5TNlignUqVP2W8OGFsMrVyxc/fpFnqswDh1qUr5vn4maBEqy/vgxXL1q6wcMgBYtLOzCX74cMjKCJHJyoHNnO0CbP30C9YqBA+HyZdss8Zoxw37fsQPevQNpiiw1FdautfW9esH16zBhgvWUmzehZ09bd+MG6Pa6VGEh3L0LnToFSajxNGpkwB4JJY/ICaB7d7tNOAlpiTTFs0WLYM0amDcPNm2CvXth8mQjqq774YPdXt4UWQniq1eQnBwkoU3aLPNIXLtmt1q2DFTbt29HkhBBr2uOGwd16sCtW3DokB3+5o2pbrNmMHMmvHgBp09bU1u92s5Sqc6fj+Pm5roBFykE4STWr4e2bWHIEBg/3gDCPbFrV2iPOmZBgXlG4dLMcfYsTJsG27aZ/ty/D0uXQrducOeOnaWmlpOD46anu+zfH3Kr54nNm62OVTWPHllYYoVDCHv2wNSpcPiwJapif/w4dO0KDx5YUjZtakQ9S0vDcfv2dQNx8swjsXWrTU9erPV/OIk2bczFMoEqNAqDckHPSspJk2DuXBsDlPS7d5uXwq13bxw3L89l8GArpfBwbN9usaxaFZQfqp5wEpo1PHU9dswIaHZ4+dLKfOxYOHoUWrUybE1Z6ek2gXmmcGdlBRMzP99ir54hAMXyyRMrT5n0vk+f0nVCuZCVZWuVP7VqmV58/279QR4RrkY+b0QQ5rlzSK1DrVxAYv3rV6S7KuKpcmV4+rR4ZAiRUO+QVvyPBqaLyftK3Ih5QtnboUNF3Ds6Zna2qWcEiUuXQDPg/zIN0lLOCBKeFnz5UvE0JAOquPbtS5DQo/JCyiiZVraryfwrU8VICkaNsvGufv1i5NJffr59M6aauspr6h/ydLVqUZFiv4GpKy5eXF4KZb6NxSahTii9L0+eKP4a8zXKlWJlv4uqd6iPtG5tc0WPHtYhpX4lTS/Mw4bZIKOPVHfWLBt4YljZJLRZ41pycghGDWrlSsjMtKFFCqi5Q61a3z0ruS9hT8S6gmbQ4GASGOETtD8aPjJkKEiX5QAAAABJRU5ErkJggg=='
pic=new_img_data#GIF decoded to string. imageString from myimages.py
render = PhotoImage(data=pic)
#myLabel.config(image=render)
'''
#new_icon=PhotoImage(file="note_me\\atomwriter icon\\\new .png")
new_icon=PhotoImage(file="atomwriter icon/new.png")
open_icon=PhotoImage(file="atomwriter icon/open .png")
save_icon=PhotoImage(file="atomwriter icon/save .png")
save_as_icon=PhotoImage(file="atomwriter icon/saveas .png")
exit_icon=tk.PhotoImage(file="atomwriter icon/exit .png")
#code for file menu
#new button functionality
data_main=""
def new_main_func(event=None):
    global data_main
    data_main=""
    text_editor_main.delete(1.0,tk.END)
    
file=tk.Menu(main_menu,tearoff=False)
file.add_command(label="New",image=new_icon,compound=tk.LEFT,accelerator="ctrl+N",command=new_main_func)

'''
def open_file_main(event=None):#open file functionality
    global data_main
    data_main=filedialog.askopenfilenames(initialdir=os.getcwd(),title="select your file",filetypes=(("Text files","*.txt"),("All files","*.*")))
    try:
        with open(data_main,"r") as openfile1:
            text_editor_main.delete(1.0,tk.END)
            text_editor_main.insert(1.0,openfile1.read())
    except FileNotFoundError:
        return
    except:
        return
    main_swasher.title(os.path.basename(data_main))
'''

def open_file_main(event=None):#open file functionality
    global data_main 
    data_main = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(data_main, 'r') as fr:
            text_editor_main.delete(1.0, tk.END)
            text_editor_main.insert(1.0, fr.read())
    except FileNotFoundError:
        return 
    except:
        return 
    main_swasher.title(os.path.basename(data_main))
file.add_command(label="open",image=open_icon,compound=tk.LEFT,accelerator="ctrl+o",command=open_file_main)
#save file functionality
def save_file_main(event=None):
    global data_main
    try:
        if data_main:
            writtendata=str(text_editor_main.get(1.0,tk.END))
            with open(data_main,"w",encoding="utf-8") as file3:
                file3.write(writtendata)
        else:
            data_main=filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=(("Text files","*.txt"),("All files","*.*")))
            writtendata2=text_editor_main.get(1.0,tk.END)
            data_main.write(writtendata2)
            data_main.close()
    except:
        return
file.add_command(label="save",image=save_icon,compound=tk.LEFT,accelerator="ctrl+s",command=save_file_main)
def save_as_main(event=NONE):
    global data_main
    try:
        if data_main:
            data_main=filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=(("Text files","*.txt"),("All files","*.*")))
            writtendata2=text_editor_main.get(1.0,tk.END)
            data_main.write(writtendata2)
            data_main.close()
    except:
        return
file.add_command(label="save as",image=save_as_icon,compound=tk.LEFT,accelerator="ctrl+alt+s",command=save_as_main)
text_changed=True
def exit_func(event=None):
    global data_main, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if data_main:
                    content = text_editor_main.get(1.0, tk.END)
                    with open(data_main, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_swasher.destroy()
                else:
                    content2 = str(text_editor_main.get(1.0, tk.END))
                    data_main = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    data_main.write(content2)
                    data_main.close()
                    main_swasher.destroy()
            elif mbox is False:
                main_swasher.destroy()
        else:
            main_swasher.destroy()
    except:
        return 
file.add_command(label="exit",image=exit_icon,compound=tk.LEFT,accelerator="ctrl+d",command=exit_func)

#images for edit menu
copy_icon=PhotoImage(file="atomwriter icon/copy.png")
paste_icon=PhotoImage(file="atomwriter icon/paste.png")
cut_icon=PhotoImage(file="atomwriter icon/cut.png")
clear_all_icon=PhotoImage(file="atomwriter icon/clear.png")
find_icon=PhotoImage(file="atomwriter icon/find.png")
#code for edit menu
edit=tk.Menu(main_menu,tearoff=False)

edit.add_command(label="copy",image=copy_icon,compound=tk.LEFT,accelerator="ctrl+c",command=lambda:text_editor_main.event_generate("<Control c>"))
edit.add_command(label="paste",image=paste_icon,compound=tk.LEFT,accelerator="ctrl+v",command=lambda:text_editor_main.event_generate("<Control v>"))
edit.add_command(label="cut",image=cut_icon,compound=tk.LEFT,accelerator="ctrl+x",command=lambda:text_editor_main.event_generate("<Control x>"))
edit.add_command(label="clear all",image=clear_all_icon,compound=tk.LEFT,accelerator="ctrl+Alt+x",command=lambda:text_editor_main.delete(1.0,tk.END))


def finding_main(event=None):
    def find():
        word_main=find_input.get()
        text_editor_main.tag_remove("match","1.0",tk.END)
        matching=0
        if word_main:
            starting_position="1.0"
            while True:
                starting_position=text_editor_main.search(word_main,starting_position,stopindex=tk.END)
                if not starting_position:
                    break
                ending_position=f'{starting_position}+{len(word_main)}c'
                text_editor_main.tag_add("match",starting_position,ending_position)
                matching+=1
                starting_position=ending_position
                text_editor_main.tag_config("match",foreground="yellow",background="blue")
    def replace():
        word_main=find_input.get()
        replace_main=replace_input.get()
        replacig_bash=text_editor_main.get(1.0,tk.END)
        new_replacing_bash=replacig_bash.replace(word_main,replace_main)
        text_editor_main.delete(1.0,tk.END)
        text_editor_main.insert(1.0,new_replacing_bash)
    main_swasher2=tk.Toplevel()
    main_swasher2.geometry("450x250+500+200")
    main_swasher2.title("find_&_Replace")
    main_swasher2.resizable(0,0)
    dancing_frame=ttk.LabelFrame(main_swasher2,text="find_replace")
    dancing_frame.pack(pady=20)
    text_find_lebal=ttk.Label(dancing_frame,text="find")
    text_find_lebal.grid(row=0,column=0,padx=4,pady=4)
    text_replce_lebal=ttk.Label(dancing_frame,text="replce")
    text_replce_lebal.grid(row=1,column=0,padx=4,pady=4)
    find_input = ttk.Entry(dancing_frame, width=20)
    replace_input = ttk.Entry(dancing_frame, width=20)
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)
    find_button = ttk.Button(dancing_frame, text='Find',command=find)
    replace_button = ttk.Button(dancing_frame, text= 'Replace',command=replace)
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)
    main_swasher2.mainloop()
edit.add_command(label="find",image=find_icon,compound=tk.LEFT,accelerator="ctrl+f",command=finding_main)

#imort images for view
toolbar_icon=PhotoImage(file="atomwriter icon/toolbar.png")
statusbar_icon=PhotoImage(file="atomwriter icon/statusbar.png")
#code for view
view=tk.Menu(main_menu,tearoff=False)
#show_toolbar=tk.BooleanVar()
#show_toolbar=tk.set(True)
#show_statuabar=tk.BooleanVar()
#show_statuabar=tk.set(True)
#show_statusbar = tk.BooleanVar()
#show_statusbar.set(True)



show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False 
    else :
        text_editor_main.pack_forget()
        status_bar_main.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor_main.pack(fill=tk.BOTH, expand=True)
        status_bar_main.pack(side=tk.BOTTOM)
        show_toolbar = True 

view.add_checkbutton(label="tool bar",offvalue=0,onvalue=True,variable=show_toolbar,image=toolbar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label="status bar",offvalue=False,onvalue=1,image=statusbar_icon,compound=tk.LEFT)

#color theme
light_default=PhotoImage(file="atomwriter icon/light.png")
light_pulse=PhotoImage(file="atomwriter icon/lightpulse.png")
dark_pulse=PhotoImage(file="atomwriter icon/dark.png")
red_pulse=PhotoImage(file="atomwriter icon/red.png")
blue_pulse=PhotoImage(file="atomwriter icon/blue.png")
yellow_pulse=PhotoImage(file="atomwriter icon/yellow.png")
colour_theme_data=tk.StringVar()
colour_theme=tk.Menu(main_menu,tearoff=False)
icon_shift=[light_default,light_pulse,dark_pulse,red_pulse,blue_pulse,yellow_pulse]
color_dict = {
    'light_default ' : ('#000000', '#ffffff'),
    'light_pulse' : ('#474747', '#e0e0e0'),
    'dark_pulse' : ('#c4c4c4', '#2d2d2d'),
    'red_pulse' : ('#2d2d2d', '#ffe8e8'),
    'yellow_pulse' : ('#474747', '#d3b774'),
    'blue_pulse' :('#ededed', '#6b9dc2')
}
def change_theme():
    chosen_theme = colour_theme_data.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor_main.config(background=bg_color, fg=fg_color) 
counter=0
for i in color_dict:
    colour_theme.add_radiobutton(label=i,image=icon_shift[counter],variable=colour_theme_data,compound=tk.LEFT,command=change_theme)
    counter+=1


#all cascade
main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="edit",menu=edit)
main_menu.add_cascade(label="view",menu=view)
main_menu.add_cascade(label="colour theme",menu=colour_theme)
main_swasher.config(menu=main_menu)
#*************************************part2------->fontbox,sizebox,boldbutton,italic button,underline button,fontcolor button
#**fontset,leftalign button,centeraligh button,rightalign button ---->all mounted on status bar

tool_bar=ttk.Label(main_swasher)
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_set=tk.font.families()
font_save=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_save,state="readonly")
font_box["values"]=font_set
font_box.current(font_set.index('Arial'))
font_box.grid(column=0,row=0,pady=5)#padx is to move right with desired value to move



#size box
size_box_data=tk.IntVar()
size_box_area=ttk.Combobox(tool_bar,width=20,textvariable=size_box_data,state="readonly")
size_box_area["value"]=list(range(4,200,2))
size_box_area.grid(column=1,row=0,padx=5)
#bold button
bold_icon=PhotoImage(file="atomwriter icon/bold.png")
bold_button=ttk.Button(tool_bar,image=bold_icon)
bold_button.grid(column=2,row=0,pady=5)
#italic button
italic_icon=PhotoImage(file="atomwriter icon/italic.png")
italic_button=ttk.Button(tool_bar,image=italic_icon)
italic_button.grid(column=3,row=0,pady=5)
#underline button
underline_icon=PhotoImage(file="atomwriter icon/underline.png")
underline_button=ttk.Button(tool_bar,image=underline_icon)
underline_button.grid(column=4,row=0,pady=5)
#fontcolor button
fontcolor_icon=PhotoImage(file="atomwriter icon/colour.png")
fontcolor_button=ttk.Button(tool_bar,image=fontcolor_icon)
fontcolor_button.grid(column=5,row=0,pady=5)
#leftalign button
left_icon=PhotoImage(file="atomwriter icon/left.png")
left_button=ttk.Button(tool_bar,image=left_icon)
left_button.grid(column=6,row=0,pady=5)
#centeralign button
center_icon=PhotoImage(file="atomwriter icon/center.png")
center_button=ttk.Button(tool_bar,image=center_icon)
center_button.grid(column=7,row=0,pady=5)
#rightalign button
right_icon=PhotoImage(file="atomwriter icon/right.png")
right_button=ttk.Button(tool_bar,image=right_icon)
right_button.grid(column=8,row=0,pady=5)

#*****************part3---------->text editor**************


#text editor and scroll bar
text_editor_main=tk.Text(main_swasher)
text_editor_main.config(wrap="word",relief=tk.FLAT)

Scrollbar_main=Scrollbar(main_swasher)
text_editor_main.focus_set()
Scrollbar_main.pack(side=tk.RIGHT,fill=tk.Y)
text_editor_main.pack(fill=tk.BOTH,expand=TRUE)
Scrollbar_main.config(command=text_editor_main.yview)
text_editor_main.config(yscrollcommand=Scrollbar_main.set)
#font bindining
current_font_data="Arial"
current_font_size_data=14
#func for font type
def font_jump(main_swasher):
    global current_font_data
    current_font_data=font_save.get()
    text_editor_main.configure(font=(current_font_data,current_font_size_data))
font_box.bind("<<ComboboxSelected>>", font_jump)
#func for font size and fuctionality
def font_size_jump(main_swasher):
    global current_font_size_data
    current_font_size_data=size_box_data.get()
    text_editor_main.configure(font=(current_font_data,current_font_size_data))
size_box_area.bind("<<ComboboxSelected>>", font_size_jump)
     
text_editor_main.configure(font=("Arial",14))# it will print by default data in arialand size will be 14
#for bold button
'''
this print statement will print the output as below list 
print(tk.font.Font(font=text_editor_main["font"]).actual())
output={'family': 'Arial', 'size': 14, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
and for bold button we need to access the weight element of list,similarly u caon use slant for italic and underline 
for making underline text 
'''
def bold_making():
    bold_texting=tk.font.Font(font=text_editor_main["font"])
    if bold_texting.actual()["weight"]=="normal":
        text_editor_main.configure(font=(current_font_data,current_font_size_data,"bold"))
    if bold_texting.actual()["weight"]=="bold":
        text_editor_main.configure(font=(current_font_data,current_font_size_data,"normal"))    
bold_button.configure(command=bold_making)
#for italic button
def italic_making():
    italic_texting=tk.font.Font(font=text_editor_main["font"])
    if italic_texting.actual()["slant"]=="roman":
        text_editor_main.configure(font=(current_font_data,current_font_size_data,"italic"))
    if italic_texting.actual()["slant"]=="italic":
        text_editor_main.configure(font=(current_font_data,current_font_size_data,"normal"))    
italic_button.configure(command=italic_making)

#for underline button
def underline_making():
    underline_texting=tk.font.Font(font=text_editor_main["font"])
    if underline_texting.actual()["underline"]==0:
        text_editor_main.configure(font=(current_font_data,current_font_size_data,"underline"))
    if underline_texting.actual()["underline"]==1:
        text_editor_main.configure(font=(current_font_data,current_font_size_data,"normal"))    
underline_button.configure(command=underline_making)

#for font color of text
def font_text_color_making():
    font_text_color_data=tk.colorchooser.askcolor()
    text_editor_main.configure(fg=font_text_color_data[1])
fontcolor_button.configure(command=font_text_color_making)

#left alignment
def left_text_alignment_making():
    main_text_data=text_editor_main.get(1.0,"end")
    text_editor_main.tag_config("left",justify=tk.LEFT)
    text_editor_main.delete(1.0,tk.END)
    text_editor_main.insert(tk.INSERT,main_text_data,"left")
left_button.configure(command=left_text_alignment_making)

#center alignment
def center_text_alignment_making():
    main_text_data=text_editor_main.get(1.0,"end")
    text_editor_main.tag_config("center",justify=tk.CENTER)
    text_editor_main.delete(1.0,tk.END)
    text_editor_main.insert(tk.INSERT,main_text_data,"center")
center_button.configure(command=center_text_alignment_making)
#right alignment
def right_text_alignment_making():
    main_text_data=text_editor_main.get(1.0,"end")
    text_editor_main.tag_config("right",justify=tk.RIGHT)
    text_editor_main.delete(1.0,tk.END)
    text_editor_main.insert(tk.INSERT,main_text_data,"right")
right_button.configure(command=right_text_alignment_making)
#status bar
status_bar_main=ttk.Label(main_swasher,text="status bar")
status_bar_main.pack(side=tk.BOTTOM)
'''
#status bar
status_bar_main=ttk.Label(main_swasher,text="status bar")
status_bar_main.pack(side=tk.BOTTOM)
text_edited=FALSE
zippy=[]
def status_bar_counter():
    
 
    word_count=len(text_editor_main.get(1.0,"end-1c").split())
    charecter_count=len(text_editor_main.get(1.0,"end-1c"))
    for i in text_editor_main:
        if keyboard.is_pressed():
            zippy.append(i)

        
            status_bar_main.config(text=zippy)
        


text_editor_main.bind("<<Modified>>",status_bar_counter())
'''  
'''
#worked
text_edited=FALSE
def status_bar_counter(event=None):

    if text_editor_main.edit_modified:
        text_edited=True
        word_count=len(text_editor_main.get(1.0,"end-1c").split())
        charecter_count=len(text_editor_main.get(1.0,"end-1c"))
        status_bar_main.config(text="no of charecters"+str(word_count))
    text_editor_main.edit_modified(False)


text_editor_main.bind("<<Modified>>",status_bar_counter())
'''


'''
def show(key):
  
    
    status_bar_counter()
    
        # Stop listener
    return 0
  
# Collect all event until released
with Listener(on_press = show) as listener:   
    listener.join()
'''


'''
def status_bar_counter(event=None):
    if text_editor_main.edit_modified():
        word_count=len(text_editor_main.get(1.0,"end-1c").split())
        charecter_count=len(text_editor_main.get(1.0,"end-1c"))
        status_bar_main=ttk.Label(main_swasher,text="status bar")
        status_bar_main.pack(side=tk.BOTTOM)
        #status_bar_main.config(text=f'charecter:{charecter_count}' 'words:{word_count}')
'''
#text_editor_main.bind("<<Modified>>",status_bar_counter)
'''
status_bar_main=ttk.Label(main_swasher,text="status bar")
status_bar_main.pack(side=tk.BOTTOM)
def status_bar_counter():
    if text_editor_main.edit_modified():
        word_count=len(text_editor_main.get(1.0,"end-1c").split())
        charecter_count=len(text_editor_main.get(1.0,"end-1c"))
        status_bar_main.config(text="mandjdskdndj")
        #status_bar_main.config(text=f'charecter:{charecter_count}' 'words:{word_count}')

text_editor_main.bind("<<Modified>>",status_bar_counter)
'''
text_editor_main.bind("<Control-n>", new_main_func)
text_editor_main.bind("<Control-o>", open_file_main)
text_editor_main.bind("<Control-s>", save_file_main)
text_editor_main.bind("<Control-Alt-s>", save_as_main)
text_editor_main.bind("<Control-q>", exit_func)
text_editor_main.bind("<Control-f>", finding_main)

main_swasher.mainloop()