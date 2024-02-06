import Avatar from "react-avatar";
import { useRecoilValue } from 'recoil'
import { userAtom } from '@/store';
import { IMessage } from "@/lib/types";
import Image from "next/image";

const Message = (message: IMessage) => {
  
  const user = useRecoilValue(userAtom)
  
  return (
    <div className="flex flex-col w-full items-center justify-end">
      {message?.input && <div 
        className={`flex flex-col message rounded-xl w-[70%] sm:w-[50%] my-2 p-4`}
      >
        <div>
          <div className='flex w-full items-end'>
            <Avatar 
                name={user?.email}
                alt={`${user?.email}-avatar`}
                size='30'
                className='rounded-full -ml-8'
            />
            <strong>You</strong> 
          </div>
          <div className='text-sm font-sans w-full flex break-all whitespace-pre-line flex-wrap'>
            {message?.input}
          </div>
        </div>
      </div>}
      { message?.output && <div 
        className={`flex flex-col message rounded-xl bg-gray-600 w-[70%] sm:w-[50%] my-2 p-4 ${message?.output?.error && 'ring-1 bg-red-500/60'}`}
      >
        <div>
          <div className='flex w-full items-end'>
            <Avatar 
                src={'/QuantGenie.png'}
                alt={`genie-avatar`}
                size='30'
                className='rounded-full -ml-8'
            />
            <strong>Genie</strong> 
          </div>
          <div className='text-sm font-sans w-full flex break-all whitespace-pre-line flex-wrap'>
            {message?.output?.text}
          </div>
        </div>
        <ul className="flex flex-row flex-wrap gap-2 my-2">
          { message?.output?.images?.map((url)=>
            <Image 
              key={url}
              className="rounded-md"
              src={'/QuantGenie.png'}
              alt="graph"
              width={100}
              height={100}
            />
          )}
        </ul>
      </div> }
    </div>
  )};

  export default Message;