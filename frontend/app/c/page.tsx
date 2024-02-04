"use client"

import { useState } from "react";
import ChatSection from "@/components/ChatSection";
import SidebarSection from "@/components/SideBar";
import AccountForm from "@/components/AccountForm";
import useAxios from "@/lib/axios";
import { useQuery } from '@tanstack/react-query'
import { IChat } from "@/lib/types";
import { useRecoilValue } from "recoil";
import { userAtom } from "@/store";

interface IChatParams {
  params: { 
    session: string 
  }
}

export default function Page() {

  const [history, setHistory] = useState(true)
  const [account, setAccount] = useState(false)
  const user = useRecoilValue(userAtom)
  
  const [chat, setChat] = useState<IChat>({
    id: '',
    user_id: user?._id,
    messages: [],
    chat_history: '',
    last_accessed_date: new Date()
  })
  
  return (
    <div className="relative w-screen flex flex-row justify-center border-white/20 h-screen max-h-screen items-center overflow-hidden">

      <title>New Chat</title>

      { history && <div className="relative h-screen max-w-[260px] w-[260px] px-4">          
          <SidebarSection 
            session={undefined} 
            setAccount={setAccount}
          />
      </div> }
      <div className="relative h-screen flex items-end w-full bg-gray-700 justify-center">
          <ChatSection 
            history={history}
            setHistory={setHistory}
            setAccount={setAccount}
            chat={chat}
            session={''}
          />
      </div>
      { account && <div className="absolute flex inset-0 z-50 w-screen min-h-screen justify-center items-center bg-gray-700/70 h-full">
        <div 
          className="flex justify-center items-center rounded-md bg-gray-800"
        >
          <AccountForm setAccount={setAccount} buttons={true}/>
      </div>
     </div> }
    </div>
  );
}
