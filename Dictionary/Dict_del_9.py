# The del keyword removes the item with the specified key name:
Telcom = {
    "airtel":"SunInfotec",
    "vodacom":"Talanx",
    "mtn":"Alcatel-Lucent",
    "net1":"Nokia Siemens Networks",
    "Hauwei": "Ericsson"
}
print("Existing list: \n", Telcom)

# Remove 'net1' from dictionary
del Telcom["net1"]
print("New items after delete: \n", Telcom)

# deleted item from the dictionary cannot be accessed again. If you try to access it,  
# Python will raise a KeyError exception:
del Telcom
print("Trying to access deleted dictionary: \n", Telcom) #this will raise an error  because Telcom is no longer defined.
