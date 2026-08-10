# ==========================================
# Project: Application Inventory Management System
# Developer: Hina Gohil
# Version: 1.0
# ==========================================
applications =  [
    {
        "Name" : "Google Chrome",
        "Vendor" : "Google",
        "Version" : "138",
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
    print("5. Exit")

## Display the application list
def display_inventory(apps):
    print("\n*****Application Inventory*******")

    for number, app in enumerate(apps, start=1):
        print(f"\nApplication {number}")
        print(f"Name            : {app['Name']}")
        print(f"Vendor          : {app['Vendor']}")
        print(f"Version         : {app['Version']}")
        print(f"Architecture    : {app['Architecture']}")

##searching for the application

def search_application(apps, app_name):
    print("\nSearching for the application...........")
    for app in apps:
        if app["Name"] == app_name:
            print("\nApplication Found.")
            print(f"Name            : {app['Name']}")
            print(f"Vendor          : {app['Vendor']}")
            print(f"Version         : {app['Version']}")
            print(f"Architecture    : {app['Architecture']}")
            return

    print(f"\n{app_name} was not found.")

## Adding the application
#new_application = {
#    "Name": "Adobe Reader",
#    "Vendor": "Adobe",
#    "Version": "25.001",
#    "Architecture": "64-bit"
#}


def add_application(apps, new_app):
    print("\nAdding the new application...")
    for app in apps:
        if app["Name"] == new_app["Name"]:
            print("\nApplication already exists.")
            return

    apps.append(new_app)
    print(f"\nApplication added successfully.")

def delete_application(apps, app_name):
    print("\nSearching for the application...")
    for app in apps:
        if app["Name"] == app_name:
            apps.remove(app)
            print(f"{app_name} deleted successfully.")
            return
    print("Application not found.")

def update_app (apps, app_name):
    print("\nSearching for the application...")
    for app in apps:
        if app["Name"] == app_name:
            new_version = input("Enter New Version:")
            app["Version"] = new_version
            
            print(f"{app_name} updated successfully.")
            return
    print("Application not found.")

while True:

    menu()

    choice = input("Enter your choice: ")
    print(f"You selected: {choice}")

    if choice == "1":
        #print(type(choice))
        display_inventory(applications)
    elif choice ==  "2":
        app_name = input("Enter application name to search:")
        #print(f"{app_name}")
        search_application(applications, app_name)
    elif choice == "3":
        name = input("Enter application name:")
        vendor = input("Enter vendor       :")
        version = input("Enter version     :")
        architecture = input("Enter architecture   :")

        new_app = {
            "Name" : name, 
            "Vendor" : vendor, 
            "Version" : version,
            "Architecture" : architecture
        }
        #print(f"{new_app}")
        add_application(applications, new_app)

    elif choice == "4" :
        del_app = input("Enter application name to delete:")
        delete_application(applications, del_app)
    elif choice == "5" :
            upd_app = input("Enter application name to update:")
            update_app(applications, upd_app)

    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid Choice.")
    

