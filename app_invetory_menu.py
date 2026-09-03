# ==========================================
# Project: Application Inventory Management System
# Developer: Hina Gohil
# Version: 1.0
# ==========================================

import re

from inventory_functions import display_application, display_inventory, search_application, search_by_vendor, normalize_architecture, search_by_arch, select_application, application_exists, sort_applications, load_inventory, save_inventory

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
         
def add_application(apps, new_app):
    print("\nAdding the new application...")
    apps.append(new_app)
    print("\nApplication added successfully.")
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
            architecture = input("Enter New Architecture:").strip()
            if architecture == "":
                 print("Application architecture cannot be empty.")
                 return
            architecture = normalize_architecture(architecture)
            app["Architecture"] = architecture
            print(f"{app['Name']} updated successfully.")
            save_inventory(apps)
    else:
            print("Invalid Choice.")
            return

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

        architecture = normalize_architecture(architecture)

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
                architecture = normalize_architecture(architecture)

                search_by_arch(applications, architecture)

    elif choice == "9":
        print("Exiting...")
        break
    else:
        print("Invalid Choice.")
    

