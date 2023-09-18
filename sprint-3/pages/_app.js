import '@/styles/globals.css'

import { Provider } from 'react-redux'
import store from '@/store/store'

import NavbarContextProvider from '@/contexts/NavbarContext'

export default function App({ Component, pageProps }) {

    return (
        <Provider store={store}>
            <NavbarContextProvider>
                <Component {...pageProps} />
            </NavbarContextProvider>
        </Provider>
    )
}
