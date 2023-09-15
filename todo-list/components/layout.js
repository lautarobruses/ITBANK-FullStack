import Head from 'next/head';
import Footer from './Footer';
import NavBar from './Navbar';

export default function Layout({ children }) {
    return (
        <>
            <Head>
                <title>ToDo List</title>
                <meta
                    name='description'
                    content='App que permite administrar una lista de tareas'
                />
                <meta name='viewport' content='width=device-width, initial-scale=1' />
                <link rel='icon' href='/favicon.ico' />
            </Head>
            <NavBar />
            <main>{children}</main>
            <Footer />
        </>
    )
}