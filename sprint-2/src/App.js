import {
    BrowserRouter as Router,
    Routes, Route
} from 'react-router-dom'

import GlobalStyles from './components/GlobalStyles'


import Background from './components/Background'
import Header from './components/Header/Header'
import Navbar from './components/Navbar/Navbar'
import Footer from './components/Footer/Footer'

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