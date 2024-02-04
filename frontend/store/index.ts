import {
    atom
  } from 'recoil';
  import { TUser } from '@/lib/types';

export const userAtom = atom<TUser>({
    key: 'userAtom',
    default: {
        _id: '',
        email: '',
    },
})

export const accessAtom = atom<string | undefined>({
    key: 'accessAtom',
    default: undefined
})

export const refreshAtom = atom<string | undefined>({
    key: 'refreshAtom',
    default: undefined
})

