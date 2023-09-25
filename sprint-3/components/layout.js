import Header from './Header/Header';
import Navbar from './Navbar/Navbar';
import Footer from './Footer/Footer';
import Background from './Background';

export default function Layout({ children }) {
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