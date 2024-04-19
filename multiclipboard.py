import sys, json, clipboard
'''
NOTES
clipboard.copy("ls") // This command will pase pase a the value in the parenthses to the clipboard
data = clipboars.paste() // This will paste whatever is stored on the clipboard to the terminal when run
print(sys.argv[2:]) #this argv will give all the cmd line arguments passed alongside the python file
'''

SAVED_DATA = "clipboard.json"


def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f) #this dumps the "data" to the file, "f"

def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}
    

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save':
        key = input("enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("data saved")
    elif command == 'load':
        key = input("enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard")
        else:
            print("key does not exist")
    elif command == 'list':
        print(data)
    else:
        print('Unknown command: enter a valid command (save, list, load)')

else:
    print("please pass exactly one command")
