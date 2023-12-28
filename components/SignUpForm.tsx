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
import { useRouter } from "next/navigation"

const SignUpForm = () => {

    const [showPassword, setShowPassword] = useState(false)
    const router = useRouter()

    const signUpSchema =  z.object({
        email: z.string().email('Please enter a valid email'),
        password: z.string().min(8, 'Password must be at least 8 characters'),
        re_password: z.string().min(8, 'Password must be at least 8 characters'),
    }).refine(data => data.password === data.re_password, {
        message: 'Passwords do not match',
        path: ['re_password']
    })


    const signUpForm = useForm<z.infer<typeof signUpSchema>>({
        resolver: zodResolver(signUpSchema),
        defaultValues: {
            email: '',
            password: '',
            re_password: '',
        }
    })

    const onSubmit = (data: z.infer<typeof signUpSchema>) => {        
       
    }

  return (
    <div className="flex flex-col text-center">
        <p className="block text-2xl font-bold m-4">
            Create your account
        </p>
        <Form {...signUpForm}>
        <form onSubmit={signUpForm.handleSubmit(onSubmit)} className="space-y-3 w-full md:min-w-[300px]">
            <FormField
            control={signUpForm.control}
            name="email"
            render={({ field }) => (
                <FormItem className="">
                <FormControl>
                    <Input className={`rounded-sm ${signUpForm.formState?.errors?.email ? 'border-red-500 dark:border-orange-400': ''}`} placeholder="Enter your email" {...field} />
                </FormControl>
                <FormMessage className="dark:text-orange-400 text-xs"/>
                </FormItem>
            )}
            />
            <div className="relative">
              <FormField
              control={signUpForm.control}
              name="password"
              render={({ field }) => (
                  <FormItem>
                  <FormControl>
                      <Input type={`rounded-sm ${showPassword ? 'text': "password"}`} className={`${signUpForm.formState?.errors?.password ? 'border-red-500 dark:border-orange-400': ''}`}  placeholder="Enter your Password" {...field} />
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
            <FormField
            control={signUpForm.control}
            name="re_password"
            render={({ field }) => (
                <FormItem>
                    <FormControl>
                        <Input type="password" className={`rounded-sm ${signUpForm.formState?.errors?.re_password ? 'border-red-500 dark:border-orange-400': ''}`} placeholder="Confirm Password" {...field} />
                    </FormControl>
                    <FormMessage className="dark:text-orange-400 text-xs"/>
                </FormItem>
            )}
            />
            <div className="flex flex-col w-full items-center">
                <div className="w-full text-xs my-2 font-didact_gothic text-left">
                Already have an account?
                    <Link className="hover:underline text-blue-700 dark:text-blue-300" href="/login"> Login</Link>
                </div>

                <Button className="w-full rounded-sm bg-[#3C46FF] hover:bg-[#0000FF] text-white" type="submit">Signup with Email</Button>

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

export default SignUpForm