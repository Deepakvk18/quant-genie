import Avatar from "react-avatar";

const Message = ({ sender, text }) => (
    <div 
      className={`flex flex-col message rounded-md ${sender === 'Genie' ? 'bg-gray-600' : 'Genie-message'} w-[50%] my-2 py-2 px-2`}
    >
  
      <div className='flex w-full items-center'>
        <Avatar 
            src={ sender === 'user' ? '' : '/QuantGenie.png'}
            alt={`${sender}-avatar`}
            size='30'
            className='rounded-full -ml-8'
        />
        <strong>{sender === 'user' ? 'You' : 'Genie'}</strong> 
      </div>
      <div className='text-sm font-sans w-full flex overflow-wrap break-all whitespace-pre-line'>
        {text}
      </div>
    </div>
  );

  export default Message;