import '@/styles/globals.css'

import { Provider } from 'react-redux'
import store from '@/store/store'

import NavbarContextProvider from '@/contexts/NavbarContext'

import TransferContextProvider from '@/contexts/TransferContext'


export default function App({ Component, pageProps }) {

    return (
        <Provider store={store}>
            <NavbarContextProvider>
                <TransferContextProvider>
                    <Component {...pageProps} />
                </TransferContextProvider>
            </NavbarContextProvider>
        </Provider>
    )
}
