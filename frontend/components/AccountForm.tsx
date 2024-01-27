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
import { useState } from "react"
import Image from "next/image"
import Avatar from "react-avatar"
import { BadgeDollarSign } from 'lucide-react';
import { useRecoilValue } from 'recoil'
import { userAtom } from '@/store';

const AccountForm = ({ setAccount, buttons }) => {

    const user = useRecoilValue(userAtom)

  return (
    <div className="flex flex-col w-full min-w-[300px] items-start justify-center h-full">
        <div className="flex flex-col text-center justify-center items-center">
          <div className="grid grid-cols-[80%_20%] gap-2 p-4 w-full rounded-md">
            
            <div className="flex flex-col gap-1 items-start justify-center m-2">
              <h2 className="block text-2xl font-bold ">
                  { buttons && 'Your account'}
              </h2>
              <p className="text-xs">
                {user?.email}
              </p>
              <div className="flex flex-row gap-2">
                <BadgeDollarSign 
                  color="gold"
                />
                {user?.credits || 200}
              </div>
            </div>
            <div className="w-full mr-4 flex justify-end">
              <Avatar 
                className="rounded-full m-2" 
                name={user?.email}
                alt="profile-image" 
                size='40'
              />
            </div>
          </div>          
        </div>          
        { buttons && <div className="flex flex-row gap-2 px-4 pb-4 w-full justify-between">
          <Button 
              className="bg-[rgb(231,101,86)] w-1/2 hover:bg-[#ff4d4a] text-white"
              onClick={()=>setAccount(false)}>
              Back
          </Button>
          <Button 
            className="w-1/2 rounded-sm bg-[#3C46FF] hover:bg-[#0000FF] text-white" type="submit">
          Recharge
          </Button>
        </div>}
    </div>
  )
}

export default AccountForm;