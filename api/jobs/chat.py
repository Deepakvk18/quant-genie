from database.messages import ChatRepo
import datetime

chat_repo = ChatRepo()

def add_to_chat(user_id, chat_id, message, chat_history):
    if chat_id:
        chat = chat_repo.get_chat(chat_id)
    else:
        chat = chat_repo.new_chat(user_id, {'user_id': user_id, 'title': 'New Chat', 'messages': []},)

    chat.get('messages').append(message)
    chat['last_accessed_date'] = datetime.datetime.now()
    chat['chat_history'] = chat_history
    print(chat)
    chat_repo.add_chat(chat)
    return {'status': 'Completed'}

# add_to_chat('65b34f54607a3ead8a0a0e54', '65b8e505082b1f6da7b4eedf', [{'input':
# "How do I say 'good morning' in Tamil?", 'output': {'text': "Vanakkam! That's how you greet someone in the morning in Tamil. Want to hear how to say 'good evening' too?", 'images': ['http://none.com/1.js']}}])



