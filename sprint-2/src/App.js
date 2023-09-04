import {
    BrowserRouter as Router,
} from 'react-router-dom'

import GlobalStyles from './components/GlobalStyles'

import Background from './components/Background'
import Header from './components/Header/Header'
import Navbar from './components/Navbar/Navbar'
import Footer from './components/Footer/Footer'
import Main from './components/Main/Main'

const App = () => {
    return (
        <Router>
            <GlobalStyles /> {/*No funciona en React Native*/}
            <Background />
            <Header />
            <Navbar />
            <Main />
            <Footer />
        </Router>
    )
}

export default App