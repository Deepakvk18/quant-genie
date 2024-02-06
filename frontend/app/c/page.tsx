"use client"

import { useEffect, useState } from "react";
import ChatSection from "@/components/ChatSection";
import SidebarSection from "@/components/SideBar";
import AccountForm from "@/components/AccountForm";
import { useRouter } from "next/navigation";

export default function Page() {

  const [history, setHistory] = useState(true)
  const [account, setAccount] = useState(false)
  const [chatHistory, setChatHistory] = useState<string | undefined>(undefined)
  const [chatId, setChatId] = useState<string>('')
  const router = useRouter()

  useEffect(() => {
    if (chatId) router.push(`c/${chatId}`)
  }, [chatId])
  
  
  return (
    <div className="w-screen flex flex-row justify-center h-screen max-h-screen items-center">

      <title>New Chat</title>

      { history && <div className="h-screen max-w-[260px] w-[260px] min-w-[260px] px-4">          
          <SidebarSection 
            session={undefined} 
            setAccount={setAccount}
            setChatId={setChatId}
          />
      </div> }
      <div className="relative h-screen flex items-end w-full bg-gray-700 justify-center">
          <ChatSection 
            history={history}
            setHistory={setHistory}
            setAccount={setAccount}
            chatHistory={chatHistory}
            setChatHistory={setChatHistory}
            chatId={chatId}
            setChatId={setChatId}
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
