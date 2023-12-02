import styles from '@/styles/Login/TextBox.module.css'

import React, { useState, useContext } from 'react'

import { TypeContext } from '@/contexts/TypeContext'
import { IdContext } from '@/contexts/IdContext'

import OpenEye from "@/public/svg/OpenEye.svg";
import ClosedEye from "@/public/svg/ClosedEye.svg";

const InputBlock = () => {
    const type = useContext(TypeContext)
    const id = useContext(IdContext)

    const [input, setInput] = useState('')
    const [displayPassword, setDisplayPassword] = useState(false)

    if (type === 'text' || type === 'number' || type === 'email') {
        return <input 
            type={type}
            id={id}
            value={input}
            name={id}
            className={`${styles.input}`}
            onChange={({ target }) => setInput(target.value)}
            required
        />
    } else if (type === 'password') {
        return  (
            <div className={`${styles.passwordContainer}`}>
                <input
                    type={displayPassword ? 'text' : 'password'}
                    id={id} 
                    value={input}
                    name={id}
                    className={`${styles.input}`}
                    onChange={({ target }) => setInput(target.value)}
                    required
                />
                <button 
                    className={`${styles.buttonEye}`} 
                    type='button' onClick={ () => setDisplayPassword(!displayPassword) }
                >
                    <OpenEye className={`${displayPassword ? styles.hideIcon : styles.showIcon}`}/>
                    <ClosedEye className={`${displayPassword ? styles.showIcon : styles.hideIcon}`}/>
                </button>
            </div>
        )
    } else {
        return console.error('Unknown type: ' + type)
    }
}

const TextBox = ({ type = 'text', id = 'default', error='', children }) => {
    return (
        <IdContext.Provider value={id}>
            <TypeContext.Provider value={type}>
                <div className={`${styles.textBox}`}>
                    <label>{children}</label>
                    <div>
                        <InputBlock />
                        <div className={`${styles.error}`}>{error}</div>
                    </div>
                </div>
            </TypeContext.Provider>
        </IdContext.Provider>
    )
}

export default TextBox