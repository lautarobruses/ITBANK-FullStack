import {
    BrowserRouter as Router, Routes, Route, Navigate
} from 'react-router-dom'

import React, { useEffect } from 'react'

import { useDispatch, useSelector } from 'react-redux'
import { initializeLoged } from './reducers/loginReducer'

import GlobalStyles from './components/GlobalStyles'
import Background from './components/Background'
import Inicio from './components/Main/Inicio'
import Cuenta from './components/Main/Cuenta'
import Pagos from './components/Main/Pagos'
import Login from './components/Login/Login'
import LoginForm from './components/Login/LoginForm'
import FooterLogin from './components/Login/FooterLogin'
import RegisterForm from './components/Login/RegisterForm'
import Home from './components/Home'
import PageNotFound from './components/PageNotFound'
import ComingSoon from './components/ComingSoon'

const App = () => {
    const dispatch = useDispatch()
    const loggedUser = useSelector((state) => state.loggedUser)

    useEffect(() => {
        dispatch(initializeLoged())
    }, [dispatch])

    return (
        <Router>
            <GlobalStyles /> {/*No funciona en React Native*/}
            <Background />
            <Routes>
                <Route path='/' element={ <Home /> }>
                    <Route index element={<Inicio />} /> {/*Pagina de inicio*/}
                    <Route path="/cuenta" element={ <Cuenta /> } />
                    <Route path="/transferencias" element={null} />
                    <Route path="/pagos" element={ <Pagos /> } />
                    <Route path="/prestamos" element={null} />
                </Route>
                <Route path='/login' element={ loggedUser ? <Navigate replace to="/"/> : <Login /> }>
                    <Route index element={
                        <>
                            <LoginForm />
                            <FooterLogin/>
                        </>
                    } />
                    <Route path="/login/register" element={ <RegisterForm/> } />
                </Route>
                <Route path='/coming-soon' element={ <ComingSoon/> } />
                <Route path='*' element={ <PageNotFound/> } />
            </Routes>
        </Router>
    )
}

export default App