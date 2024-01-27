import {
    atom,
    selector,
    useRecoilState,
    useRecoilValue,
  } from 'recoil';
  import { TUser } from '@/lib/types';

export const userAtom = atom<TUser | undefined>({
    key: 'userAtom',
    default: undefined,
})

export const accessAtom = atom<string | undefined>({
    key: 'accessAtom',
    default: undefined
})

export const refreshAtom = atom<string | undefined>({
    key: 'refreshAtom',
    default: undefined
})

