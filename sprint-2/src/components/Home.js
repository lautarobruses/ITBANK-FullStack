import Header from './Header/Header'
import Navbar from './Navbar/Navbar'
import Footer from './Footer/Footer'
import Main from './Main/Main'
import NavbarContextProvider from './Contexts/NavbarContext'

const Home = () => {
    return(
        <NavbarContextProvider>
            <Header />
            <Navbar />
            <Main />
            <Footer />
        </NavbarContextProvider>
    )
}

export default Home