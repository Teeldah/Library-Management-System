import uuid

items = []

def AddItem():
	title = input("Enter a title for the item: ")
	category = input("What category does the item belongs to **e.g Book, Article, Research paper:  ")
	catalogue_id = input("Enter the catalogue id for this item: ")
	shelf_no = input("Enter the number for this Item: ")
	arrival_date = input("Enter date of arrival in this format **YYYY-MM-DD** :  ")
	issued = False
	issue_to = ""
	issue_date = ""
	return_date = ""
	
	if len(items) != 0:
		for item in items:
			if item["catalogue_id"] == catalogue_id:
				print(f"Item with {catalogue_id} and {item['title']} exists already")
	else:
		id = uuid.uuid4()
		item_dict = {
			"item_id": id,
			"title":title,
			"category":category,
			"catalogue_id":catalogue_id,
			"shelf_number": shelf_no,
			"Date of Arrival": arrival_date,
			"Issued":issued,
			"Issue_date":issue_date,
			"Return_date":return_date,
			"Issued_to": issue_to
			}
		items.append(item_dict)
		print(f"Item with {item_dict['title']} and  {item_dict['catalogue_id']} has been saved Successfully")

def UpdateItem(catalogue_id, fields):
	if len(items) != 0:
		for item in items:
			if item["catalogue_id"] == catalogue_id:

				for field in fields:
					if str(field).lower() == "title":
						new_title = input("Enter a title for the item: ")
						item["title"] = new_title
					if str(field).lower() == "category":
						new_category = input("What category does the item belongs to **e.g Book, Article, Research paper:  ")
						item["category"] = new_category
					if str(field).lower() == "shelf_number":
						new_shelf_no = input("Enter the number for this Item: ")
						item["shelf_number"] = new_shelf_no
					if str(field).lower() == "arrival_date":
						new_arrival_date =  input("Enter date of arrival in this format **YYYY-MM-DD** :  ")
						item["Date of Arrival"] = new_arrival_date
				print(f"Item with catalogue_id {item['catalogue_id']} has been update successfully")
			else:
				print(f"Item with {catalogue_id} does not exist")
				break
	else:
		print("Database is empty, Add items to be able to update it")



def ItemDelete(catalogue_id):
	if len(items) != 0:
		for item in items:
			if item["catalogue_id"] == catalogue_id:
				items.remove(item)
				print(f"Item with {catalogue_id} has been deleted successfully")
			else: 
				print(f"Item with {catalogue_id} does not exist")
				break
	else:
		print("Database is Empty")



def ItemFetch(catalogue_id):
	if len(items) != 0:
		for item in items:
			if item["catalogue_id"] == catalogue_id:
				for key, value in item.items():
					print(f"{key} = {value}")
			else:
				print(f"Item with {catalogue_id} does not exist")
				break
	else:
		print("Database is Empty")

def ItemFetchAll():
	if len(items) != 0:
		for item in items:
			for key, value in item.items():
				print(f"{key} = {value}")
			print("\n\n")
			

def IssueItem(catalogue_id=None, title=None):
	if len(items) != 0:
		for item in items:
			if item["catalogue_id"] == catalogue_id:
				item["Issue_date"] = input("Enter date of Item issue in this format **YYYY-MM-DD** :  ")
				item["Return_date"] = input("Enter Date to Return Item in this format **YYYY-MM-DD** :  ")
				item["Issued"] = True
				item["Issued_to"] = input("Enter name of Patron or Reader: ")

			else:
				print(f"Item with {catalogue_id} does not exist")
				break

def GetIssuedItems():
	issued_items = []
	if len(items) == 0:
		for item in items:
			if item["Issued"] == True:
				issued_items.append(item)
		for i in issued_items:
			for key, value in item.items():
					print(f"{key} = {value}")
			print("\n\n")
	else:
		print("Database is Empty")



print("""                              WELCOME TO MATILDA'S LIBRARY MANAGEMENT SYSTEM(LMS): 
      
      """)
name = input("Enter your full-name for our records: ")


while True:
	print("""                
				WHAT WOULD YOU LIKE TO DO:
		
		
		1. Add an item to the system? use code #additem
		2. Update an already existing Item? use code #updateitem
		3. Fetch an Item from the Database or Archive? use code #fetchitem
        4. Fetch all Items from the Database or Archive? use code #fetchallitems
		4. Delete item from the Archives? use code #deleteitem
		5. Issue an item to a Patron? use code #issueitem
		6. fetch all issued items? use code #fetchall_issueditems
		7. Logout of the LMS System? #logout

											""")

	code = input(f"Welcome {name}, what would you like to do  ## check the options above and their various codes without the hash sign and input it here## :  ")
	if str(code).lower() == "additem":
		AddItem()
	elif str(code).lower() == "updateitem":
		fields = []
		catalogue_id = input("Enter Item catalogue_id to be updated: ")
		print("Enter fields to Edit from the options Below:")
		print("""THIS ARE THE FIELDS THAT CAN BE EDITED:
				1. Title
				2. Category
				3. Shelf_Number:
				4. Arrival_date
				""")
		for i in range(9):
			field = input("Enter field name or 'end' to end it: ")
			if field.lower() == "end":
				break
			else:
				fields.append(field)

		UpdateItem(catalogue_id, fields)
	elif str(code).lower() == "fetchitem":
		catalogue_id = input("Enter Item catalogue_id: ")
		ItemFetch(catalogue_id)
	elif str(code).lower() == "fetchallitems":
		ItemFetchAll()
		catalogue_id = input("Enter Item catalogue_id: ")
	elif str(code).lower() == "deleteitem":
		catalogue_id = input("Enter Item catalogue_id: ")
		ItemDelete(catalogue_id)
	elif str(code).lower() == "issueitem":
		catalogue_id = input("Enter Item catalogue_id to be updated: ")
		IssueItem(catalogue_id)
	elif str(code).lower() == "fetchall_issueditems":
		GetIssuedItems()
	elif str(code).lower() == "logout":
		break
	else:
		print("#############You Entered a wrong option#############33")
		
print("Logout of LMS is successful.....####")
	