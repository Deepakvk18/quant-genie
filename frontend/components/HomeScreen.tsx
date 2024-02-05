
const HomeScreen = ({ setScreen }) => {
  return (
    <div className="flex w-full gap-4">
        <p onClick={()=>setScreen('/login')} className="relative flex w-[50%] h-12 items-center justify-center rounded-md text-center text-base font-medium bg-[#3C46FF] text-[#fff] hover:bg-[#0000FF]" data-testid="login-button">
        <span className="relative -top-[1px]">Log in</span>
        </p>
        <p onClick={()=>setScreen('/signup')} className="relative w-[50%] flex h-12 items-center justify-center rounded-md text-center text-base font-medium bg-[#3C46FF] text-[#fff] hover:bg-[#0000FF]">
        <span className="relative -top-[1px]">Sign up</span>
        </p>
    </div>
  )
}

export default HomeScreen