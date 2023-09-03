import {
    BrowserRouter as Router,
    Routes, Route
} from 'react-router-dom'

import { styled } from 'styled-components'

import GlobalStyles from './GlobalStyles'

import Footer from './components/Footer/Footer'
import Header from './components/Header/Header'
import Navbar from './components/Navbar/Navbar'

import background from '../src/assets/background.jpg'

const Background = styled.div`
    position: fixed;
    top: 10%;
    left: 15%;
    width: 100%;
    height: 90%;
    background-image: url(${background});
    background-size: cover;
    background-position: center;
    z-index: -1;
`

const App = () => {
    return (
        <Router>
            <GlobalStyles /> {/*No funciona en React Native*/}
            <Background />
            <Header />
            <Navbar />
            <Routes>
                {/* DENTRO DE ELEMENT VA EL COMPONENTE CORRESPONDIENTE A CADA RUTA */}
                <Route path="/" element={null} />
                <Route path="/cuenta" element={null} />
                <Route path="/transferencias" element={null} />
                <Route path="/pagos" element={null} />
                <Route path="/prestamos" element={null} />
            </Routes>
            <Footer />
        </Router>
    )
}

export default App