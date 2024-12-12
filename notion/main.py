from functions import Notion

KEY_ACESS = "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"
DB_ID = "159ebe4500388076adbdcdf8d5465e28"

# Initialize Notion instance
notion = Notion(KEY_ACESS)

# Get data
# notion.get_data(DB_ID, 100)

# Add data
# title = "Test Title"
# description = "Test Description"
# published_date = datetime.now().astimezone(timezone.utc).isoformat()
# data = {
#     "URL": {"title": [{"text": {"content": description}}]},
#     "Title": {"rich_text": [{"text": {"content": title}}]},
#     "Published": {"date": {"start": published_date, "end": None}}
# }
# notion.add_data(DB_ID, data)

# Update data
# page_id = '159ebe45-0038-814a-bf06-cc06a632b194'
# update_data = {"Title": {"rich_text": [{"text": {"content": "Update title"}}]}}
# notion.update_data(page_id, update_data)

# Delete data
# page_id = '159ebe45-0038-814a-bf06-cc06a632b194'
# notion.delete_data(page_id)

# Add data in a note
# data = [{"object": "block","type": "heading_2","heading_2": {"rich_text": [{"type": "text","text": {"content": "Types of kale",},}]},}]
# notion.note_add_data('159ebe45003880bfb4e8f16b15dbec1e', data)

# Read a note
# page_id = "159ebe45003880bfb4e8f16b15dbec1e"
# print(notion.read_note(page_id))

# Delete a block in a note
# page_id = "159ebe45-0038-802b-b04a-d2af38c27b72"
# print(notion.delete_note_child(page_id))

# Delete a note
page_id = "159ebe45003880bfb4e8f16b15dbec1e"
print(notion.delete_note(page_id))