"use client"

import { useState } from "react";
import ChatSection from "../../../components/ChatSection";
import SidebarSection from "@/components/SideBar";

export default function Page({ params }) {
  const sidebarItems = [
    {
      title: 'Today',
      items: [
        { id: '0bae2fcd-c159-4342-ad17-88e8d3360b32', label: 'Next.js Homepage Example By CHatGPT and BArd Comparison' },
        { id: '26abf7af-298d-4045-9778-7ca65cb747a9', label: 'Pandas DataFrame Column Query' },
        { id: '0bae2fcd-c159-4342-ad17-88e8d3360b32', label: 'Next.js Homepage Example By CHatGPT and BArd Comparison' },
        { id: '26abf7af-298d-4045-9778-7ca65cb747a9', label: 'Pandas DataFrame Column Query' },
        { id: '0bae2fcd-c159-4342-ad17-88e8d3360b32', label: 'Next.js Homepage Example By CHatGPT and BArd Comparison' },
        { id: '26abf7af-298d-4045-9778-7ca65cb747a9', label: 'Pandas DataFrame Column Query' },
        { id: '0bae2fcd-c159-4342-ad17-88e8d3360b32', label: 'Next.js Homepage Example By CHatGPT and BArd Comparison' },
        { id: '26abf7af-298d-4045-9778-7ca65cb747a9', label: 'Pandas DataFrame Column Query' },
      ],
    },
    // Add more sidebar sections as needed
  ];

  const { session } = params

  const [history, setHistory] = useState(true)

  

  return (
    <div className="relative w-screen flex flex-row justify-center border-white/20 h-screen max-h-screen items-center overflow-hidden">
      { history && <div className="relative h-screen max-w-[260px] w-[260px] px-4">          
          <SidebarSection 
            title="Today" 
            items={sidebarItems[0].items} 
            session={session} 
            setHistory={setHistory}
          />
      </div> }
      <div className="relative h-screen flex items-end w-full bg-gray-700 justify-center">
          <ChatSection 
            setHistory={setHistory}
            history={history}
          />
      </div>
    </div>
  );
}
