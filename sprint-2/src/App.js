import {
    BrowserRouter as Router,
    Routes, Route
} from 'react-router-dom'

import GlobalStyles from './GlobalStyles'

import Footer from './components/Footer/Footer'
import Header from './components/Header/Header'
import Navbar from './components/Navbar/Navbar'

const App = () => {
    return (
        <Router>
            <GlobalStyles /> {/*No funciona en React Native*/}
            <Header />
            <Navbar />
            <Routes>
                <Route path="/" element={<h1>inicio</h1>} />
                <Route path="/cuenta" element={<h1>cuenta</h1>} />
                <Route path="/transferencias" element={null} />
                <Route path="/pagos" element={null} />
                <Route path="/prestamos" element={null} />
            </Routes>
            {/* Main */}
            <Footer />
        </Router>
    )
}

export default App