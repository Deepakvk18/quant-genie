import Avatar from "react-avatar";
import { useRecoilValue } from 'recoil'
import { userAtom } from '@/store';

const Message = ({ sender, text }) => {
  
  const user = useRecoilValue(userAtom)
  
  return (
    <div 
      className={`flex flex-col message rounded-xl ${sender === 'Genie' ? 'bg-gray-600' : 'Genie-message'} w-[50%] my-2 p-4`}
    >
  
      <div className='flex w-full items-center'>
        <Avatar 
            src={ sender === 'user' ? '': '/QuantGenie.png'}
            name={sender === 'user' ? user?.email: ''}
            alt={`${sender}-avatar`}
            size='30'
            className='rounded-full -ml-8'
        />
        <strong>{sender === 'user' ? 'You' : 'Genie'}</strong> 
      </div>
      <div className='text-sm font-sans w-full flex break-all whitespace-pre-line flex-wrap'>
        {text}
      </div>
    </div>
  )};

  export default Message;