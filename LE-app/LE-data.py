from tkinter import *
import json
import csv
import os
import subprocess

root = Tk()
root.title("Lymphedema App")
root.geometry("400x650")

logo = PhotoImage(file="logo.png")
root.iconphoto(False, logo)

def saveBeforeData():

    global entry_weight, entry_claw, entry_ankle, above_ankle_entry, below_knee_entry, knee_entry, above_knee_1_entry, above_knee_entry_2
    
    entry_weight_data = entry_weight.get()
    entry_claw_data = entry_claw.get()
    entry_ankle_data = entry_ankle.get()
    above_ankle_entry_data = above_ankle_entry.get()
    below_knee_entry_data = below_knee_entry.get()
    knee_entry_data = knee_entry.get()
    above_knee_1_entry_data = above_knee_1_entry.get()
    above_knee_2_entry_data = above_knee_entry_2.get()
    
    with open('LE-data.json', 'r') as file:
        data = json.load(file)
        data[0]['weight_before'] = entry_weight_data
        data[0]['claw_before'] = entry_claw_data
        data[0]['ankle_before'] = entry_ankle_data
        data[0]['above_ankle_before'] = above_ankle_entry_data
        data[0]['below_knee_before'] = below_knee_entry_data
        data[0]['knee_before'] = knee_entry_data
        data[0]['above_knee_1_before'] = above_knee_1_entry_data
        data[0]['above_knee_2_before'] = above_knee_2_entry_data

    file.close()

    with open('LE-data.json', 'w') as file:
        json.dump(data, file)

    file.close()

def loadData():

    global entry_weight, entry_claw, entry_ankle, above_ankle_entry, below_knee_entry, knee_entry, above_knee_1_entry, above_knee_entry_2

    with open('LE-data.json', 'r') as file:
        data = json.load(file)

    file.close()

    entry_weight.insert(0,data[0]['weight_before'])
    entry_claw.insert(0, data[0]['claw_before'])
    entry_ankle.insert(0, data[0]['ankle_before'])
    above_ankle_entry.insert(0, data[0]['above_ankle_before'])
    below_knee_entry.insert(0, data[0]['below_knee_before'])
    knee_entry.insert(0, data[0]['knee_before'])
    above_knee_1_entry.insert(0, data[0]['above_knee_1_before'])
    above_knee_entry_2.insert(0, data[0]['above_knee_2_before'])

def clearEntry():

    global entry_weight, entry_claw, entry_ankle, above_ankle_entry, below_knee_entry, knee_entry, above_knee_1_entry, above_knee_entry_2

    with open('LE-data.json', 'r') as file:
        data = json.load(file)
        data[0]['weight_before'] = ""
        data[0]['claw_before'] = ""
        data[0]['ankle_before'] = ""
        data[0]['above_ankle_before'] = ""
        data[0]['below_knee_before'] = ""
        data[0]['knee_before'] = ""
        data[0]['above_knee_1_before'] = ""
        data[0]['above_knee_2_before'] = ""

    file.close()

    with open('LE-data.json', 'w') as file:
        json.dump(data, file)

    entry_weight.delete(0, END)
    entry_claw.delete(0, END)
    entry_ankle.delete(0, END)
    above_ankle_entry.delete(0, END)
    below_knee_entry.delete(0, END)
    knee_entry.delete(0, END)
    above_knee_1_entry.delete(0, END)
    above_knee_entry_2.delete(0, END)


def saveAfterData():

    global entry_weight_after, entry_claw_after, entry_ankle_after, above_ankle_entry_after, below_knee_entry_after, knee_after_entry, above_knee_1_entry_after, above_knee_entry_2_after, wraps_completed_entry
    
    entry_weight_after_data = entry_weight_after.get()
    entry_claw_after_data = entry_claw_after.get()
    entry_ankle_after_data = entry_ankle_after.get()
    above_ankle_entry_after_data = above_ankle_entry_after.get()
    below_knee_entry_after_data = below_knee_entry_after.get()
    knee_entry_after_data = knee_after_entry.get()
    above_knee_1_entry_after_data = above_knee_1_entry_after.get()
    above_knee_2_entry_after_data = above_knee_entry_2_after.get()
    wraps_completed_entry_data = wraps_completed_entry.get()
    
    with open('LE-data.json', 'r') as file:

        data = json.load(file)

        data[1]['weight_after'] = entry_weight_after_data
        data[1]['claw_after'] = entry_claw_after_data
        data[1]['ankle_after'] = entry_ankle_after_data
        data[1]['above_ankle_after'] = above_ankle_entry_after_data
        data[1]['below_knee_after'] = below_knee_entry_after_data
        data[1]['knee_after'] = knee_entry_after_data
        data[1]['above_knee_1_after'] = above_knee_1_entry_after_data
        data[1]['above_knee_2_after'] = above_knee_2_entry_after_data
        data[1]['wraps_completed_after'] = wraps_completed_entry_data

    file.close()
    
    with open('LE-data.json', 'w') as file:
        json.dump(data, file)

    file.close()

