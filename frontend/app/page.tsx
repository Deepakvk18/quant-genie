"use client"

import { useState } from 'react';
import { TypeAnimation } from 'react-type-animation';
import HomeScreen from '@/components/HomeScreen';
import SignInForm from '@/components/SignInForm';
import SignUpForm from '@/components/SignUpForm';
import { useRouter } from 'next/navigation';

export default function Page() {

  const [screen, setScreen] = useState('/')
  const refresh = typeof window !== 'undefined' ? localStorage.getItem('refreshToken') : null 
  const router = useRouter()

  if (refresh) router.push('/c')

  return (
    <div className="flex max-h-screen w-screen flex-col sm:supports-[min-height:100dvh]:min-h-[100dvh] md:grid md:grid-cols-2 lg:grid-cols-[60%_40%]">
      <title>QuantGenie - Your pocket Financial Assistant</title>
      <div className="relative hidden flex-1 flex-col justify-center px-5 pt-8 text-[#FE7600] dark:text-[#D292FF] md:flex md:px-6 md:py-[22px] lg:px-8 bg-[rgba(210,146,255)]/30">
        <nav className="left-0 top-8 flex w-full px-6 sm:absolute md:top-[22px] md:px-6 lg:px-8">
          <h1>
            <div className="flex cursor-default items-center text-[20px] font-bold leading-none lg:text-[22px]">
              <div>QuantGenie<span className="">●</span></div>
            </div>
          </h1>
        </nav>
        <div className="flex flex-col text-[32px] leading-[1.2] md:text-[40px] w-full" >
          <TypeAnimation
            className='flex bg-transparent text-white w-full flex-wrap'
            sequence={[
              'Quant-genie: Your AI-powered financial advisor.', 500,
              'Unleash the power of technical, fundamental, and behavioral analysis.', 500,
              'Gain insights from market sentiment and make informed investment decisions.', 500,
              'Quant-genie: Your personalized path to financial success.', 500,
              "Let's get started!",
            ]}
            speed={2}
            omitDeletionAnimation
            wrapper='strong'
            repeat={Infinity}
            />
        </div>
      </div>
      <div className="relative flex grow flex-col items-center justify-between bg-white px-5 py-8 text-black dark:bg-black dark:text-white sm:rounded-t-[30px] md:rounded-none md:px-6">
        <div className="relative flex w-full grow flex-col items-center justify-center">
          { screen === '/' && <h2 className="text-center text-[20px] leading-[1.2] md:text-[32px] md:leading-8">Get started</h2> }
          <div className="flex mt-5 w-full max-w-[440px] justify-center items-center">
            <div className="grid gap-x-3 gap-y-2 sm:gap-y-0 w-full">
            <div className="flex justify-center items-center flex-col gap-2">
              { screen === '/' && <HomeScreen setScreen={setScreen} /> }
              { screen === '/login' && <SignInForm setScreen={setScreen} /> }
              { screen === '/signup' && <SignUpForm setScreen={setScreen} /> }
          </div>
            </div>
          </div>
        </div>
        <div className="mt-10 flex flex-col justify-center ">
        </div>
      </div>
    </div>
  );
}
