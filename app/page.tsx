import Link from 'next/link';

export default function Home() {

  return (
    <div className="flex max-h-screen w-screen flex-col sm:supports-[min-height:100dvh]:min-h-[100dvh] md:grid md:grid-cols-2 lg:grid-cols-[60%_40%]">
      <div className="relative hidden flex-1 flex-col justify-center px-5 pt-8 text-[#FE7600] dark:text-[#D292FF] md:flex md:px-6 md:py-[22px] lg:px-8 bg-purple-500">
        <nav className="left-0 top-8 flex w-full px-6 sm:absolute md:top-[22px] md:px-6 lg:px-8">
          <h1 aria-label="ChatGPT by OpenAI">
            <div className="flex cursor-default items-center text-[20px] font-bold leading-none lg:text-[22px]">
              <div>QuantGenie<span className="">●</span></div>
            </div>
          </h1>
        </nav>
        <div className="flex flex-col text-[32px] leading-[1.2] md:text-[40px]" aria-hidden="true">
        </div>
      </div>
      <div className="relative flex grow flex-col items-center justify-between bg-white px-5 py-8 text-black dark:bg-black dark:text-white sm:rounded-t-[30px] md:rounded-none md:px-6">
        <div className="relative flex w-full grow flex-col items-center justify-center">
          <h2 className="text-center text-[20px] leading-[1.2] md:text-[32px] md:leading-8">Get started</h2>
          <div className="flex mt-5 w-full max-w-[440px] justify-center items-center">
            <div className="grid gap-x-3 gap-y-2 sm:gap-y-0 w-full">
            <div className="flex justify-center items-center flex-col gap-2">
              <div className="flex w-full gap-4">
                <Link href={'/login'} className="relative flex w-[50%] h-12 items-center justify-center rounded-md text-center text-base font-medium bg-[#3C46FF] text-[#fff] hover:bg-[#0000FF]" data-testid="login-button">
                <div className="relative -top-[1px]">Log in</div>
                </Link>
                <Link href={'/signup'} className="relative w-[50%] flex h-12 items-center justify-center rounded-md text-center text-base font-medium bg-[#3C46FF] text-[#fff] hover:bg-[#0000FF]">
                <div className="relative -top-[1px]">Sign up</div>
                </Link>
              </div>
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
