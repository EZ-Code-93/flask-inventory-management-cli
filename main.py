import argparse
import admin

    
def main():
    parser = argparse.ArgumentParser(description="Inventory Admin CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    
    subparsers.add_parser("list", help="Get all inventory items")

    
    get_parser = subparsers.add_parser("get", help="Get a single item by ID")
    get_parser.add_argument("id", type=int, help="Item ID")

   
    add_parser = subparsers.add_parser("add", help="Add a new item")
    add_parser.add_argument("name", type=str, help="Item name")
    add_parser.add_argument("quantity", type=int, help="Item quantity")

    
    update_parser = subparsers.add_parser("update", help="Update an existing item")
    update_parser.add_argument("id", type=int, help="Item ID")
    update_parser.add_argument("--name", type=str, help="New item name")
    update_parser.add_argument("--quantity", type=int, help="New item quantity")

    
    delete_parser = subparsers.add_parser("delete", help="Delete an item by ID")
    delete_parser.add_argument("id", type=int, help="Item ID")

    args = parser.parse_args()

    
    if args.command == "list":
        admin.get_all()
    elif args.command == "get":
        admin.get_one(args.id)
    elif args.command == "add":
        admin.create_item(args.name, args.quantity)
    elif args.command == "update":
        admin.update_item(args.id, args.name, args.quantity)
    elif args.command == "delete":
        admin.delete_item(args.id)




if __name__ == "__main__":
    main()