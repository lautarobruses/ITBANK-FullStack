import {
    BrowserRouter as Router,
} from 'react-router-dom'

import GlobalStyles from './components/GlobalStyles'

// import Background from './components/Background'
// import Header from './components/Header/Header'
// import Navbar from './components/Navbar/Navbar'
// import Footer from './components/Footer/Footer'
// import Main from './components/Main/Main'
import Login from './components/Login/Login'


const App = () => {
    // return (
    //     <Router>
    //         <GlobalStyles /> {/*No funciona en React Native*/}
    //         <Background login={false}/>
    //         <Header />
    //         <Navbar />
    //         <Main />
    //         <Footer />
    //     </Router>
    // )

    return (
        <Router>
            <GlobalStyles /> {/*No funciona en React Native*/}
            <Login />
        </Router>
    )
}

export default App