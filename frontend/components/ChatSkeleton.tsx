import { Skeleton } from "@/components/ui/skeleton"


const ChatSkeleton = () => {
  return (
    <div className="w-full"><div className="flex flex-col w-full items-center justify-end">
    <div 
      className={`flex flex-col rounded-xl w-[70%] sm:w-[50%] my-2 p-4`}
    >
      <div>
        <div className='flex w-full items-end'>
            <Skeleton className="h-8 w-8 rounded-full -ml-10" />
            <Skeleton className="flex rounded-md px-2 my-1 mx-2 w-[10%] h-6"/>
        </div>
        <div className='text-sm font-sans w-full'>
        <Skeleton className="flex rounded-md px-2 my-1 h-4 w-full"/>
            <Skeleton className="flex rounded-md px-2 my-1 h-4 w-full"/>
            <Skeleton className="flex rounded-md px-2 my-1 h-4 w-full"/>
            <Skeleton className="flex rounded-md px-2 my-1 h-4 w-[50%]"/>
        </div>
      </div>
    </div>
    <div 
      className={`flex flex-col message rounded-xl w-[70%] sm:w-[50%] my-2 p-4`}
    >
      <div>
      <div className='flex w-full items-end'>
            <Skeleton className="h-8 w-8 rounded-full -ml-10" />
            <Skeleton className="flex rounded-md px-2 my-1 mx-2 h-6 w-[15%]"/>
        </div>
        <div className='text-sm font-sans w-full'>
            <Skeleton className="flex rounded-md px-2 my-1 h-4 w-full"/>
            <Skeleton className="flex rounded-md px-2 my-1 h-4 w-full"/>
            <Skeleton className="flex rounded-md px-2 my-1 h-4 w-full"/>
            <Skeleton className="flex rounded-md px-2 my-1 h-4 w-full"/>
            <Skeleton className="flex rounded-md px-2 my-1 h-4 w-full"/>
            <Skeleton className="flex rounded-md px-2 my-1 h-4 w-full"/>
            <Skeleton className="flex rounded-md px-2 my-1 h-4 w-[30%]"/>
        </div>
      </div>
    </div>
  </div></div>
  )
}

export default ChatSkeleton