"use client"

import Link from "next/link";
import Avatar from "react-avatar";
import { FileEdit } from "lucide-react";
import { useEffect, useState } from "react";
import HistorySkeleton from "./HistorySkeleton";
import { useRecoilValue, useResetRecoilState } from 'recoil'
import { accessAtom, refreshAtom, userAtom } from '@/store';
import { useQuery } from '@tanstack/react-query'
import useAxios from "@/lib/axios";
import { useRouter } from "next/navigation";
import { Power } from "lucide-react";


const SidebarItem = ({ chatObject }) => (
  <div className="group">
    <p className="flex items-center rounded-lg py-2 relative text-sm max-w-full whitespace-nowrap text-ellipsis">
        {chatObject.title}
    </p>
  </div>
);

const SidebarSection = ({ session, setAccount, setChatId }) => {  

  const user = useRecoilValue(userAtom)
  const [items, setItems] = useState([])
  const axios = useAxios()
  const router = useRouter()
  const resetRefresh = useResetRecoilState(refreshAtom)
  const resetAccess = useResetRecoilState(accessAtom)
  const resetUser = useResetRecoilState(userAtom)

  const { data: chats, isLoading } = useQuery({
    queryKey: [`chat-history-${user?._id}`],
    queryFn: async ()=>{
      const res = await axios.get('/chats')
      return res?.data
    }
  })

  useEffect(()=>{
    if (chats?.chats?.length !== 0) {
      setItems(chats?.chats)
    }
  }, [chats])

  return (
  <div className="flex flex-col mt-2 w-full h-screen max-h-screen pb-4 duration-1000 transition-transform" data-projection-id="5" style={{ height: 'auto', opacity: 1 }}>
    <div onClick={()=>router.push('/c')} className='flex w-full  items-center mb-4 cursor-pointer px-2 py-2 hover:bg-gray-400/20 rounded-lg'>
      <Avatar 
          src='/QuantGenie.png'
          alt='logo'
          size='30'
          className="rounded-full mr-2 shrink"
      />
      <Link href='/c' className="text-sm font-sans font-bold"> New Chat </Link>
      <FileEdit
        size='20'
        className="absolute right-6"  
      />
    </div>
    <h2 className="flex font-semibold font-sans text-sm p-2 text-gray-500">
        Chat History
    </h2>
    <ol className="relative overflow-y-auto overflow-x-hidden h-[75vh]">
      { isLoading ? 
          <HistorySkeleton /> : 
          items?.map((item) => (
            <Link 
              href={`/c/${item._id}`}
              className={`flex relative hover:bg-gray-400/20 rounded-md ${session === item._id ? 'bg-gray-400/20' : ''} px-2 my-1 w-full` } 
              key={item._id}
            >
              <SidebarItem chatObject={item} />
            </Link>
      ))}
    </ol>
    <div className="absolute flex flex-row w-[260px] bottom-0 left-0 py-2 px-4 gap-2">
      <div 
        className="flex mt-4 items-center cursor-pointer py-2 px-2 hover:bg-gray-400/20 rounded-lg w-full"
        onClick={()=>setAccount(true)}
      >
          <Avatar 
              name={user?.email}
              alt='logo'
              size='30'
              className="rounded-full mr-2"
          />
          <p className="text-xs font-sans font-semibold w-full"> Your Account </p>
      </div>
      <div 
        className="flex mt-4 items-center cursor-pointer py-2 px-2 hover:bg-gray-400/20 rounded-lg float-right"
        onClick={()=>{
          resetRefresh()
          resetAccess()
          resetUser()
          localStorage.clear()
          router.push('/')
        }}
      >   <Power 
            size='23'
            color="gray"
            className="rounded-full"
          />
      </div>
    </div>
  </div>
)};

export default SidebarSection;