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
import Image from "next/image"

const AccountForm = ({ setAccount }) => {

    const [edit, setEdit] = useState(false)

    const editSchema =  z.object({
      name: z.string(),
      email: z.string().email(),
      'OpenAI API Key': z.string(),
      'FMP API Key': z.string(),
      'Google API Key': z.string(),
      'News API Key': z.string()
    })

    const editForm = useForm<z.infer<typeof editSchema>>({
        resolver: zodResolver(editSchema),
        defaultValues: {
            'OpenAI API Key': '',
            'FMP API Key': '',
            'Google API Key': '',
            'News API Key': ''

        }
    })

    const onSubmit = (data: z.infer<typeof signUpSchema>) => {        
       
    }

  return (
    <div className="flex w-full items-center justify-center h-full">
        <div className="flex flex-col text-center justify-center items-center">
          <div className="grid grid-cols-[30%_70%] w-full m-4 bg-purple-500">
            <div className="w-full">
              <Image 
                className="rounded-full m-2" 
                src={""} 
                alt="profile-image" 
                width={50}
            />
            </div>
            <div className="flex flex-col items-end justify-center m-2">
              <h2 className="block text-2xl font-bold ">
                  Your account
              </h2>
              <p className="text-xs">
                Email: abcdefgh@gmail.com
              </p>
            </div>
          </div>
          <Form {...editForm}>
          <form onSubmit={editForm.handleSubmit(onSubmit)} className="w-full md:min-w-[300px] md:grid md:grid-cols-2 gap-4">
              <FormField
              control={editForm.control}
              name="OpenAI API Key"
              render={({ field }) => (
                  <FormItem className="">
                  <FormControl>
                      <Input className={`rounded-sm`} type="password" placeholder="Enter your OpenAI API Key" {...field} />
                  </FormControl>
                  <FormMessage className="dark:text-orange-400 text-xs"/>
                  </FormItem>
              )}
              />
                <FormField
                control={editForm.control}
                name="FMP API Key"
                render={({ field }) => (
                    <FormItem>
                    <FormControl>
                        <Input type={`rounded-sm`} type="password" placeholder="Enter your FMP API Key" {...field} />
                    </FormControl>
                    <FormMessage className="dark:text-orange-400 text-xs"/>
                    </FormItem>
                )}
                />
              <FormField
              control={editForm.control}
              name="Google API Key"
              render={({ field }) => (
                  <FormItem>
                      <FormControl>
                          <Input type="password" className={`rounded-sm`} placeholder="Enter your Google API Key" {...field} />
                      </FormControl>
                      <FormMessage className="dark:text-orange-400 text-xs"/>
                  </FormItem>
              )}
              />
              <FormField
              control={editForm.control}
              name="News API Key"
              render={({ field }) => (
                  <FormItem>
                      <FormControl>
                          <Input type="password" className={`rounded-sm`} placeholder="Enter your News API Key" {...field} />
                      </FormControl>
                      <FormMessage className="dark:text-orange-400 text-xs"/>
                  </FormItem>
              )}
              />
            <button 
                className="bg-[rgb(231,101,86)] hover:bg-[#ff4d4a] text-white"
                onClick={()=>setAccount(false)}>
                Back
            </button>
            <Button className="w-full rounded-sm bg-[#3C46FF] hover:bg-[#0000FF] text-white" type="submit">
            Submit
            </Button>

          </form>
              
          </Form>
        </div>
    </div>
  )
}

export default AccountForm;