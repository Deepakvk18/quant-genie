"use client"

import Link from "next/link";
import Avatar from "react-avatar";
import { FileEdit } from "lucide-react";
import { useState } from "react";
import AccountForm from "./AccountForm";

const SidebarItem = ({ chatObject }) => (
  <div className="group">
    <Link href={`/c/${chatObject.id}`} className="flex items-center rounded-lg py-2 relative text-sm max-w-full whitespace-nowrap ">
        {chatObject.label.substr(0, 28).trim()}
    </Link>
  </div>
);

const SidebarSection = ({ title, items, session, setHistory }) => {  

  const [account, setAccount] = useState(false)

  const openNewChat = ()=>{
    
  }
  
  
  
  return (
  <div className="flex flex-col mt-2 w-full h-screen max-h-screen pb-24 duration-1000 transition-transform " data-projection-id="5" style={{ height: 'auto', opacity: 1 }}>
    <div onClick={openNewChat} className='flex w-full  items-center mb-4 cursor-pointer px-2 py-2 hover:bg-gray-400/20 rounded-lg'>
      <Avatar 
          src='/QuantGenie.png'
          alt='logo'
          size='30'
          className="rounded-full mr-2 shrink"
      />
      <p className="text-sm font-sans font-bold"> New Chat </p>
      <FileEdit
        size='20'
        className="absolute right-6"  
      />
    </div>
    <h2 className="flex font-semibold font-sans text-sm m-2 text-gray-500">
        Chat History
    </h2>
    <ol className="relative overflow-y-auto overflow-x-hidden">
      {items.map((item, index) => (
        <li className={`flex relative hover:bg-gray-400/20 rounded-md ${session === item.id ? 'bg-gray-400/20' : ''} px-2 my-1 w-full` }data-projection-id={index + 7} style={{ opacity: 1, height: 'auto' }} key={item.label}>
          <SidebarItem chatObject={item} />
        </li>
      ))}
    </ol>
    <div 
      className="absolute flex bottom-2 items-center cursor-pointer px-4 py-2 hover:bg-gray-400/20 rounded-lg"
      onClick={()=>setAccount(true)}
    >
        <Avatar 
            src='/QuantGenie.png'
            alt='logo'
            size='30'
            className="rounded-full mr-2"
        />
        <p className="text-sm font-sans font-semibold mr-16"> Your Account </p>
     </div>
     { account && <div className="absolute flex inset-0 z-50 w-screen min-h-screen justify-center items-center bg-gray-700/70 h-full">
        <div 
          className="min-w-[300px] w-[40%] p-16 rounded-md bg-gray-800"
        >
          <AccountForm setAccount={setAccount}/>
        </div>
     </div> }
  </div>
)};

export default SidebarSection;