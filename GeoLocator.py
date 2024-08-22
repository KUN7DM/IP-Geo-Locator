import tkinter as tk
import ttkbootstrap as ttk
import requests
import webbrowser

def locator():
    ipAddress = strIPData.get()
    jsonLink = f"https://ipinfo.io/{ipAddress}/json"
    data = requests.get(jsonLink)
    dataDict = data.json()
    
    ipVar.set(dataDict["ip"])
    cityVar.set(dataDict["city"])
    regionVar.set(dataDict["region"])
    countryVar.set(dataDict["country"])
    locVar.set(dataDict["loc"])
    postalVar.set(dataDict["postal"])
    return dataDict

def map_link():
    dataDict = locator()
    url = f"https://www.google.com/maps/@{dataDict["loc"]},660m"
    webbrowser.open_new_tab(url)
    #print(url)

root = ttk.Window(themename = "minty")
root.iconphoto(False, tk.PhotoImage(file='C:\\Users\\Sam\\OneDrive - DNS Accountants Ltd\\Code\\Projects\\PythonProjects\\GeoLoc\\internet (2).png'))
root.title("GeoLocator")
root.geometry("250x300")

# Top Side
top_frame = ttk.Frame(master=root)
top_frame.pack()
top_label = ttk.Label(master=top_frame, text="Enter IP ")
top_label.pack(side="left")

# Input Data
strIPData = tk.StringVar()
top_entry = ttk.Entry(master=top_frame, width=30, bootstyle="danger", textvariable=strIPData)
top_entry.pack(side="left")

# Separator
empty_frame = ttk.Frame(master=root)
empty_frame.pack(pady=10)

# IP
ipVar = tk.StringVar()
ip_frame = ttk.Frame(master=root)
ip_frame.pack(fill="x")
ip_label = ttk.Label(master=ip_frame, text="IP:")
ip_label.pack(side="left", fill="both", padx=30)
ip_data = ttk.Label(master=ip_frame, textvariable=ipVar)
ip_data.pack(side="left")

# City
cityVar = tk.StringVar()
city_frame = ttk.Frame(master = root)
city_frame.pack(fill="x")
city_label = ttk.Label(master=city_frame, text="CITY:")
city_label.pack(side="left", fill="both", padx=30)
city_data = ttk.Label(master=city_frame, textvariable=cityVar)
city_data.pack(side="left")

# Region
regionVar = tk.StringVar()
region_frame = ttk.Frame(master=root)
region_frame.pack(fill="x")
region_label = ttk.Label(master=region_frame, text="REGION:")
region_label.pack(side="left", fill="both", padx=30)
region_data = ttk.Label(master=region_frame, textvariable=regionVar)
region_data.pack(side="left")

# Country
countryVar = tk.StringVar()
country_frame = ttk.Frame(master=root)
country_frame.pack(fill="x")
country_label = ttk.Label(master=country_frame, text="COUNTRY:")
country_label.pack(side="left", fill="both", padx=30)
country_data = ttk.Label(master=country_frame, textvariable=countryVar)
country_data.pack(side="left")

# Location
locVar = tk.StringVar()
loc_frame = ttk.Frame(master=root)
loc_frame.pack(fill="x")
loc_label = ttk.Label(master=loc_frame, text="LOC:")
loc_label.pack(side="left", fill="both", padx=30)
loc_data = ttk.Label(master=loc_frame, textvariable=locVar)
loc_data.pack(side="left")

# Postal Code
postalVar = tk.StringVar()
postal_frame = ttk.Frame(master=root)
postal_frame.pack(fill="x")
postal_label = ttk.Label(master=postal_frame, text="POSTAL CODE:")
postal_label.pack(side="left", fill="both", padx=30)
postal_data = ttk.Label(master=postal_frame, textvariable=postalVar)
postal_data.pack(side="left")

# Find Button
action_button = ttk.Button(master=root, text="Find", bootstyle = "primary", command=locator)
action_button.pack(pady=20)

# Find On Map
link_button = ttk.Button(master = root, text="Find on Map", bootstyle = "secondary", command=map_link)
link_button.pack()

root.mainloop()