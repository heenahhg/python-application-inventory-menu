import json
import re

def save_inventory(apps):
    with open("applications.json", "w") as file:
        json.dump(apps, file, indent=4)

def load_inventory(default_apps):
    try:
        with open("applications.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("applications.json not found. Using default inventory.")
        return default_apps

    except json.JSONDecodeError:
        print("Invalid JSON data. Using default inventory.")
        return default_apps
    
    
def display_application(app):
    print(f"Name            : {app['Name']}")
    print(f"Vendor          : {app['Vendor']}")
    print(f"Version         : {app['Version']}")
    print(f"Architecture    : {app['Architecture']}")


## Display the application list
def display_inventory(apps):
    print("\n*****Application Inventory*******")
    total = len(apps)
    print(f"Total Applications: {total}")
    
    for number, app in enumerate(apps, start=1):
        
        print(f"\nApplication {number}")
        #sort_applications(app)
        display_application(app)

##searching for the application
def search_application(apps, app_name):
    print("\nSearching for the application...........")
    matches = []

    for app in apps:
        if app_name.lower() in app["Name"].lower():
            matches.append(app)

    if len(matches) == 0:
        print("Application not found.")
        return

    print(f"\nApplications found: {len(matches)}")

    for number, app in enumerate(matches, start=1):
        print(f"\nApplication {number}")
        display_application(app)

def search_by_vendor(apps, vendor_name):
    print("\nSearching for application by vendor...........")
    matches = []

    for app in apps:
        if vendor_name.lower() in app["Vendor"].lower():
            matches.append(app)

    if len(matches) == 0:
        print("Application not found.")
        return

    print(f"\nApplications found: {len(matches)}")

    for number, app in enumerate(matches, start=1):
        print(f"\nApplication {number}")
        display_application(app)

def normalize_architecture(architecture):
     architecture = architecture.lower().strip()
     if architecture in ["64", "64-bit", "x64", "amd64"]:
        return "64-bit"

     if architecture in ["32", "32-bit", "x86"]:
        return "32-bit"

     return architecture

def search_by_arch(apps, architecture):
    print("\nSearching for application by architecture...........")
    matches = []

    for app in apps:
        if normalize_architecture(architecture) == normalize_architecture(app["Architecture"]):
            matches.append(app)

    if len(matches) == 0:
        print("Application not found.")
        return

    print(f"\nApplications found: {len(matches)}")

    for number, app in enumerate(matches, start=1):
        print(f"\nApplication {number}")
        display_application(app)

def validate_version(version):
    return bool(re.fullmatch(r"\d+(\.\d+)*", version))

def select_application(apps, app_name):
    matches = []

    for app in apps:
        if app_name.lower() in app["Name"].lower():
            matches.append(app)

    if len(matches) == 0:
        print("Application not found.")
        return None
    elif len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        print("\nMultiple applications found:", len(matches))
        
        for number, app in enumerate(matches, start=1):
                print(f"Application {number}: {app['Name']}")

        selected = input("Enter the number of the application:")
                
        try:
            selected = int(selected)
        except ValueError:
            print("Invalid application number.")
            return None
                   
        if selected < 1 or selected > len(matches):
            print("Invalid application number.")
            return None
                               
        app = matches[selected - 1]
                   
        print("Selected application:", app["Name"])
        return app    
       
def application_exists(apps, app_name):
    for app in apps:
        if app["Name"].lower() == app_name.lower():
            return True

    return False

def sort_applications(apps):

    sorted_apps = sorted(apps, key=lambda app: app["Name"].lower())

    print("\n*****Applications Sorted by Name*****")

    for number, app in enumerate(sorted_apps, start=1):
        print(f"\nApplication {number}")
        display_application(app)

