import { useEffect } from 'react'

import { useRouter } from 'next/router'

import { useDispatch, useSelector } from 'react-redux'

import { initializeLoged } from '@/store/reducers/loginReducer'

import Header from './Header/Header';
import Navbar from './Navbar/Navbar';
import Footer from './Footer/Footer';
import Background from './Background';

export default function Layout({ children }) {
    const router = useRouter()
    const dispatch = useDispatch()
    const loggedUser = useSelector((state) => state.loggedUser)

    useEffect(() => {
        dispatch(initializeLoged())
        if (!loggedUser) {
            router.replace('/cuenta/login');
        }
    }, [dispatch, router, loggedUser])

    return (
        <>
            <Background />
            <Header />
            <Navbar />
            <main>{children}</main>
            <Footer />
        </>
    )
}