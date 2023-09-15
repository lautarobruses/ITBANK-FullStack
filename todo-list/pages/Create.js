import { React, useState } from "react"

const Create = () => {
    const [user, setUser] = useState('')
    const [id, setId] = useState('')
    const [title, setTitle] = useState('')

    const Cargar = (event) => {
        event.preventDefault()
        const listado = {
            user: user,
            id: id,
            title: title,
            completed: false,
        }
        console.log(listado)
        setUser('')
        setId('')
        setTitle('')
    }

    return (
        <div>
            <form onSubmit={Cargar}>
                <label> Indicá tu usuario: </label>
                <input 
                    className="User" 
                    placeholder="Usuario"
                    onChange={({ target }) => setUser(target.value)}
                />

                <label>Indicá tu ID: </label>
                <input 
                    className="id"
                    placeholder="Id"
                    onChange={({ target }) => setId(target.value)}
                />

                <label>Indicá el título de la tarea: </label>
                <input 
                    className="title" 
                    placeholder="titulo"
                    onChange={({ target }) => setTitle(target.value)}
                />
                <button type='submit'>Cargar</button>
            </form>
        </div>
    )
}

export default Create