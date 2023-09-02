import GlobalStyles from './GlobalStyles'

import Footer from './components/Footer/Footer'
import Header from './components/Header/Header'
import Navbar from './components/Navbar/Navbar'

const App = () => {
    return (
        <>
            <GlobalStyles /> {/*No funciona en React Native*/}
            <Header />
            <Navbar />
            {/* Main */}
            <Footer />
        </>
    )
}

export default App