def loadAfterData():

    global entry_weight_after, entry_claw_after, entry_ankle_after, above_ankle_entry_after, below_knee_entry_after, knee_after_entry, above_knee_1_entry_after, above_knee_entry_2_after, wraps_completed_entry
    
    with open('LE-data.json', 'r') as file:
        data = json.load(file)

    file.close()

    entry_weight_after.insert(0,data[1]['weight_after'])
    entry_claw_after.insert(0, data[1]['claw_after'])
    entry_ankle_after.insert(0, data[1]['ankle_after'])
    above_ankle_entry_after.insert(0, data[1]['above_ankle_after'])
    below_knee_entry_after.insert(0, data[1]['below_knee_after'])
    knee_after_entry.insert(0, data[1]['knee_after'])
    above_knee_1_entry_after.insert(0, data[1]['above_knee_1_after'])
    above_knee_entry_2_after.insert(0, data[1]['above_knee_2_after'])
    wraps_completed_entry.insert(0, data[1]['wraps_completed_after'])

def clearEntryAfter():

    global entry_weight_after, entry_claw_after, entry_ankle_after, above_ankle_entry_after, below_knee_entry_after, knee_after_entry, above_knee_1_entry_after, above_knee_entry_2_after, wraps_completed_entry

    with open('LE-data.json', 'r') as file:
        data = json.load(file)
        data[1]['weight_after'] = ""
        data[1]['claw_after'] = ""
        data[1]['ankle_after'] = ""
        data[1]['above_ankle_after'] = ""
        data[1]['below_knee_after'] = ""
        data[1]['knee_after'] = ""
        data[1]['above_knee_1_after'] = ""
        data[1]['above_knee_2_after'] = ""

    file.close()

    with open('LE-data.json', 'w') as file:
        json.dump(data, file)

    entry_weight_after.delete(0, END)
    entry_claw_after.delete(0, END)
    entry_ankle_after.delete(0, END)
    above_ankle_entry_after.delete(0, END)
    below_knee_entry_after.delete(0, END)
    knee_after_entry.delete(0, END)
    above_knee_1_entry_after.delete(0, END)
    above_knee_entry_2_after.delete(0, END)
    wraps_completed_entry.delete(0,END)

