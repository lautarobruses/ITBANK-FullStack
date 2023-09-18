import Head from 'next/head';
import Header from './Header/Header';
import Navbar from './Navbar/Navbar';
import Footer from './Footer/Footer';
import Background from './Background';

export default function Layout({ children }) {
    return (
        <>
            <Head>
                <title>Nexus Bank</title>
                <meta
                    name='description'
                    content='App que permite administrar una lista de tareas'
                />
                <meta name='viewport' content='width=device-width, initial-scale=1' />
                <link rel='icon' href='/favicon.ico' />
            </Head>
            <Background />
            <Header />
            <Navbar />
            <main>{children}</main>
            <Footer />
        </>
    )
}