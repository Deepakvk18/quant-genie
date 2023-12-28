"use client"

import React, { useEffect, useState } from 'react';
import { ArrowUp } from 'lucide-react';
import Message from './Message';
import { ChevronLeft, Menu, Download, Share2 } from 'lucide-react';


const ChatSection = ({ history, setHistory }) => {
  const [messages, setMessages] = useState([
    { sender: 'user', text: 'Hello!' },
    { sender: 'Genie', text: 'Hi there!' },
    { sender: 'user', text: 'How are you?' },
    { sender: 'user', text: 'Hello!' },
    { sender: 'Genie', text: 'Hi there!' },
    { sender: 'user', text: 'How are you?' },
    { sender: 'user', text: 'Hello!' },
    { sender: 'Genie', text: 'Hi there!' },
    { sender: 'user', text: 'How are you?' },

    { sender: 'user', text: 'Hello!' },
    { sender: 'Genie', text: 'Hi there!' },
    { sender: 'user', text: 'How are you?' },

    // Add more messages as needed
  ]);

  const scrollToBottom = ()=>{
    const chatArea = document.getElementById('dummy-div')
    chatArea?.scrollIntoView({ behavior: 'smooth' })
  }
  
  useEffect(()=>{
    scrollToBottom()
  }, [])

  const [loading, setLoading] = useState(false)
  const [loadingText, setLoadingText] = useState('')
  const loadingTextArray = ['Thinking....', 'Getting Data...', 'Analyzing Data...', 'Getting Results...', 'Preparing Final Output...']

  useEffect(() => {
    const textarea = document.getElementById('autoresize');
    
    
    function autoResize() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';    
        this.style.maxHeight = 300 + 'px'
        this.style.minHeight = 100 + 'px'
      }
    textarea?.addEventListener('input', autoResize, false);
  }, [])
  


  const [message, setMessage] = useState('')

  const handleSendMessage = (text) => {
    setLoading(true)
    const newMessage = { sender: 'user', text };
    setMessages((prevMessages)=>[...prevMessages, newMessage]);
    scrollToBottom()
    // Simulate response after a delay (for demo purposes)
    // const intArray = 
    setTimeout(() => {
      const responseMessage = { sender: 'Genie', text: 'I am good, thank you!' };
      setMessages((prevMessages)=>[...prevMessages, responseMessage]);
      scrollToBottom()
      setLoading(false)  
    }, 3000);
    
  };

  return (
    <div id='chat-area' className={`relative h-[85%] w-full m-auto pb-28 pt-14 overflow-y-auto flex flex-col items-center chat-scrollbar ${history && 'invisible md:visible'}`}>
      
        <Menu 
          onClick={()=>setHistory(true)}
          className={`cursor-pointer fixed inset-0 mt-4 ml-4 items-start gap-10 hover:opacity-40 ${history && 'invisible'}`}
          size='20'
        />

          {messages.map((message, index) => (
            <Message key={index} {...message} />
          ))}

        <div id='dummy-div' />
        <div className="fixed bottom-4 flex flex-col h-[15%] justify-center items-center bg-gray-700 w-[60%]">
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
              <div className={`absolute right-5 top-5 rounded-md cursor-pointer hover:opacity-80 bg-white ${message === '' && 'opacity-30'} ${loading && 'invisible'}`}>
                <ArrowUp 
                  color='black'
                />
              </div>
            </div>
          
          <p className='text-xs text-gray-400 mt-2'>
            QuantGenie can make mistakes. Consider checking important information.
          </p>
      </div>
      <ChevronLeft 
        className={`fixed left-[260px] hover:opacity-50 top-4 cursor-pointer ${history ? 'visible': 'invisible'}`}
        onClick={()=>setHistory(false)}
        size='20'
        color='gray'
      />
    </div>
  );
};

export default ChatSection;