def exportToCSV():

    #import current data
    with open('LE-data.json', 'r') as file:
        data = json.load(file)
    
    file.close()

    with open('LE-data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["Catergory","Before", "After"]

        writer.writerow(field)
        writer.writerow(["Weight Before", data[0]['weight_before'], data[1]['weight_after']])
        writer.writerow(["(1) Claw", data[0]['claw_before'], data[1]['claw_after']])
        writer.writerow(["(2) Ankle", data[0]['ankle_before'], data[1]['ankle_after']])
        writer.writerow(["(3) Above Ankle", data[0]['above_ankle_before'], data[1]['above_ankle_after']])
        writer.writerow(["(4) Below the knee", data[0]['below_knee_before'], data[1]['below_knee_after']])
        writer.writerow(["(5) Knee", data[0]['knee_before'], data[1]['knee_after']])
        writer.writerow(["(6) Above knee", data[0]['above_knee_1_before'], data[1]['above_knee_1_after']])
        writer.writerow(["(7) Above knee 2", data[0]['above_knee_2_before'], data[1]['above_knee_2_after']])
        writer.writerow(["Wraps completed", data[0]['wraps_completed_before'], data[1]['wraps_completed_after']])

    file.close()
    print(".csv created successfully")

    subprocess.Popen(["open", "LE-data.csv"])

#First frame

frame = Frame(root)
frame.pack()

labelframe = LabelFrame(frame, text="Before")
labelframe.grid(row=0, column=0)

weight_before = Label(labelframe, font=('Helvetica', 14), text="Weight Before")
weight_before.grid(column=0, row=0, sticky="w")

entry_weight = Entry(labelframe, width=13)
entry_weight.grid(column=1, row=0, sticky="w", padx=(0,20))

claw_before = Label(labelframe, font=('Helvetica', 14), text="(1) Claw(อุ้งเท้า)")
claw_before.grid(column=0, row=1, sticky="w")

entry_claw = Entry(labelframe,  width=13)
entry_claw.grid(column=1, row=1, sticky="w")

ankle_before= Label(labelframe, font=('Helvetica', 14), text="(2) Ankle(ตาตุ่ม)")
ankle_before.grid(column=0, row=2, sticky="w")

entry_ankle = Entry(labelframe,  width=13)
entry_ankle.grid(column=1, row=2, sticky="w")

above_ankle_before = Label(labelframe, font=('Helvetica', 14), text="(3) Above Ankle(เหนือตาตุ่ม)")
above_ankle_before.grid(column=0, row=3, sticky="w")

above_ankle_entry = Entry(labelframe,  width=13)
above_ankle_entry.grid(column=1, row=3, sticky="w")

below_knee_before = Label(labelframe, font=('Helvetica', 14), text="(4) Below the knee(ใต้เข่า)")
below_knee_before.grid(column=0, row=4, sticky="w")

below_knee_entry= Entry(labelframe,  width=13)
below_knee_entry.grid(column=1, row=4, sticky="w")

knee_before = Label(labelframe, font=('Helvetica', 14), text="(5) Knee(เข่า)")
knee_before.grid(column=0, row=5, sticky="w")

knee_entry = Entry(labelframe,  width=13)
knee_entry.grid(column=1, row=5, sticky="w")

above_knee_1_before = Label(labelframe, font=('Helvetica', 14), text="(6) Above knee(เหนือเข่า)")
above_knee_1_before.grid(column=0, row=6, sticky="w")

above_knee_1_entry = Entry(labelframe,  width=13)
above_knee_1_entry.grid(column=1, row=6, sticky="w")

above_knee_2_before = Label(labelframe, font=('Helvetica', 14), text="(7) Above knee 2(เหนือเข่า)")
above_knee_2_before.grid(column=0, row=7, sticky="w")

above_knee_entry_2 = Entry(labelframe,  width=13)
above_knee_entry_2.grid(column=1, row=7, sticky="w")

button_save = Button(labelframe, text="Save", command=saveBeforeData)
button_save.grid(column=0, row=8, sticky="w",pady=(0,10))

button_save2 = Button(labelframe, text="Clear Entries", command=clearEntry)
button_save2.grid(column=1, row=8, sticky="w",pady=(0,10))

#Second frame

frame2 = Frame(root)
frame2.pack()

labelframe2 = LabelFrame(frame2, text="After")
labelframe2.grid(row=0, column=0)

weight_after = Label(labelframe2, font=('Helvetica', 14), text="Weight After")
weight_after.grid(column=0, row=0, sticky="w")

entry_weight_after = Entry(labelframe2, width=13)
entry_weight_after.grid(column=1, row=0, sticky="w", padx=(0,20))

claw_after = Label(labelframe2, font=('Helvetica', 14), text="(1) Claw(อุ้งเท้า)")
claw_after.grid(column=0, row=1, sticky="w")

entry_claw_after = Entry(labelframe2,  width=13)
entry_claw_after.grid(column=1, row=1, sticky="w")

ankle_after= Label(labelframe2, font=('Helvetica', 14), text="(2) Ankle(ตาตุ่ม)")
ankle_after.grid(column=0, row=2, sticky="w")

entry_ankle_after = Entry(labelframe2,  width=13)
entry_ankle_after.grid(column=1, row=2, sticky="w")

above_ankle_after = Label(labelframe2, font=('Helvetica', 14), text="(3) Above Ankle(เหนือตาตุ่ม)")
above_ankle_after.grid(column=0, row=3, sticky="w")

above_ankle_entry_after = Entry(labelframe2,  width=13)
above_ankle_entry_after.grid(column=1, row=3, sticky="w")

below_knee_after = Label(labelframe2, font=('Helvetica', 14), text="(4) Below the knee(ใต้เข่า)")
below_knee_after.grid(column=0, row=4, sticky="w")

below_knee_entry_after= Entry(labelframe2,  width=13)
below_knee_entry_after.grid(column=1, row=4, sticky="w")

knee_after = Label(labelframe2, font=('Helvetica', 14), text="(5) Knee(เข่า)")
knee_after.grid(column=0, row=5, sticky="w")

knee_after_entry = Entry(labelframe2,  width=13)
knee_after_entry.grid(column=1, row=5, sticky="w")

above_knee_1_after = Label(labelframe2, font=('Helvetica', 14), text="(6) Above knee(เหนือเข่า)")
above_knee_1_after.grid(column=0, row=6, sticky="w")

above_knee_1_entry_after = Entry(labelframe2,  width=13)
above_knee_1_entry_after.grid(column=1, row=6, sticky="w")

above_knee_2_after = Label(labelframe2, font=('Helvetica', 14), text="(7) Above knee 2(เหนือเข่า)")
above_knee_2_after.grid(column=0, row=7, sticky="w")

above_knee_entry_2_after = Entry(labelframe2,  width=13)
above_knee_entry_2_after.grid(column=1, row=7, sticky="w")

wraps_completed = Label(labelframe2, font=('Helvetica', 14), text="Wraps Completed")
wraps_completed.grid(column=0, row=8, sticky="w")

wraps_completed_entry = Entry(labelframe2,  width=13)
wraps_completed_entry.grid(column=1, row=8, sticky="w")

button_save_after = Button(labelframe2, text="Save", command=saveAfterData)
button_save_after.grid(column=0, row=9, sticky="w",pady=(0,10))

button_save2_after = Button(labelframe2, text="Clear Entries", command=clearEntryAfter)
button_save2_after.grid(column=1, row=9, sticky="w",pady=(0,10))

button_export = Button(root, text="Export to CSV", command=exportToCSV)
button_export.pack()

loadData()
loadAfterData()

root.mainloop()