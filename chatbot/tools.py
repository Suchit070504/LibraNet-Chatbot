from langchain.tools import tool
from library.manager import LibraryManager
from library.sample_data import load_sample_data
import json

manager = load_sample_data(LibraryManager())

# Helper to parse JSON input for multi-parameter tools
def parse_json_input(input_str):
    try:
        return json.loads(input_str)
    except Exception as e:
        return {}

@tool
def register_user(args: str):
    """Register a new library user. args is a JSON string with user_id, name, email."""
    params = parse_json_input(args)
    user_id = params.get("user_id")
    name = params.get("name")
    email = params.get("email")
    if None in [user_id, name, email]:
        return "Missing parameters for register_user"
    return manager.register_user(user_id, name, email)

@tool
def borrow_item(args: str):
    """Borrow an item for given days. args is JSON string with user_id, item_id, duration_days (optional)."""
    params = parse_json_input(args)
    user_id = params.get("user_id")
    item_id = params.get("item_id")
    duration_days = params.get("duration_days", 10)
    if None in [user_id, item_id]:
        return "Missing parameters for borrow_item"
    return manager.borrow_item(user_id, item_id, duration_days)

@tool
def return_item(args: str):
    """Return an item and calculate fines. args is JSON string with item_id."""
    params = parse_json_input(args)
    item_id = params.get("item_id")
    if item_id is None:
        return "Missing item_id for return_item"
    return manager.return_item(item_id)

@tool
def generate_reports(args: str = None):
    """Generate reports of library usage. No input expected."""
    return manager.generate_reports()

@tool
def list_items(args: str = None):
    """List all library items with availability. No input expected."""
    return "\n".join(manager.list_items())
