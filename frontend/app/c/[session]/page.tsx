"use client"

import { useEffect, useState } from "react";
import ChatSection from "../../../components/ChatSection";
import SidebarSection from "@/components/SideBar";
import AccountForm from "@/components/AccountForm";
import useAxios from "@/lib/axios";
import { IChat } from "@/lib/types";
import { useRecoilValue } from "recoil";
import { accessAtom, userAtom } from "@/store";
import { useQuery } from "@tanstack/react-query";
import { useRouter } from "next/navigation";

interface IChatParams {
  params: { 
    session: string 
  }
}

export default function Page({ params }: IChatParams) {

  const { session } = params

  const [history, setHistory] = useState(true)
  const [account, setAccount] = useState(false)
  const user = useRecoilValue(userAtom)
  const [chat, setChat] = useState<IChat | null>({
    id: '',
    user_id: user?._id,
    messages: [],
    chat_history: '',
    title: 'New Chat',
    last_accessed_date: new Date()
  })

  const accessToken = useRecoilValue(accessAtom)
  const router = useRouter()
  const refresh = typeof window !== 'undefined' ? localStorage.getItem('refreshToken') : null 

  const axios = useAxios()
  const { data: chatSession, error } = useQuery({
    queryKey: [`getChat-${session}`],
    queryFn: async ()=>{
      const res = await axios.get(`chat/${session}`)
      return res?.data
    }
  })

  useEffect(()=>{
    if (!refresh) {
      router.push('/')
      return
    }
    if (error) router.push('/c')
    setChat(chatSession)
  }, [chatSession, error])

  
  return (
    <div className="relative w-screen flex flex-row justify-center border-white/20 h-screen max-h-screen items-center overflow-hidden">
      <title>{chat?.title}</title>
      { history && <div className="relative h-screen max-w-[260px] w-[260px] px-4">          
          <SidebarSection 
            session={session} 
            setAccount={setAccount}
          />
      </div> }
      <div className="relative h-screen flex items-end w-full bg-gray-700 justify-center">
          <ChatSection 
            history={history}
            setHistory={setHistory}
            setAccount={setAccount}
            chat={chat}
            session={session}
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
