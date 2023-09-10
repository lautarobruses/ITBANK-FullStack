import Header from './Header/Header'
import Navbar from './Navbar/Navbar'
import Footer from './Footer/Footer'
import Main from './Main/Main'
// import { Outlet } from 'react-router-dom'

const Home = () => {
    return(
        <>
            <Header />
            <Navbar />
            <Main />
            <Footer />
        </>
    )
}

export default Home