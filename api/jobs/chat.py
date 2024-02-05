from database.messages import ChatRepo, MessageRepo
from models.chat import Message
from exceptions import QuantGenieException

chat_repo = ChatRepo()
message_repo = MessageRepo()

def add_to_chat(user_id:str, chat_id:str, message:Message, chat_history:str):
    if chat_id:
        chat = chat_repo.update_history_time(chat_id, chat_history)
        if (chat.get('user_id') != user_id):
            raise QuantGenieException('This is not your chat')
        message = message_repo.add_message(chat_id, message)
    else:
        title = 'New Chat II'
        chat = chat_repo.new_chat({ 'user_id': user_id, 'title': title })
        message = message_repo.add_message(chat.get('_id'), message)
    chat_id = chat_id if chat_id else chat.get('_id')
    chat_repo.update_history_time(chat_id, chat_history)
    return {'status': 'Completed'}



