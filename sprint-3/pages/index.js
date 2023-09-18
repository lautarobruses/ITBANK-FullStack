import { useEffect } from 'react'

import { useDispatch } from 'react-redux'

import { initializeLoged } from '@/store/reducers/loginReducer'

import Layout from '@/components/layout'

export default function Home() {
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(initializeLoged())
    }, [dispatch])

    return (
        <Layout>
            <>
                <h1>HOLA USUARIO</h1>
            </>
        </Layout>
    )
}
