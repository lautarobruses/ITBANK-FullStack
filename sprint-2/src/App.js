import GlobalStyles from './GlobalStyles'

import Footer from './components/Footer'
import Header from './components/Header'
import Navbar from './components/Navbar'

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