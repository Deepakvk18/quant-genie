"use client"

import { useForm } from "react-hook-form"
import { z } from "zod"
import { zodResolver } from "@hookform/resolvers/zod"
import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import Link from "next/link"
import { Eye, EyeOff } from "lucide-react"
import { useState } from "react"
import { useMutation } from "@tanstack/react-query"
import { useRouter } from "next/navigation"
import { useSetRecoilState } from 'recoil'
import { userAtom, accessAtom, refreshAtom } from "@/store"
import { TLogin, TLoginRes } from "@/lib/types"
import useAxios from "@/lib/axios"

const SignInForm = () => {

    const [showPassword, setShowPassword] = useState(false)

    const signInSchema =  z.object({
        email: z.string().email('Please enter a valid email'),
        password: z.string().min(8, 'Password must be at least 8 characters'),
    })

    const signInForm = useForm<z.infer<typeof signInSchema>>({
        resolver: zodResolver(signInSchema),
        defaultValues: {
            email: '',
            password: '',
        }
    })

    const axios = useAxios()

    const signInMutation = useMutation({
        mutationFn: async (data: TLogin)=>{
            const res = await axios.post('/login', data)
            return res?.data
        }
    })
    const router = useRouter()
    const setUser = useSetRecoilState(userAtom)
    const setAccess = useSetRecoilState(accessAtom)
    const setRefresh = useSetRecoilState(refreshAtom)

    const onSubmit = async (data: z.infer<typeof signInSchema>) => {        
        // console.log(data)
        const res = await signInMutation.mutateAsync(data)
        console.log("Before Mutataion", signInMutation.data);
        setUser(res?.user)
        setAccess(res?.access_token)
        setRefresh(res?.refresh_token)
        localStorage.setItem('refreshToken', res?.refresh_token)
        router.push('/c')
    }

  return (
    <div className="flex-col justify-center text-center">
        <p className="block text-2xl font-bold m-4">
            Welcome Back
        </p>
        <Form {...signInForm}>
        <form onSubmit={signInForm.handleSubmit(onSubmit)} className="space-y-3 w-full md:min-w-[300px]">
            <FormField
            control={signInForm.control}
            name="email"
            render={({ field }) => (
                <FormItem className="">
                <FormControl>
                    <Input className={`rounded-sm ${signInForm.formState?.errors?.email ? 'border-red-500 dark:border-orange-400': ''}`} placeholder="Enter your email" {...field} />
                </FormControl>
                <FormMessage className="dark:text-orange-400 text-xs"/>
                </FormItem>
            )}
            />
            <div className="relative">
                
              <FormField
              control={signInForm.control}
              name="password"
              render={({ field }) => (
                  <FormItem>
                  <FormControl>
                      <Input type={`${showPassword ? 'text': "password"}`} className={`rounded-sm ${signInForm.formState?.errors?.password ? 'border-red-500 dark:border-orange-400': ''}`} placeholder="Enter your password"  {...field} />
                  </FormControl>
                  <FormMessage className="dark:text-orange-400 text-xs"/>
                  </FormItem>
              )}
              />
              <div className="absolute right-3 top-2 z-10">
                { showPassword 
                  ? <EyeOff onClick= {() => setShowPassword(false)} className= "cursor-pointer"/>
                  : <Eye onClick={()=>setShowPassword(true)} className="cursor-pointer" /> }
              </div>
            </div>
              
            <div className="flex flex-col w-full justify-between items-center">
                <Link className="text-xs text-left my-2 hover:underline font-didact_gothic text-blue-700 dark:text-blue-300" href="/forgot-password">Forgot Password?</Link>
                <Button className="w-full rounded-sm bg-[#3C46FF] hover:bg-[#0000FF] text-white hover:" type="submit">Sign in with Email</Button>
            </div>
            <div className="text-xs my-2 font-didact_gothic">
            Don't have an account?
            <Link className="hover:underline text-blue-700 dark:text-blue-300" href="/signup"> Sign Up!</Link>
            </div>
        </form>
        <div className="w-full text-xs my-2 font-didact_gothic text-left">
            Go to homepage
            <Link className="hover:underline text-blue-700 dark:text-blue-300" href="/"> QuantGenie</Link>
        </div>
        </Form>
    </div>
  )
}

export default SignInForm