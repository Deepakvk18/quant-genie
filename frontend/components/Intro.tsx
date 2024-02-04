import React from 'react'
import Avatar from 'react-avatar'
import { useRecoilValue } from 'recoil'
import { userAtom } from '@/store';
import AccountForm from './AccountForm';
import { BadgeDollarSign } from 'lucide-react';

const Intro = ({ setAccount }) => {

    const user = useRecoilValue(userAtom)

  return (
    <div className='flex flex-col gap-x-8 flex-wrap w-[80%] lg:w-[50%] bg-slate-600 rounded-xl p-4 text-sm'>
        <div className='flex lg:flex-row gap-4'>
            <div className='flex flex-row gap-4 items-center w-1/2'>
                <Avatar 
                    src={'/QuantGenie.png'}
                    alt={`genie-avatar`}
                    size='40'
                    className='rounded-full'
                />
                <h2 className='text-xl font-semibold'>
                    QuantGenie
                </h2>
            </div>
            <div 
                className='flex flex-row gap-2 w-1/2 py-2 justify-end items-center hover:bg-black rounded-md cursor-pointer'
                onClick={()=>setAccount(true)}
            >
                <div className='flex flex-col gap-1 items-end text-center'>
                    <p className="text-xs">
                        {user?.email}
                    </p>
                    <div className="flex flex-row gap-2 items-center justify-center">
                    <BadgeDollarSign 
                        color="gold"
                    />
                    {user?.credits || 200}
                    </div>
                </div>
                <Avatar 
                    className="rounded-full mr-2" 
                    name={user?.email}
                    alt="profile-image" 
                    size='40'
                />
            </div>
        </div>
        <h3 className='flex text overflow-auto text-wrap flex-wrap'>
        Hi. I'm QuantGenie, your friendly finance assistant! I'm here to help you navigate the exciting world of the stock market with my expertise in technical, fundamental, and sentimental analysis. Just give me a ticker symbol and I'll whip up a comprehensive analysis using fancy images and insightful data.
        <br /><br />
        Think of me as your financial compass, guiding you towards informed investment decisions. Whether you're a seasoned trader or a curious beginner, I'm here to make the market less intimidating and more rewarding. Ask me anything about a stock's financials, trends, or market sentiment, and I'll do my best to provide clear, actionable insights.
        <br /><br />
        So, fire away! What stock would you like to dive into today? Remember, I can handle one at a time to ensure the analysis is thorough and accurate. Let's make some smart investment moves together!
        </h3>
    </div>
  )
}

export default Intro