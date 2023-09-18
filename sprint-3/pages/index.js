import { useEffect } from 'react'

import { useRouter } from 'next/router'

import { useDispatch, useSelector } from 'react-redux'

import { initializeLoged } from '@/store/reducers/loginReducer'

import Layout from '@/components/layout'

export default function Home() {
    const dispatch = useDispatch()
    const router = useRouter();
    const loggedUser = useSelector((state) => state.loggedUser)

    useEffect(() => {
        dispatch(initializeLoged())
    }, [dispatch])

    useEffect(() => {
        if (!loggedUser) {
            router.replace('/account/login');
        }
    }, [loggedUser, router]);

    return (
        <div>
            <Layout pagina={'Inicio'}>
                <>
                    <h1>HOLA USUARIO</h1>
                </>
            </Layout>
        </div>
    )
}
