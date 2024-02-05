from database.messages import ChatRepo, MessageRepo
from models.chat import Message
from exceptions import QuantGenieException

chat_repo = ChatRepo()
message_repo = MessageRepo()

def add_to_chat(user_id:str, chat_id:str, message:Message, chat_history:str):
    message = message_repo.add_message(chat_id, message)
    chat_repo.update_history_time(chat_id, history=chat_history)
    return {'status': 'Completed'}



