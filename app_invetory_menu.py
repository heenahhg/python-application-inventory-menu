# ==========================================
# Project: Application Inventory Management System
# Developer: Hina Gohil
# Version: 1.0
# ==========================================

import re
import json

applications =  [
    {
        "Name" : "Google Chrome",
        "Vendor" : "Google",
        "Version" : "138",
        "Architecture" : "64-bit"
    },
     {
            "Name" : "Chrome Remote Control",
            "Vendor" : "Google",
            "Version" : "1.0.0",
            "Architecture" : "64-bit"
        },
    {
        "Name": "Microsoft Edge",
        "Vendor": "Microsoft",
        "Version": "138",
        "Architecture": "64-bit"
    },
    {
        "Name": "VLC",
        "Vendor": "VideoLAN",
        "Version": "4.0",
        "Architecture": "64-bit"
    }
]

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
    
    
applications = load_inventory(applications)

## Creating a menu
def menu():
    print("=" * 30)
    print("Application Inventory Management")
    print("=" * 30)
    print("1. Display Inventory")
    print("2. Search Application")
    print("3. Add Application")
    print("4. Delete Application")
    print("5. Update Application")
    print("6. Sort Applications")
    print("7. Search by Vendor")
    print("8. Search by Architecture")
    print("9. Exit")

def get_menu_choice():
     while True:
          choice = input("Enter your choice:").strip()

          if choice.isdigit():
               return choice

          print("Invalid Input. Please enter a number.")

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
        display_application(app)
      #  print(f"Name            : {app['Name']}")
      #  print(f"Vendor          : {app['Vendor']}")
      #  print(f"Version         : {app['Version']}")
      #  print(f"Architecture    : {app['Architecture']}")

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
         
## Adding the application
#new_application = {
#    "Name": "Adobe Reader",
#    "Vendor": "Adobe",
#    "Version": "25.001",
#    "Architecture": "64-bit"
#}
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

def add_application(apps, new_app):
    print("\nAdding the new application...")
    apps.append(new_app)
    print(f"\nApplication added successfully.")
    save_inventory(apps)


def delete_application(apps, app_name):
    app = select_application(apps, app_name)

    if app is None:
        return
    apps.remove(app)
    print(f"{app['Name']} deleted successfully.")
    save_inventory(apps)

def validate_version(version):
    return bool(re.fullmatch(r"\d+(\.\d+)*", version))

def update_app (apps, app_name):
    
    app = select_application(apps, app_name)

    if app is None:
        return
    print("1. Version")
    print("2. Vendor")
    print("3. Architecture")
    choice = input("Enter your choice: ")
    print(f"You selected: {choice}")

    if choice == "1":
            new_version = input("Enter New Version:").strip()
            if not validate_version(new_version):
                    print("Invalid version format.")
                    return
            app["Version"] = new_version
            print(f"{app['Name']} updated successfully.")
            save_inventory(apps)
    elif choice == "2":
            new_vendor = input("Enter New Vendor:").strip()
            if new_vendor == "":
                print("Application vendor cannot be empty.")
                return
            app["Vendor"] = new_vendor
            print(f"{app['Name']} updated successfully.")
            save_inventory(apps)
    elif choice == "3":
            new_arc = input("Enter New Architecture:").strip()
            if new_arc == "":
                 print("Application architecture cannot be empty.")
                 return
            app["Architecture"] = new_arc
            print(f"{app['Name']} updated successfully.")
            save_inventory(apps)
    else:
            print("Invalid Choice.")
            return

def sort_applications(apps):

    sorted_apps = sorted(apps, key=lambda app: app["Name"].lower())

    print("\n*****Applications Sorted by Name*****")

    for number, app in enumerate(sorted_apps, start=1):
        print(f"\nApplication {number}")
        display_application(app)

while True:

    menu()

    choice = get_menu_choice()
    print(f"You selected: {choice}")
    
    if choice == "1":
        #print(type(choice))
        display_inventory(applications)
        
    elif choice ==  "2":
        app_name = input("Enter application name to search:").strip()
        if app_name == "":
            print("Application name cannot be empty.")
            continue
        #print(f"{app_name}")
        search_application(applications, app_name)
    elif choice == "3":
        name = input("Enter application name:").strip()
        if name == "":
            print("Application name cannot be empty.")
            continue
        if application_exists(applications, name):
            print("Application already exists.")
            continue
        vendor = input("Enter vendor       :").strip()
        if vendor == "":
            print("Application vendor cannot be empty.")
            continue
        version = input("Enter version     :").strip()
        if not validate_version(version): 
            print("Invalid version format.")
            continue
        architecture = input("Enter architecture   :").strip()
        if architecture == "":
            print("Architecture cannot be empty.")
            continue

        new_app = {
            "Name" : name, 
            "Vendor" : vendor, 
            "Version" : version,
            "Architecture" : architecture
        }
        #print(f"{new_app}")
        add_application(applications, new_app)

    elif choice == "4" :
        del_app = input("Enter application name to delete:").strip()
        delete_application(applications, del_app)
    elif choice == "5" :
            app_name = input("Enter application name to update:").strip()
            if app_name == "":
                print("Application name cannot be empty.")
                continue
            update_app(applications, app_name)
    elif choice == "6":
        sort_applications(applications)
    elif choice ==  "7":
            vendor_name = input("Enter vendor name to search:").strip()
            if vendor_name == "":
                print("Vendor name cannot be empty.")
                continue
            search_by_vendor(applications, vendor_name)
    elif choice ==  "8":
                architecture = input("Enter architecture to search:").strip()
                if architecture == "":
                    print("Architecture cannot be empty.")
                    continue
                search_by_arch(applications, architecture)

    elif choice == "9":
        print("Exiting...")
        break
    else:
        print("Invalid Choice.")
    

