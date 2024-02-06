import { Skeleton } from "@/components/ui/skeleton"


const HistorySkeleton = () => {
  return (
    <div>
        <Skeleton className="flex h-8  px-2 my-1 w-full"/>
        <Skeleton className="flex h-8  px-2 my-1 w-full"/>
        <Skeleton className="flex h-8  px-2 my-1 w-full"/>
        <Skeleton className="flex h-8  px-2 my-1 w-full"/>
    </div>
  )
}

export default HistorySkeleton