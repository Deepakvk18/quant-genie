"use client"

import React, { useEffect, useState } from 'react';
import { ArrowUp } from 'lucide-react';
import Message from './Message';
import { ChevronLeft, Menu } from 'lucide-react';
import { io } from 'socket.io-client';
import Intro from './Intro';
import { useRecoilValue } from 'recoil';
import { accessAtom, userAtom } from '@/store';
import { IMessage } from '@/lib/types';
import { useQuery } from '@tanstack/react-query';
import ChatSkeleton from './ChatSkeleton';
import useAxios from '@/lib/axios';

const ChatSection = ({ history, 
                      setHistory, 
                      setAccount, 
                      chatHistory,
                      setChatHistory,
                      chatId,
                      setChatId }) => {

  const [socket, setSocket] = useState<any>(null) 
  const access = useRecoilValue(accessAtom)
  const user = useRecoilValue(userAtom)

  const [messages, setMessages] = useState<IMessage[]>([])
  const axios = useAxios()
  const { data: msgs, isLoading, isError, refetch } = useQuery({
    queryKey: [`get-msgs-${chatId}`],
    queryFn: async ()=>{
      const res = await axios.get(`/messages/${chatId}`)
      return res?.data
    },
    enabled: !!chatId
  })

  useEffect(()=>{
    if (!messages) setMessages([])
  }, [messages])

  const scrollToBottom = ()=>{
    const chatArea = document.getElementById('dummy-div')
    chatArea?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(()=>{
 
    const socket = io('ws://localhost:8000', {
      path: '/ws/socket.io',
      autoConnect: false,
      transports: ['websocket'],
      upgrade: false,
      auth: {
        headers: access
      }
    })

    socket?.on("connect", ()=>{
      console.log("Connected!!", socket.id);
    })
  
    socket?.on("message", (data)=>{
      const jsonData = JSON.parse(data)
      console.log(jsonData);
      
      setMessages((prevMessages)=>{
        return [ ...prevMessages, { output: jsonData?.output }]
      })
      
      setChatId(jsonData?.chatId)
      scrollToBottom()
      setChatHistory(jsonData?.chat_history)
      setLoading(false)
    })
  
    socket?.on("connect_error", (err: any)=>{
      console.error(`Error due to ${err?.message}`);
    })
  
    socket?.on("disconnect", ()=>{
      console.log("Disconnect");
      socket.removeAllListeners();  
    })
    setSocket(socket)    
    scrollToBottom()
    socket.connect()

    return ()=>{
      socket.off('message')
      socket.off('connect')
      socket.off('disconnect')
      socket.off('response')
      socket.disconnect()
      socket.removeAllListeners()
    }
  }, [access])

  const [loading, setLoading] = useState(false)

  useEffect(() => {
    const textarea = document.getElementById('autoresize');
    

    function autoResize() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';    
        this.style.maxHeight = 300 + 'px'
        this.style.minHeight = 50 + 'px'
      }
    textarea?.addEventListener('input', autoResize, false);
    
  }, [])


  const [message, setMessage] = useState('')

  const handleSendMessage = async (text: string) => {
    setLoading(true)
    const newMessage = { input: text.trim() };
    await socket.emit('message', { llmInput: { input: text, chat_history: chatHistory }, chatId, userId: user?._id})
    setMessages(prevMessages=>[ ...prevMessages, newMessage ])
    scrollToBottom()
  };

  useEffect(()=>{
    if (!isError && !isLoading)
      setMessages(msgs?.messages)
    else setMessages([])
  }, [msgs, isLoading, isError])

  return (
    <div id='chat-area' className={`relative h-[85%] w-full m-auto pb-28 pt-14 overflow-y-auto flex flex-col items-center chat-scrollbar ${history && 'invisible sm:visible'}`}>
        
        <Menu 
          onClick={()=>setHistory(true)}
          className={`cursor-pointer fixed inset-0 mt-4 ml-4 items-start gap-10 hover:opacity-40 ${history && 'invisible'}`}
          size='20'
        />
          { isLoading ? 
              <div className='flex h-full w-full justify-center items-center'>
                <ChatSkeleton />
              </div> :
              messages?.length === 0 || !messages ?
                <Intro 
                  setAccount={setAccount}
                />
              : messages?.map((message: IMessage, index: number) => (
                <Message key={index} {...message} />
              )) }
          

        <div id='dummy-div' />
        <div className="fixed bottom-4 flex flex-col h-[15%] justify-center items-center bg-gray-700 px-4 md:px-0 md:w-[60%] w-full">
          
            <div
              id='input-div'
              className='relative w-full'>
              <textarea
                id="autoresize"
                name='query-input'
                className={`group rounded-xl px-4 resize-none bg-gray-700 py-[10px] ring-[0.5px] ring-slate-400 chat-input h-auto w-full disabled:ring-0`}
                value={message}
                disabled={loading}
                onChange={(e)=>setMessage(e.target.value)}
                onKeyUp={(e) => {
                  if (e.key === 'Enter') {
                    handleSendMessage(e.target.value);
                    setMessage('')
                  }
                  
                }}
              />
              <label 
                className={`absolute flex inset-0 p-2 px-4 group-active:invisible ${loading && 'animate-pulse text-gray-800 items-center justify-center'}`}
                htmlFor="query-input"
              >
                <p onClick={async ()=>{
                  document.getElementById('autoresize')?.focus()
                  }} 
                  className={`text-gray-400 cursor-text w-full h-full ${loading && 'text-center items-center'}`}>{`${loading ?  "Loading..." : (!message ? "Type your query...": '')}`}</p>
              </label>
              <div>
                <button 
                  disabled={message === ""}
                   className={`absolute right-5 top-5 rounded-md cursor-pointer hover:opacity-80 bg-white disabled:opacity-30 ${loading && 'invisible'}`} 
                   type='submit' 
                   onClick={()=>handleSendMessage(message)}
                >
                  <ArrowUp 
                    color='black'
                  />
                </button>
              </div>
            </div>
          
          <p className='text-xs text-gray-400 mt-2'>
            QuantGenie can make mistakes. Consider checking important information.
          </p>
      </div>
      <ChevronLeft 
        className={`absolute left-0 inset-0 block my-auto hover:opacity-50 top-4 cursor-pointer ${history ? 'visible': 'invisible'}`}
        onClick={()=>setHistory(false)}
        size='20'
        color='gray'
      />      
    </div>
  );
};

export default ChatSection;
