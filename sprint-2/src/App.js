import {
    BrowserRouter as Router, Routes, Route, Navigate
} from 'react-router-dom'
import React, { useState } from 'react'

import GlobalStyles from './components/GlobalStyles'
import Background from './components/Background'

import Home from './components/Home'
import Cuenta from './components/Main/Cuenta'
import Pagos from './components/Main/Pagos'
import Login from './components/Login/Login'
import LoginForm from './components/Login/LoginForm'
import FooterLogin from './components/Login/FooterLogin'
import RegisterForm from './components/Login/RegisterForm'

const App = () => {
    const [user, setUser] = useState(false)

    const login = (user) => {
        setUser(user)
    }

    return (
        <Router>
            <GlobalStyles /> {/*No funciona en React Native*/}
            <Background login={false}/>
            <Routes>
                <Route path='/' element={ user ? <Home /> : <Navigate replace to="/login"/> }>
                    {/* DENTRO DE ELEMENT VA EL COMPONENTE CORRESPONDIENTE A CADA RUTA */}
                    <Route index element={null} /> {/*Pagina de inicio*/}
                    <Route path="/cuenta" element={ <Cuenta /> } />
                    <Route path="/transferencias" element={null} />
                    <Route path="/pagos" element={ <Pagos /> } />
                    <Route path="/prestamos" element={null} />
                </Route>
                <Route path='/login' element={ <Login/> }>
                    <Route index element={ <><LoginForm onLogin={login}/><FooterLogin/></> } />
                    <Route path="/login/register" element={ <RegisterForm/> } />
                </Route>
            </Routes>
        </Router>
    )
    // return (
    //     <Router>
    //         <GlobalStyles /> {/*No funciona en React Native*/}
    //         <Login />
    //     </Router>
    // )
}

export default App